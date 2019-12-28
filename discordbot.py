from discord.ext import commands
import os
import traceback
import re
from random import randint, choice
import csv

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


s = '高木「ちんぽ！ちんぽ！ほら！お前らも出せ！」\n'\
    '吉見「監督！俺たちこんなこんなことするくらいなら練習が…！」\n'\
    '高木「うるさい黙れ素人が！そんなことよりファンサービスだ！浅尾を見習え！」\n'\
    '浅尾「…ジョッ…ジョイナアアアアアアアススススススススゥ！！！」\n'\
    'おはＤ「キャー！浅尾きゅんのM字開脚おちんぽユニコーンのオマケ付きよぉおおお！！！」\n'\
    '高木「ちんぽ！ちんぽ！ちんぽ！さあみんなでジョイナス！ファンと共に！」'

#join_us = open("join_us.csv", "r", encoding="UFT-8")
#f = csv.reader(join_us)

l =["高木", "吉見", "浅尾", "荒木", "小田"]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send(s)

@bot.command()
async def join(ctx):
    await ctx.send(choice(l))

# test終了につき凍結
#@bot.command()
#async def neko(ctx):
#    await ctx.send('にゃーん')

@bot.event
async def on_message(message):
    #メッセージ送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # ちんぽが含まれていたら？？？
    if re.search("おちんぽ", message.content):
        await message.channel.send("ジョイナス!")

    if re.search("落合", message.content):
        await message.channel.send("黙れ素人が！")



    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)



@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')


bot.run(token)
