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
    

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.event
async def on_message(message):
    #メッセージ送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # ちんぽが含まれていたら？？？（部分一致）
    if message.content in "おちんぽ":
        await message.channel.send("ジョイナス!!!")
        
    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)


    
    
        
@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')
        

bot.run(token)
