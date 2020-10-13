#
# INTERMEDIARY COPY
# GO TO NEXT COMMIT
#


import asyncio
import auraxium
from auraxium import ps2

client = auraxium.Client()

async def main():
    async with auraxium.Client() as client:
        # Get the character data as an object
        # Go over this again. It works, but it doesn't seem smart.
        char = await get_char_by_name('lawfulevilboi')

        # Print info
        print("Name:\t\t" + char.name())
        print("Faction:\t" + str(await char.faction()))
        # I think the outfit name is different from the others because
        # we need to call its constructor first (char.outfit())
        outfit = await char.outfit()
        print("Outfit:\t\t" + str(outfit.name()))
        print("Online:\t\t" + str(await char.is_online()))


# Probably gonna delete this function
async def get_char_by_name(name: str, client: auraxium.Client=client):
    char = await client.get_by_name(ps2.Character, name)
    return char

# This is how we run these async functions.
#asyncio.get_event_loop().run_until_complete(main())
