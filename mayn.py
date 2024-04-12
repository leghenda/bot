import discord
from discord.ext import commands
from bot_logic import gen_pass
from model import get_class
import os
import requests

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send( gen_pass(10))
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    

bot.command()
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        



            
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{file_name}')
            await ctx.send(get_class(model_path='./keras_model.h5',labels_path='labels.txt', image_path=f'./{file_name}'))
    else:
        await ctx.send("вы не загрузили картинку")
                

bot.run("MTE2NTE5MzUyMjY2ODg5NjM1Ng.GyC2HY.C_H6Da00tXd8aJoei6AuY-qZ_t7WeVDO8XcIA8")
