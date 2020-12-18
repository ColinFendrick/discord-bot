import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
	guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

	members = '\n - '.join([member.name for member in guild.members])
	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})\n'
		f'Guild Members:\n - {members}'
	)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)
