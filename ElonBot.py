import discord
from discord.ext import commands
TOKEN = 'NTU3Mjk5NDk3MDM5MDM2NDM2.XLViYA.g3B_VWA8xr8TP86vcbX5Rbrxa5o'
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def whymydolphinstopworkinglmao(ctx):
    await ctx.send('HAHAHHAHAHAHAHAHAH')

@bot.command()
async def clear(ctx, amount=100):
	await ctx.channel.purge(limit=amount)
    

bot.run(TOKEN)
