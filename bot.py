import discord
import random



client = discord.Client()

@client.event
async def on_ready():
    print('This shit works man, you can chill now ~ {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dice = bool(random.getrandbits(1))

    if dice = True:
        if message.content.startswith('$hello'):
        await message.channel.send('sup bitch')

        if message.content.contains('$is the bot online','bot are you online','is bot online'):
        await message.channel.send('yas')

client.run('OTU5MTQ4MTMyNTQzOTIyMTk3.YkXqTg.W5dY777aECWFCk3PGIJUIwuO2Jg')
