import discord
from discord.ext import commands
from discord import app_commands
import random
import string

# --- Token ide jön ---
TOKEN = "TOKEN"

# --- License generálás ---
def generate_license_key():
    characters = string.ascii_uppercase + string.digits
    parts = [''.join(random.choices(characters, k=5)) for _ in range(4)]
    return "TZ-" + '-'.join(parts)

def generate_multiple_keys(amount):
    keys = set()
    while len(keys) < amount:
        keys.add(generate_license_key())
    return list(keys)

# --- Bot setup ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bejelentkezve mint {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash parancsok szinkronizálva: {len(synced)}")
    except Exception as e:
        print(f"Hiba a szinkronizálásnál: {e}")

# --- /generatetz parancs ---
@bot.tree.command(name="generatetz", description="Generál TZ formátumú kulcsokat")
@app_commands.describe(db="Hány darabot generáljon?")
async def generatetz(interaction: discord.Interaction, db: int):
    if db < 1 or db > 50:
        await interaction.response.send_message("1 és 50 között adj meg számot.", ephemeral=True)
        return

    keys = generate_multiple_keys(db)
    formatted = "\n".join(keys)
    await interaction.response.send_message(f"🎟️ **Generált kulcsok:**\n```\n{formatted}\n```")

# --- /generatetzx parancs (ugyanaz, csak más név) ---
@bot.tree.command(name="generatetzx", description="Generál TZ formátumú kulcsokat alternatív paranccsal")
@app_commands.describe(db="Hány darabot generáljon?")
async def generatetzx(interaction: discord.Interaction, db: int):
    if db < 1 or db > 50:
        await interaction.response.send_message("1 és 50 között adj meg számot.", ephemeral=True)
        return

    keys = generate_multiple_keys(db)
    formatted = "\n".join(keys)
    await interaction.response.send_message(f"🎟️ **Generált kulcsok:**\n```\n{formatted}\n```")

# --- Indítás ---
bot.run(TOKEN)

