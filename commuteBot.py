import discord
import datetime
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("출퇴근")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    id = message.author.id
    if message.content.startswith("!출"):
        embed = discord.Embed(title="출근", description="닉네임 : <@{0}>".format(id), color=0x00ff00, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="출근 시간 ")
        await message.channel.send(embed=embed)
    if message.content.startswith("!퇴"):
        embed = discord.Embed(title="퇴근", description="닉네임 : <@{0}>".format(id), color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="퇴근 시간 ")
        await message.channel.send(embed=embed)

client.run('token')
