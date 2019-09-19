import random
import discord
from discord.ext import commands

client = discord.Client()
x = discord.ClientUser
commands = commands.Bot(command_prefix='!')
a = random.randrange(1, 100)
b = 0
c = 0
d = 0


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("Alpha Testing...")
    await client.change_presence(status=discord.Status.idle, activity=game)


@commands.command(name="c", aliases=["공지"], rest_is_raw=True)


@client.event
async def on_message(message):
    id = message.author.id
    channel = message.channel

    if message.content.startswith("!test"):
        await message.channel.send("test!!!!")

    if message.content.startswith("!도움말"):
        await message.channel.send("```!도움말 \n!test \n!hi \n!룰렛 \n!숫자맞추기(오류)가 있습니다.```")

    if message.content.startswith("!hi"):
        await message.channel.send("I'm Discord BOT")

    if message.content.startswith("!룰렛"):
        await message.channel.send("룰렛을 돌립니다.")
        await message.channel.send(random.randrange(1, 10))
        await message.channel.send(random.randrange(1, 10))
        await message.channel.send(random.randrange(1, 10))
    if message.content.startswith("!숫자맞추기"):
        await message.channel.send("1부터 100까지 중 랜덤한 숫자를 만들었습니다.")
        while True:
            if message.content.startswith("%s", b):
                if a > b:
                    await message.channel.send("작습니다.")
                elif a < b:
                    await message.channel.send("큽니다.")
                elif a == b:
                    await message.channel.send("같습니다.")
                    break

client.run('token')