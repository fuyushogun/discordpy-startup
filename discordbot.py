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

#with open(join_us.csv, encofing='UTF-8')as f:
#    reader = f.randlines()

l =["高木", "吉見", "浅尾", "荒木", "小田"]

joinus =['高木「ちんぽ！ちんぽ！ほら！お前らも出せ！」\n'\
    '吉見「監督！俺たちこんなこんなことするくらいなら練習が…！」\n'\
    '高木「うるさい黙れ素人が！そんなことよりファンサービスだ！浅尾を見習え！」\n'\
    '浅尾「…ジョッ…ジョイナアアアアアアアススススススススゥ！！！」\n'\
    'おはＤ「キャー！浅尾きゅんのM字開脚おちんぽユニコーンのオマケ付きよぉおおお！！！」\n'\
    '高木「ちんぽ！ちんぽ！ちんぽ！さあみんなでジョイナス！ファンと共に！」',\
    '高木「清原が逮捕されてプロ野球の将来が危うい... 田島！球界のためワシと一緒にちんぽ出せ！！」\n'\
    '浅尾(二軍)\n'\
    '小田(引退)\n'\
    '高木「小田、君は現行犯だ。ついでに言うと、執行猶予もない。しかしなんで前から噂があったにもかかわらず清原は逮捕されなかったんでしょうか」\n'\
    '福谷(二軍)\n'\
    '荒木「落合さんならもっと早く逮捕できたのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！中日も立浪のように能力と人格を併せ持った選手を育成しろ！」\n'\
    '坂井(失脚)\n'\
    '吉見(怪我)']

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

@bot.command()
async def us(ctx):
    await ctx.send(choice(joinus))

#@bot.command()
#async def us(ctx):
#    await ctx.send(choice(f))

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
