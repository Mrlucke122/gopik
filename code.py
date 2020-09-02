import discord
from discord.ext import commands
import random
from random import choice
from random import randint
import os

bot = commands.Bot(command_prefix='r!')
bot.remove_command('help')


@bot.event
async def on_ready():
    activity = discord.Game(name="r!help")
    await bot.change_presence(activity=discord.Game(name="r!help"))


@bot.command()
async def kill(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send('{} <:firearmpistolweapongunpngfavpngF:715978412967067788>  {}.'.format(member.mention, ctx.message.author.mention))


@bot.command()
async def thxallah(ctx):
    await ctx.message.delete()
    await ctx.send(
        ' {} благодарит аллаха اللَّهُ اكْبَرُﺃﻋُﻮﺫُ بِاللَّهِ ﻣِﻦَ ﺍﻟﺸَّﻴْﻄَﺎﻥِ ﺍﻟﺮَّﺟِﻴ **https://www.youtube.com/watch?v=C-V9vStmsLA**'.format(
            ctx.author.mention))
    
@bot.group()
async def кто(ctx):
    print("who")

@bot.command()
async def гей(ctx):
    await ctx.send(choice(ctx.guild.members).mention)

@bot.command()
async def plsallah(ctx):
    await ctx.message.delete()
    num = randint(1, 3)
    if num == 1:
        await ctx.send('Аллах сжалился, и воскресил {}'.format(ctx.author.mention))
    elif num == 2:
        await ctx.send('Аллах отправил {} в джаннат'.format(ctx.author.mention))
    elif num == 3:
        await ctx.send('Аллах разгневался, и отправил {} в джаханнам'.format(ctx.author.mention))


@bot.command()
async def siska(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/699070101369913367/738475041712242768/GqqHaiPK6gI.jpg')


@bot.command()
async def namaz(ctx):
    await ctx.message.delete()
    await ctx.send(
        ' {} сделал намаз اللَّهُ اكْبَرُﺃﻋُﻮﺫُ بِاللَّهِ ﻣِﻦَ ﺍﻟﺸَّﻴْﻄَﺎﻥِ ﺍﻟﺮَّﺟِﻴ ||https://www.youtube.com/watch?v=mE6C0lQNmUU||'.format(
            ctx.author.mention))


@bot.command()
async def sex(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send('{} трахнул {}'.format(ctx.author.mention, member.mention))


@bot.group(invoke_without_command=True)
async def gay(ctx):
    print("pytin")


@gay.command()
async def game(ctx):
    random_number = randint(1, 100)
    if random_number >= 1 and random_number <= 10:
        await ctx.send(f"***{ctx.author.mention} Поздравляем! Вы натурал!***")
    elif random_number >= 11 and random_number <= 14:
        await ctx.send(f"***{ctx.author.mention} Вас трахнул в попку Рикардо Милос!***")
    elif random_number >= 15 and random_number <= 20:
        await ctx.send(f"***{ctx.author.mention} Рикардо Милос зафлексил вас до смерти!***")
    elif random_number >= 21 and random_number <= 30:
        await ctx.send(f"***{ctx.author.mention} Вас выебал в рот Ван Даркхолм!***")
    elif random_number >= 31 and random_number <= 34:
        await ctx.send(
            f"***{ctx.author.mention} Вас изнасиловали в анус эльфийки с огромными сиськами и огромными членами!***")
    elif random_number >= 35 and random_number <= 40:
        await ctx.send(f"***{ctx.author.mention} Вы ассексуальны, вас никто не привлекает в сексуальном плане!***")
    elif random_number >= 41 and random_number <= 45:
        await ctx.send(f"***{ctx.author.mention} Вас затащили в ад демоны, и выебали вас во все дырки!***")
    elif random_number >= 46 and random_number <= 50:
        await ctx.send(f"***{ctx.author.mention} Вы девушка!***")
    elif random_number >= 51 and random_number <= 54:
        await ctx.send(f"***{ctx.author.mention} Вас выебали страпоном!***")
    elif random_number >= 55 and random_number <= 60:
        await ctx.send(f"***{ctx.author.mention} Вас трахнул трап!***")
    elif random_number >= 61 and random_number <= 65:
        await ctx.send(f"***{ctx.author.mention} Вас выебал в анус кабан!***")
    elif random_number >= 65 and random_number <= 70:
        await ctx.send(f"***{ctx.author.mention} Вы жёстко отсосали коню, а потом он вас трахнул в анус!***")
    elif random_number >= 71 and random_number <= 75:
        await ctx.send(f"***{ctx.author.mention} Вы одинокий гей... у вас нет парня...***")
    elif random_number >= 76 and random_number <= 78:
        await ctx.send(f"***{ctx.author.mention} Сатана украл у вас хуй.***")
    elif random_number >= 79 and random_number <= 80:
        await ctx.send(f"***{ctx.author.mention} Вас изнасиловал Леон Бравл Старс.***")
    elif random_number >= 81 and random_number <= 84:
        await ctx.send(f"***{ctx.author.mention} Вам подсыпали снотворное в кофе, и выебали вас во все дырки!***")
    elif random_number >= 85 and random_number <= 87:
        await ctx.send(f"***{ctx.author.mention} Вы стали Fuckin Slave у Dungeon Master***")
    elif random_number >= 88 and random_number <= 90:
        await ctx.send(f"***{ctx.author.mention} Вы попали в Gachimuchi***")
    elif random_number >= 91 and random_number <= 94:
        await ctx.send(f"***{ctx.author.mention} Вы не гей, но ваш анус проткнуло пикой, и вы умерли!***")
    elif random_number >= 95 and random_number <= 99:
        await ctx.send(f"***{ctx.author.mention} Вы анимешник***")
    else:
        await ctx.send(
            f"***{ctx.author.mention} Вас затащили в ад суккубы, и вы ёбете их каждый день, и да, вы натурал на 300%. ***||Шанс выпадение этого 1%, вам повезло!||")


@bot.command()
async def ban(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send('{} забанил {}!'.format(ctx.author.mention, member.mention))


@bot.command()
async def terrorist(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send('{} взорвал {} اللهم ارحمني! قتله! باسمك! بسم الله الحق!'.format(ctx.author.mention, member.mention))


@bot.command()
async def buisnes(ctx):
    await ctx.message.delete()
    await ctx.send('Мы открываем бизнес, мы будем делать бабки https://www.youtube.com/watch?v=6VqCFnHXoYU')


@bot.command()
async def spit(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send('{} плюнул в {}'.format(ctx.author.mention, member.mention))


@bot.command()
async def cry(ctx):
    await ctx.message.delete()
    await ctx.send('{} всплакнул'.format(ctx.author.mention))


# Альтернативный help

@bot.command()
async def rg(ctx):
    emb = discord.Embed(title='Рофло-Игры')
    emb.add_field(name='gay game'.format(bot), value='Запустить тест на гея!')
    await ctx.send(embed=emb)


@bot.command()
async def islam(ctx):
    emb = discord.Embed(title='Ислам команды')
    emb.add_field(name='allah'.format(bot), value='Помолиться аллаху')
    emb.add_field(name='plsallah'.format(bot), value='Попросить Аллаха воскресить тебя')
    emb.add_field(name='namaz'.format(bot), value='Сделать намаз')
    emb.add_field(name='terrorist'.format(bot), value='Объявить джихад')
    emb.add_field(name='thxallah'.format(bot), value='Поблагодарить аллаха')
    await ctx.send(embed=emb)


@bot.command()
async def hate(ctx):
    emb = discord.Embed(title='Оскорбляющие команды')
    emb.add_field(name='kill'.format(bot), value='Убить кого-то')
    emb.add_field(name='sex'.format(bot), value='Трахнуть кого-то')
    emb.add_field(name='spit'.format(bot), value='Плюнуть в дебильчика')
    await ctx.send(embed=emb)


@bot.command()
async def say(ctx, *arg):
    await ctx.message.delete()
    author = ctx.message.author
    msg = ctx.message.content
    print(author, msg)
    if ctx.message.role_mentions or ctx.message.mention_everyone:
        await ctx.send(author.mention + ", ты думаешь масспинг хорошая идея?")
    else:
        await ctx.send(' '.join(arg))

@bot.command()
async def allah(ctx):
    await  ctx.message.delete()
    await ctx.send("{} помолился аллаху 🙏".format(ctx.message.author.mention))


@bot.command()
async def pohyu(ctx):
    await  ctx.message.delete()
    await ctx.send("{} вообще похуй".format(ctx.message.author.mention))
    await ctx.send("https://www.youtube.com/watch?v=jbvYDqy2oO0")


@bot.group(invoke_without_command=True)
async def help(ctx):
    emb = discord.Embed(title='Навигация по командам')
    emb.add_field(name='rpassword'.format(bot), value='Случайный пароль')
    emb.add_field(name='say'.format(bot), value='Бот говорит за вас')
    emb.add_field(name='pohyu'.format(bot), value='Сказать что тебе похуй')
    emb.add_field(name='cry'.format(bot), value='Поплакать')
    emb.add_field(name='buisnes'.format(bot), value='Мы открываем бизнес')
    emb.add_field(name='help islam'.format(bot), value='Показать команды связаные с исламом')
    emb.add_field(name='help hate'.format(bot), value='Показать команды связаные с оскорблениями')
    emb.add_field(name='help rg'.format(bot), value='Показать команды связаные с рофло-играми')
    await ctx.send(embed=emb)


@help.command()
async def rg(ctx):
    emb = discord.Embed(title='Рофло-Игры')
    emb.add_field(name='gay game'.format(bot), value='Запустить тест на гея!')
    await ctx.send(embed=emb)


@help.command()
async def islam(ctx):
    emb = discord.Embed(title='Ислам команды')
    emb.add_field(name='allah'.format(bot), value='Помолиться аллаху')
    emb.add_field(name='plsallah'.format(bot), value='Попросить Аллаха воскресить тебя')
    emb.add_field(name='namaz'.format(bot), value='Сделать намаз')
    emb.add_field(name='terrorist'.format(bot), value='Объявить джихад')
    emb.add_field(name='thxallah'.format(bot), value='Поблагодарить аллаха')
    await ctx.send(embed=emb)


@help.command()
async def hate(ctx):
    emb = discord.Embed(title='Оскорбляющие команды')
    emb.add_field(name='kill'.format(bot), value='Убить кого-то')
    emb.add_field(name='sex'.format(bot), value='Трахнуть кого-то')
    emb.add_field(name='spit'.format(bot), value='Плюнуть в дебильчика')
    await ctx.send(embed=emb)

bot.run(os.environ['TOKEN'])
