#!/usr/bin/env python3

###########
# IMPORTS #
###########

import discord
from discord.utils import get
from discord.ext import commands

import libs.config as config

import json
import random
import os
from dotenv import load_dotenv

load_dotenv()

####################
# Config variables #
####################

c_prefix = config.get_config("prefix")
c_cogs = config.get_config("cogs")
c_on_join_role = config.get_config("roles")["on_join"]

####################
# String variables #
####################

s_status = config.get_string("status")

############
# Bot init #
############

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix=c_prefix, intents=intents)

##########
# EVENTS #
##########

# Logging the starting of the bot into the console.
@bot.event
async def on_ready():
    print("Bot is ready!")

    # Set bot status
    if s_status != "":
        await bot.change_presence(activity=discord.Game(s_status))

#  Auto-assign role
@bot.event
async def on_member_join(member):
    global c_on_join_role
    role = get(member.guild.roles, name = c_on_join_role)
    await member.add_roles(role)

####################
# Loading the cogs #
####################

if __name__ == "__main__":

    # Remove default help command to cogs.help
    bot.remove_command("help")

    # Load all the cogs
    if len(c_cogs) != 0:
        print("Loading all COGS:")
        for cog in c_cogs:
            try:
                bot.load_extension(cog)
                print(f"\t{cog} loaded successfully!")
            except commands.ExtensionError as e:
                print(f'\tAn error occurred while loading {cog}\n\tReason:\n\t{e}')

# Starting the bot
bot.run(os.getenv("BOT_TOKEN"))
