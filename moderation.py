# NICHT MEHR GENUTZT

import sqlite3
import discord
import sys
import keys
import random
import asyncio

client = discord.Client()
mlist = open("config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')


@client.event
async def on_message(message):

    # Mod hinzufügen
    if message.author.id == (keys.pmcid or keys.pxlid) and message.content.lower().startswith('p.madd'):
        user = message.mentions[0]
        mod = user.id
        madd = open("config/mods.txt", "a", encoding='utf-8')
        madd.write('"{0}"'.format(mod) + "\n")
        await client.send_message(message.channel, "{0} wurde erfolgreich den Mods hinzugefügt".format(user.name))
        madd.close()

    # Anti invite
    if ('discord'.lower() in message.content.lower()) and (message.author.id not in keys.exceptions):
        if 'discord.me'.lower() in message.content.lower():
            user = message.author
            aif = open("config/invite.txt", "r", encoding='utf-8')
            ainv = aif.readlines()
            anti = random.choice(ainv)
            await client.delete_message(message)
            await client.send_message(message.channel, anti + " " + user.mention)
        if 'discord.gg'.lower() in message.content.lower():
            user = message.author
            aif = open("config/invite.txt", "r", encoding='utf-8')
            ainv = aif.readlines()
            anti = random.choice(ainv)
            await client.delete_message(message)
            await client.send_message(message.channel, anti + " " + user.mention)


    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        mlist.close()
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)


client.run(keys.token)
