import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
   
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
client.run(os.getenv('TOKEN'))