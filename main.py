from email import message
from unicodedata import name
import discord
import random

from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType
from discord_slash import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, wait_for_component, create_select, \
    create_select_option
from pkg_resources import require

bot = commands.Bot(command_prefix="!", description = "Bot enchère")
slash = SlashCommand(bot, sync_commands = True)
guild_ids = [990173638080757760]

@bot.event
async def on_ready():
	print("Prêt à casser des cul")

@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
    channel = bot.get_channel(990187024516526130)
    await channel.send(f"Le message de {message.author.mention} a été supprimé \n> {message.content}")

@bot.event
async def on_message_edit(before, after):
    channel = bot.get_channel(990187024516526130)
    await channel.send(f"{before.author.mention} a édité son message :\n> Avant -> {before.content}\n> Après -> {after.content}")


@slash.slash(name="clear", description="supprime_des_messages", guild_ids=[990173638080757760])
@commands.has_role(990214824409579560)
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@slash.slash(name= "départ", description= "définir le prix de départ", guild_ids=[990173638080757760], options=[
    create_option(name= "montant", description= "montant de départ", option_type=4, required= True),
    create_option(name= "date", description= "date de fin des enchères", option_type=3, required= True),
    create_option(name= "gain", description= "gain de l'enchère", option_type=3, required= True)
])
@commands.has_role(990214008059600898)

async def départ(ctx, montant, date, gain):

    embed = discord.Embed(title=f"**Début de l'enchère pour {gain}**",description= f"L'enchère commence à **{montant}**€\n\n**➜** Petit rappel : vous êtes dans l'obligation d'avoir votre prénom/nom rôleplay sur ce serveur discord afin d'enchérir\n\n**➜** Pour enchérir, il vous suffura de faire la commande **/enchérir** dans ce salon accompagné du montant\n\n**➜** Vous pouvez surenchérir d'un minimum de 15 000 € au cas contraire votre offre sera supprimée.", color=0x2d85e7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/990173638080757763/990210468335468604/Auction-PNG-Transparent-Image.png")
    embed.add_field(name= "Date de fin d'enchère", value=date)
    await ctx.send(embed=embed)

@slash.slash(name= "enchérir", description= "enchérir sur une enchère", guild_ids=[990173638080757760], options=[
    create_option(name= "montant", description= "montant de votre offre", option_type=4, required= True)
])

async def enchérir(ctx, montant):

    embed = discord.Embed(title="**Une nouvelle offre !**",description= f"**{ctx.author.mention}** propose **{montant} €** pour cette enchère ! qui dit mieux ?", color=0x2d85e7)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/990173638080757763/990210468335468604/Auction-PNG-Transparent-Image.png")
    await ctx.send(embed=embed)

@slash.slash(name= "finir", description= "Finir l'enchère", guild_ids=[990173638080757760], options=[
    create_option(name= "gagnant", description= "nom du gagant de l'enchère", option_type=6, required= True),
    create_option(name= "prix", description= "Prix de vente", option_type=4, required= True),
    create_option(name= "gain", description= "gain de l'enchère :", option_type=3, required= True)
])
@commands.has_role(990214008059600898)

async def finir(ctx, gagnant, prix, gain):

    embed = discord.Embed(title="**L'enchère prend fin !**",description= f"**{gagnant.mention}** remporte l'enchère et gagane **{gain}** pour **{prix}** €\n\n**ADJUGÉ VENDU !**", color=0xa8ea66)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/990173638080757763/990210468335468604/Auction-PNG-Transparent-Image.png")
    await ctx.send(embed=embed)

bot.run("OTkwMTg0MDI4MzYxNjAxMDc0.GJgP30.yMFRnbpFKTZaTDBDeCUTMpf1n_-Wd5EC2Lt0Rc")