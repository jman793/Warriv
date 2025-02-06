import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

MESSAGE = """No doubt you've heard about the tradegy that befell the town of Tristram.
Some say that Diablo, the Lord of Terror, walks the world again."""

GUILD_ID = os.environ['GUILD_ID']

# From https://www.hostinger.com/tutorials/how-to-host-discord-bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # Ensure the bot's tree is initialized before syncing
    if bot.tree is not None:
        try:
            synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))  # Sync commands to a specific guild
            print(f"Synced {len(synced)} commands to {GUILD_ID}")
        except Exception as e:
            print(f"Sync failed: {e}")
    else:
        print("Bot tree not initialized!")

# define a new slash command that takes in elements related to a Monster Hunter hunt.

@bot.tree.command(name="hunt", description="Track a monster hunt")
async def hunt(
    interaction: discord.Interaction,
    monster: str,
    tempered: str,
    carts: int,
    party: str  # Accepts a comma-separated string
):
    # Convert comma-separated string to a list (handle empty input safely)
    party_list = [member.strip() for member in party.split(",") if member.strip()] if party else []

    # Create JSON response
    response_data = {
        "monster": monster,
        "tempered": tempered,
        "carts": carts,
        "party": party_list
    }
    json_response = json.dumps(response_data, indent=4)

    await interaction.response.send_message(f"```json\n{json_response}\n```")

bot.run(os.environ['DISC_TOKEN'])
