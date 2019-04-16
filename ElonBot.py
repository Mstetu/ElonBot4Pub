import discord
from discord.ext import commands

TOKEN = 'NTU3Mjk5NDk3MDM5MDM2NDM2.D3GUhQ.PjrnPjf_mdsLVdIcXCo7UXM1NXg'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot Is Ready')

@client.command()
async def whymydolphinstopworkinglmao():
    await client.say('HAHAHAHAHAHHAHAHA')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')

client.run(TOKEN)
