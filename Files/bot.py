import os
import discord
from discord.ext import commands
from content import *
import random
# Send messages

with open('.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value



def run_discord_bot():
  index = 2
  print(jokes[index])
  client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

  @client.event
  async def on_ready():
    print(f'{client.user} is now running!')
  @client.event
  async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')
    await welcome_channel.send(f'Welcome to the server, {member.mention}!')
  @client.command()
  async def randomjoke(ctx):
    mess_channel = ctx.message.channel
    index = random.randint(0, 39)
    text = jokes[index]
    embed = discord.Embed(
        title = "Here is a Random Joke",
        description = text,
        colour = discord.colour.from_rgb(99, 224, 159)
      )
    embed.set_footer(text = "Hope you enjoyed the joke")
    await ctx.send(mess_channel, embed=embed)
  @client.event
  async def on_message(message):
    if message.content.lower() == "hello":
      message.channel.send("Hey There")
    if message.content.lower() == "roll":
      message.channel.send(f"{random.randint(1, 6)}")
    if message.content.lower() == "help":
      message.channel.send("You can go to the github page for help")
    if message.content.lower() == "ban me":
      message.channel.send("Sorry I can only do it if the server owners tell me to")
    if message.content.lower() == "hey there":
      message.channel.send("Hello")
    if message.content.lower() == "gg":
      message.channel.send("Keep Up, appreciate people more")
    if message.content.lower() == "hi":
      message.channel.send("Hey There")
    if message.content.lower() == "!rules":
      message.channel.send("The Format should be like !rules <SERVER NAME>")
    if message.content.startswith('!membercount'):
      guild = message.guild
      member_count = len(guild.members)
      await message.channel.send(f"There are {member_count} members in this server.")
    if message.content.startswith('!ban'):
      roles = message.author.roles
      user = message.mentions[0]
      for role in roles:
        if role.name == 'Moderator':
          user_to_ban = message.mentions[0]
          await message.guild.ban(user_to_ban)
          await message.channel.send(f'{user_to_ban.name} was banished!')
    if message.content.startswith('!kick'):
      roles1 = message.author.roles
      for role in roles1:
        if role.name == 'Moderator':
          user_to_kick = message.mentions[0]
          await message.guild.kick(user_to_kick)
          await message.channel.send(f'{user_to_kick.name} was kicked!')
    # Make sure bot doesn't get stuck in an infinite loop
    if message.author == client.user:
      return

  # Remember to run your bot with your personal TOKEN
  client.run(os.environ[key])
