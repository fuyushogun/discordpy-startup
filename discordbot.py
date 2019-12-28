from discord.ext import commands
import os
import traceback
import re
from random import randint, choice

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.event
async def on_message(message):
    #メッセージ送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # ちんぽが含まれていたら？？？
    if re.search("おちんぽ", message.content):
        await message.channel.send("ジョイナス!")

    if re.match("!join", message.content):
        with open('join?us.csv', encoding='UFT-8') as f:
            join = f.randlines()
        await message.channel.send(join)


    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)

#起動時にあいさつ
@bot.event
async def on_ready():
    CHANNEL_ID = 660146537242034197
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おちんちんジョイナス！ファンと共に！')

    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)


@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')


bot.run(token)
