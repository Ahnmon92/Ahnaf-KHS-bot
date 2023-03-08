import discord, random
from discord.ext import commands

from keep_alive import keep_alive

TOKEN = "MTA3OTg5NTUwODU4MTA5MzQ1Nw.GdkVQX.fdm7kFWoY6c9DVh3gRnBCsoklvSmVcQHwvGExc"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)
#STREAMING
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name='Bacon puts soda in an oven then explodes', url='https://www.youtube.com/watch?v=aqBjQWut8Jw'))

#HELP COMMAND
@bot.command(name = "cmds")
async def cmds(ctx):
  embed = discord.Embed(
    colour = discord.Colour.red(),
    description = "Prefix = $\nCommands:\n\nrps [option] = rock paper scissors game\n\nroll [number] = roll dice [number of times]\n\nask = ask bot questions **finish with '?'\n\nimg [name] = Send's a picture of the select person\n\nrandimg = sends random image bot has\n\n das = OG command for the people\n\nchad = chad meter, tells you how chad you are",
    title = "Ahnaf Monirul Discord Bot"
    
  )
  await ctx.send(embed = embed)
#ROLL DICE
@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1, 6)
    await ctx.channel.send(f"You got... {d}!")
@bot.command(name = "ask")  
async def ask(ctx, *words):
  st= ""
  for word in words:
    st+= word
  if st.endswith("?"):
    reply = "I don't know the answer to that yet"
    await ctx.channel.send(reply)
  else:
    await ctx.channel.send("That is not a question")

#ROCK PAPER SCISSORS
@bot.command(name = "rps")
async def rps(ctx, user: str):
    comp_choice = ['rock', 'paper', 'scissors']
    computer = random.choice(comp_choice)
    if user not in comp_choice:
        await ctx.channel.send(f'That is not an option. Please choose from: {comp_choice}')
    else:
        if user == computer:
            await ctx.channel.send(f"You chose **{user}** and I chose **{computer}**, it's a draw!")
        elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            await ctx.channel.send(f"You chose **{user}** and I chose **{computer}**, You win!")
        else:
            await ctx.channel.send(f"You chose **{user}** and I chose **{computer}**, I win!")

#GIF
@bot.command(name = "gif")    
async def gif(ctx, category: str):
  cat = ["https://imgur.com/t/cat_gifs/fraQQDl", "https://imgur.com/t/cat_gifs/aeLG2", "https://imgur.com/t/cat_gifs/pSbwM5x"]
  catimg = random.choice(cat)

  dog = ["https://imgur.com/t/dog_gif/1EYVlub", "https://imgur.com/t/dog_gif/WbNVTM1", "https://imgur.com/t/dog_gif/J8I3Dga"]
  dogimg = random.choice(dog)
  
  if category == "cat":
    await ctx.channel.send(catimg)
  if category == "dog":
    await ctx.channel.send(dogimg)

#AVATAR
@bot.command(name = "avatar")
async def avatar(ctx, member: discord.Member = None):
  if member == None:
    member = ctx.author
  embed = discord.Embed(title = member, colour = discord.Colour.red()).set_image(url = member.avatar.url)
  await ctx.send(embed = embed)
#IMAGES
@bot.command(name = "shame")
async def image(ctx):
  await ctx.send("https://imgur.com/TMJtWdO")
@bot.command(name = "img")
async def img(ctx, name: str):
  if "luke" == name:
    await ctx.send("https://imgur.com/xr19Zdm")
  if "mrigank" == name:
    await ctx.send("https://imgur.com/OUAgQ0f")
  if "nic" == name:
    await ctx.send("https://imgur.com/pr2MXYO")
  if "ian" == name:
    await ctx.send("https://imgur.com/SaXjxeP")
  if "ali" == name:
    await ctx.send("https://imgur.com/GwBwzds")
  if "ahnaf" == name:
    await ctx.send("https://imgur.com/91hO7A4")
    
    

@bot.command(name = "randimg")
async def image(ctx):
  img_list = ["https://imgur.com/xr19Zdm", "https://imgur.com/OUAgQ0f", "https://imgur.com/pr2MXYO", "https://imgur.com/SaXjxeP", "https://imgur.com/fyy0m18", "https://imgur.com/GwBwzds", "https://imgur.com/kTrhV5H", "https://imgur.com/91hO7A4"]
  rand_img = random.choice(img_list)
  await ctx.send(rand_img)

#CHAD METER
@bot.command(name = "chad")
async def chad(ctx):
  number = random.randint(0, 100)

  await ctx.send(f"You are {number}% chad")
  if number == 100:
    await ctx.send("https://imgur.com/M4HM7yQ")
  elif number >= 90:
    await ctx.send("https://imgur.com/FV4WUoX")
  elif number >= 80:
    await ctx.send("https://imgur.com/pSzKkWf")
  elif number >= 50:
    await ctx.send("https://imgur.com/MQsx3tC")
  else:
    await ctx.send("https://imgur.com/zJnvdUM")

@bot.command(name = "das")
async def das(ctx):
  await ctx.send("mrigank built like")
  await ctx.send("https://imgur.com/k30OiY7")
  
    
    

  
  




  

  
  
  
  
  

















keep_alive()

bot.run(TOKEN)