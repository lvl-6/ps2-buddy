###############################################################################
# ./lib/api/playerinfo.py
#
# Author: John C <lvl-6.github.io>
# Created: 13/10/2020
#
# Description:
# Responsible for getting info regarding players (i.e. not general map data),
# and returning in a format the bot can understand.
#
###############################################################################

import asyncio
import auraxium
from auraxium import ps2

client = auraxium.Client()

async def basic_info(
        name: str,
        client: auraxium.Client = client,
        ):
    # Get the character data as an object (auraxium.ps2.Character)
    char = await client.get_by_name(ps2.Character, name)

    # Print info
    print("Name:\t\t" + char.name())
    print("Faction:\t" + str(await char.faction()))
    outfit = await char.outfit()
    print("Outfit:\t\t" + str(outfit.name()))
    print("Online:\t\t" + str(await char.is_online()))


# This is how we run these async functions.
#asyncio.get_event_loop().run_until_complete(basic_info('player_name_here'))
