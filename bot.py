import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')
	guild = discord.utils.get(client.guilds, name=GUILD)

	members = '\n - '.join([member.name for member in guild.members])
	print(
		f'{bot.user.name} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})\n'
		f'Guild Members:\n - {members}'
	)

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)


@bot.command(
	name='51',
	help='Gives a random hk 51 quote'
)
async def fifty_one(ctx, side: str):
	hk51_quotes = [
		'I kill to serve!',
		'The Maker marked you; nothing personal.',
		'You\'re already dead! Just lie down!'
	]

	if (side == 'Republic'):
		hk51_quotes = hk51_quotes + [
			'Statement: The Republic is "great", I "love" deleting Imperial troublemakers.'
		]
	elif side == 'Empire':
		hk51_quotes = hk51_quotes + [
			'Declaration: Our Imperial liquidations goes well.'
		]

	response = random.choice(hk51_quotes)
	await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='new-nagabot-channel'):
	guild = ctx.guild
	existing_channel = discord.utils.get(guild.channels, name=channel_name)
	if not existing_channel:
		print(f'Creating a new channel: {channel_name}')
		await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
