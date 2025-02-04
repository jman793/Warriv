import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

MESSAGE = """No doubt you've heard about the tradegy that befell the town of Tristram.
Some say that Diablo, the Lord of Terror, walks the world again."""

# From https://www.hostinger.com/tutorials/how-to-host-discord-bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def greet(ctx):
    response = MESSAGE
    await ctx.send(response)

@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

bot.run(os.environ['DISC_TOKEN'])
