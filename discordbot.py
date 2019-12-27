from discord.ext import commands
import os
import traceback

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
    
@bot.event
async def on_message(message):
    # 「チンポ」で始まるか調べる
    if message.content.startswith("おはよう"):
        #botは無視
        if bot.user != message.author:
            #めっせーじ
            m = "おちんぽジョイナス！" + message.author.neme + "さん!!!"
            #メッセージが送られてきたチャンネルへメッセージを送る
            await message.bot.send(m)


bot.run(token)
