#Copyrghit .../Leonardo\...
#Version 1.0
#Python 3.9.5
#NomeBOT= SacraMuerte
#SocialNetwok Discord: ᲼᲼᲼᲼᲼᲼᲼᲼          「✞♛Leoภⱥℝdo♛✞」#9537
#Contatto Telegram: @IzzySec 


from asyncio.tasks import wait
from distutils.command.config import config
from http import client
from subprocess import CREATE_NEW_PROCESS_GROUP
from turtle import title
from unicodedata import name
from discord.ext import commands
from discord import permissions
import discord
import random
import asyncio
from discord.ext.commands import Bot

print("------------------------")
print("❌OFFLINE | BOT OFFLINE")
print("------------------------")
token = "OTM0ODg0OTU5MjM4Mzg5ODMx.Ye2ldw.sBZtPgmajLqy-uvQpx5TCY7EBtg"
client = commands.Bot(command_prefix = '!')

#Presentazione del bot 
@client.command()
async def info(ctx):
    await ctx.send("Copyrghit .../Leonardo\... -- Version 1.0 -- #Python 3.9.5 -- #NomeBOT= SacraMuerte -- #SocialNetwok Discord: ᲼᲼᲼᲼᲼᲼᲼᲼          「✞♛Leoภⱥℝdo♛✞」#9537 --  #Contatto Telegram: @IzzySec")



#SALA-EVENTI
@client.event
async def on_ready():
    print('✅ONLINE | BOT ONLINE')
    print("------------------------")

#SALA-HELP_COMMAND
@client.event
async def on_message(message):
    if message.content.startswith('!comandi'):
        embedVar = discord.Embed(title="SacraMuerte", description="ECCO A TE I COMANDI", color=0x00ff00)
        embedVar.add_field(name="!clear", value="serve per eliminare i messaggi", inline=False)
        embedVar.add_field(name="!ban", value="serve per bannare un user", inline=False)
        embedVar.add_field(name="!kick", value="serve per kickkare un user", inline=False)

        await message.channel.send(embed=embedVar)


#SALA_COMANDI
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100000000):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=None)


#SALA-ACCENSIONE
client.run(token)


