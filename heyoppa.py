from discord.ext import commands
from discord.ext.commands import Bot
from boto.s3.connection import S3Connection
import asyncio
import discord
import os
import datetime

bot = commands.Bot(command_prefix="!")

icon = "https://cdn.pbrd.co/images/HvZ0h0T.png"
hiimage = "http://logoonline.mtvnimages.com/uri/mgid:file:http:shared:s3.amazonaws.com/articles.newnownext.com-production/wp-content/uploads/2017/03/2my81uh-1490061002.gif"
byeimage = "https://metrouk2.files.wordpress.com/2018/03/rpdr_fi0.gif"
channel = None

@bot.event
async def on_ready():
	print("Bot is ready to go")
	channel = bot.get_channel(384395211771478026)
	await bot.change_presence(activity=discord.Game(name="play.lgbtrealms.com"))


@bot.event
async def on_member_join(member):
	print("Member Joined")
	channel = bot.get_channel(384395211771478026)
	userIcon = (member).avatar_url
	joinembed = discord.Embed(title=None, description=None, color=0x00FFFF)
	joinembed.set_author(name="LGBTPlus", icon_url=icon)
	joinembed.add_field(name="Welcome {} to LGBT Realms!".format(member), value="Make sure to read our Rules in #Welcome", inline=False)
	joinembed.add_field(name="Join us in game: play.lgbtrealms.com", value=" Remember, always be yourself!", inline=False)
	joinembed.set_thumbnail(url=userIcon)
	joinembed.set_image(url=hiimage)
	joinembed.set_footer(text="{} joined at {:%Y-%m-%d %H:%M:%S}".format(member, datetime.datetime.today()), icon_url=icon)
	await channel.send(embed=joinembed)

@bot.event	
async def on_member_remove(member):
	print("Member Left")
	channel = bot.get_channel(384395211771478026)
	userIcon = (member).avatar_url
	joinembed = discord.Embed(title=None, description=None, color=0xFF0000)
	joinembed.set_author(name="LGBTPlus", icon_url=icon)
	joinembed.add_field(name="Goodbye {}, Sashay Away!".format(member), value="See you on the other side, the rainbow side!", inline=False)
	joinembed.set_thumbnail(url=userIcon)
	joinembed.set_image(url=byeimage)
	joinembed.set_footer(text="www.lgbtrealms.com | Goodbye {}".format(member), icon_url=icon)
	await channel.send(embed=joinembed)

@bot.command(pass_context=True)
async def status(ctx, *, msg: str):
    owner = discord.utils.get(ctx.message.guild.roles, name="Owner")
    admin = discord.utils.get(ctx.message.guild.roles, name="Admin")
    if owner in ctx.author.roles or admin in ctx.author.roles:
        await ctx.message.delete()
        msgoptions = msg.split("|")
        embed = discord.Embed(title=None, description=None, color=0xFFD700)
        embed.add_field(name=msgoptions[0], value=msgoptions[1], inline=False)
        await ctx.send(embed=embed)
        print("Status {}, {} Added".format(msgoptions[0], msgoptions[1]))

bot.run(os.environ['token'])