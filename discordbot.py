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


@bot.event()
async def on_message(message):
    #botを無視
    if message.author.bot:
        return
    #おちんぽ？
    if message.content == 'おちんぽ':
        await message.channel.send('ジョイナス!!!')
        
@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')
        

bot.run(token)
