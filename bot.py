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
    elif message.author != client.user:
        dice = bool(random.getrandbits(1))

        if "hello bot" in message.content.lower():
                await message.channel.send('sup bitch')

        if "is the bot online" in message.content.lower():
                await message.channel.send('yas')
        if "bot lets have sex" in message.content.lower():
                await message.channel.send('**moans**')
        if "bot" and "some d" in message.content.lower():
                await message.channel.send('B===D--')
        if "who's right" in message.content.lower():
            member = random.choice(message.guild.members)
            await message.channel.send(member.mention + ' is right')
       
        if "bot" and "good metal artist" in message.content.lower():
            await message.channel.send('idk, i\'d pick ' + random.choice(open('artists.txt').readlines()))
        if "how does a computer work" in message.content.lower():
            await message.channel.send('computer go brrr')

        if "bot work" in message.content.lower():
            await message.channel.send('shh... it\'s a secret ;\)')

        if "bot" and "trans people" in message.content.lower():
            await message.channel.send('Trans woman \( noun \): A man who was so upset about his small penis he decided he was gonna be bullied less by switching genders')

        if dice == True:
           if "hello bot" in message.content.lower():
               await message.channel.send('sup bitch')
        else:
            if "hello bot" in message.content.lower():
                await message.channel.send('fuck u')
            else:
                return

client.run('your token goes here')
