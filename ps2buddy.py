###############################################################################
# ps2-buddy
# ./ps2buddy.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 28/09/2020
#
# Description:
# A generally helpful bot for people who play PlanetSide 2.
# Makes use of the Daybreak's Census API to pull game data.
#
###############################################################################

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase

import lib.logging as logging

version = '0.1'
bot_token = os.getenv('PS2BUDDY_TOKEN')


###############################################################################
# Bot Initialisation
###############################################################################

# We will load only the cogs in this list for security reasons.
extensions = ['cogs.hello'] # TODO

bot = BotBase(
    command_prefix = commands.when_mentioned,
    description = 'I help with PlanetSide 2 related stuff.',
    owner_ids = 0,
    case_insensitive = True,
    )

# Program is running as main (i.e. not imported by another program)
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
        logging.print_log('Loaded extension: ' + extension)

@bot.event
async def on_connect():
    logging.print_log('Bot has connected to Discord.')

@bot.event
async def on_disconnect():
    logging.print_log('Bot has disconnected from Discord.')

@bot.event
async def on_ready():
    logging.print_log('Bot is ONLINE and READY.')


###############################################################################
# Program Execution
###############################################################################

bot.run(bot_token)
