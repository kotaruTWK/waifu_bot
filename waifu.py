import discord
from discord.ext import commands
import booru
import asyncio
import random
import json
from coder import *
from shitpost import *
from rateWaifu import *
from getWaifu import *

# https://discordapp.com/oauth2/authorize?&client_id=379825486873886720&scope=bot&permissions=0

intents = discord.Intents.default()
intents.message_content = True

# Bot token in the quotes
bot_token = "Mzc5ODI1NDg2ODczODg2NzIw.GQkJIT.O5K4X3ULY4ANHJyNplXt3WDdncGE8LIQv7uTPw"

"""Changes Made:
Prefix modifier (fix help and ERR prefixes)
multiple channels"""


#prefix


def fileinfo(get, message):
    print("enter fileinfo. Message content: ")
    print(message.content+'\n')
    with open('data.json', 'r+', encoding='UTF-8') as file:
        data = json.load(file)
        #print(data)
        guildID = str(message.guild.id)
        #print(data['data'])
        if guildID in data['data']:
            print("enter if")
            if get == 'p':
                print("enter if P")
                newp = message.content.split(" ")
                data['data'][guildID]['Prefix'] = newp[1]
                file.seek(0)
                json.dump(data, file, indent=4)
                return data['data'][guildID]['Prefix']
        else:
            print("enter if not p")
            tempdict = {guildID : {'Server Name' : message.guild.name, 'Prefix' : '.', 'Shortcuts' : {}}}
            print(data)
            data['data'].update(tempdict)
            print(data)
##            data['data'][guildID]['Server Name'] = message.guild.name
##            data['data'][guildID]['Prefix'] = '.'
##            data['data'][guildID]['Shortcuts'] = {}
        file.seek(0)
        json.dump(data, file, indent=4)
        return data['data'][guildID]['Prefix']

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as {} {}\n".format(client.user.name, client.user.id))
    
@client.event
async def on_message(message):
    #print(message.channel.id)
    p = fileinfo('', message)
    
    if message.content.startswith(p+"test"):
        #await message.channel.send(str(message.author.roles))
        print(str(message.author.roles))

    if message.content.startswith(p+"hide"):
        await client.change_presence(status=discord.Status.invisible)

    if message.content.startswith(p+"unhide"):
        await client.change_presence(status=discord.Status.online)

    if message.content.startswith(p+"brb"):
        tmp = await message.channel.send("https://media1.tenor.com/images/984eb3f07a32810bcd550d4c40764ba7/tenor.gif")
        tmp = await message.channel.send("Give "+str(message.author.display_name)+" some time alone... It would seem they are... preoccupied.")
        
    if message.content.startswith(p+"hentai"):
        content = message.content.replace(p+"hentai", "")
        imgs = booru.Gelbooru()
        res = await imgs.search(query=content, random=True, gacha=True, block="-rating:safe -rating:general -rating:sensitive")
        embed = discord.Embed(title="You like what you see?", description="tags searched: "+str(content), color=0xaad4ff)
        embed.set_image(url=booru.resolve(res)["file_url"])
        await message.channel.send(embed = embed)
        
    if message.content.startswith(p+"r34"):
        content = message.content.replace(p+"r34", "")
        imgs = booru.Rule34()
        res = await imgs.search(query=content, random=True, gacha=True)
        embed = discord.Embed(title="You did this to yourself.", description="tags searched: "+str(content), color=0xaad4ff)
        embed.set_image(url=booru.resolve(res)["file_url"])
        await message.channel.send(embed = embed)
    
    if message.content.startswith(p+"anna"):
	    embed = discord.Embed(title="Anna's Streams", description="Join Anna's newest streaming endeavor as she explores the new frontiers of her 18+ life by visiting her at one of these!", color=0xaad4ff)
	    embed.add_field(name="Twitch", value="[https://www.twitch.tv/it_meanna](https://www.twitch.tv/it_meanna)", inline=True)
	    embed.add_field(name="Only Fans", value="[https://www.onlyfans.com/it_meanna](https://www.onlyfans.com/it_meanna)", inline=True)
	    await message.channel.send(embed = embed)
	
    if message.content.startswith(p+"waifu"):
        content = message.content.replace(p+"waifu", "")
        embed = discord.Embed(title="Is this your waifu?", description="", color=0xaad4ff)
        imgs = booru.Safebooru()
        res = await imgs.search(query=content, random=True, gacha=True)
        embed.set_image(url=booru.resolve(res)["file_url"])
        await message.channel.send(embed=embed)

    if "owo" in message.content.lower():
        await message.channel.send(str(shitPost("owo")))

    if "rawr" in message.content.lower():
        await message.channel.send(str(shitPost("rawr")))

    if message.content.startswith(p+"rate"):
        content = message.content.replace(p+"rate", "")
        await message.channel.send(rateWaifu(str(content)))
	
    if message.content.startswith(p+"change"):
        oldP = p
        p = fileinfo('p', message)
        await message.channel.send("Prefix changed from '"+oldP+"' to '"+p+"'")
        
    if message.content.startswith(p+"code"):
        if message.content.startswith(p+"code "):
            content = str(message.content).split(" , ")
        else:
            content = str(message.content).split(",")
        content.remove(content[0])
        if len(content)==2:
            coded = coder(content[0], content[1])
        elif len(content) == 1:
            coded = coder(content[0])
        elif len(content) == 3:
            if content[1] == "" or content[1] == " ":
                coded = coder(content[0])
            else:
                coded = coder(content[0], content[1])
            await message.channel.send(discord.User(id = getID(content[2])), coded)
            return
        else:
            coded = "Please include a message or properly seperate your command. Refer to "+p+"help for proper usage."
        await message.channel.send(coded)

    if message.content.startswith(p+"decode"):
        if message.content.startswith(p+"decode "):
            content = str(message.content).split(" , ")
        else:
            content = str(message.content).split(",")
        content.remove(content[0])
        if len(content) == 2:
            decoded = decoder(content[0], content[1])
        elif len(content) == 1:
            decoded = decoder(content[0])
        elif len(content) == 3:
            if content[1] == "" or content[1] == " ":
                decoded = decoder(content[0])
            else:
                decoded = decoder(content[0], content[1])
            await message.channel.send(discord.User(id = getID(content[2])), decoded)
            return
        else:
            decoded = "Please include a message or properly seperate your command. Refer to "+p+"help for proper usage."
        await message.channel.send(decoded)

    if message.content.startswith(p+"say"):
        if "bot host" in [y.name.lower() for y in message.author.roles]:
            print(message.content.split(" ")[1])
            channel = client.get_channel(379672766103683075)
            print(channel)
            builder = ""
            for i in range(2, len(str(message.content).split(" ")), 1):
                builder += str(message.content).split(" ")[i] + " "
            await channel.send(builder)

    """if message.content.startswith(p+"play"):
        channel = message.channel
        channel.connect
        #vc = await channel.connect(channel)
        #vc.play(discord.FFmpegPCMAudio('porn star dancing.mp3'))
        """
            
    if message.content.startswith(p+"help"):
        embed = discord.Embed(title="Help", description=" ", color=0xaad4ff)
        if "bot host" in [y.name.lower() for y in message.author.roles]:            
            embed.add_field(name="Say(Admin)", value=p+"say <channel name> <message>", inline=True)
            embed.add_field(name="Change Prefix(Admin)", value=p+"change <new prefix>", inline=True)
            embed.add_field(name="Hide(Admin)", value="Make bot appear offline. \nUsage: "+p+"hide", inline=True)
            embed.add_field(name="Unhide(Admin)", value="Make bot appear online. \nUsage: "+p+"unhide", inline=True)
        embed.add_field(name="BRB", value="Use when you will be back later. \nUsage: "+p+"brb", inline=True)
        embed.add_field(name="Code Message", value="Codes message using custom cypher.\nUsage: "+p+"code,<message to code>,<keyword (optional)>", inline=True)
        embed.add_field(name="Decode Message", value="Decodes message using custom cypher.\nUsage: "+p+"decode,<message to decode>,<keyword (optional)>", inline=True)
        embed.add_field(name="How to Shitpost", value="say 'OwO' or 'rawr'", inline=True)
        embed.add_field(name="Rate Someone", value="Rate a person (real or fictional) out of 100. \nUsage: "+p+"rate <name>", inline=True)
        embed.add_field(name="Get Hentai", value="Search Gelbooru for hentai. \nUsage: "+p+"hentai <tags>", inline=True)
        embed.add_field(name="Get Waifu Pic", value="Attempts to grab a random picture of your waifu from Safebooru. \nUsage: "+p+"waifu <name>", inline=True)
        embed.add_field(name="Get Hentai R34", value="Search R34 for hentai.(furry is inevitable). \nUsage: "+p+"r34 <tags>", inline=True)
        embed.add_field(name="Anna", value="Shows Anna's Twitch and future ventures. \nUsage: "+p+"anna", inline=True)
        await message.channel.send(embed=embed)


client.run(bot_token)
