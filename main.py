import os
import discord, random
from discord.ext import commands

from keep_alive import keep_alive

my_secret = os.environ['TOKEN']


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents) #Assigns bot command prefix
#STREAMING
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name='Bacon puts soda in an oven then explodes', url='https://www.youtube.com/watch?v=aqBjQWut8Jw')) #Changes bot activity to streaming and shows what it's streaming

#HELP COMMAND
@bot.command(name = "cmds")
async def cmds(ctx):
  embed = discord.Embed(
    colour = discord.Colour.red(),
    description = "Prefix = $\nCommands:\n\nrps [option] = rock paper scissors game\n\nroll [number] = roll dice [number of times]\n\nask = ask bot questions\n\nimg [name] = Send's a picture of the select person\n\nrandimg = sends random image bot has\n\n das = OG command for the people\n\nchad = chad meter, tells you how chad you are\n\nguess = play a number guessing game\n\ngif [option] = sends a random gif of selected category **currently only cat and dog**",
    title = "Ahnaf Monirul Discord Bot"
    
  ) #Embeded message containing bot commands
  await ctx.send(embed = embed)
#ROLL DICE
@bot.command(name = "roll")
async def roll(ctx,num): #Generates random number from 1 - 6
  for i in range(int(num)): #Rolls amount dependant on user input
    d = random.randint(1, 6)
    await ctx.channel.send(f"You got... {d}!")
#ASK COMMAND
@bot.command(name = "ask")  
async def ask(ctx, *words):
  ans = ["Yes", "No", "Maybe"]
  st= ""
  for word in words:
    st+= word
  if st.startswith("is") or st.startswith("am") or st.startswith("will"): #Question has to start with "is", "am" or "will"
    reply = random.choice(ans)
    await ctx.channel.send(reply)
  else:
    await ctx.channel.send("That's not a question I can answer yet")    
#ROCK PAPER SCISSORS
@bot.command(name = "rps")
async def rps(ctx): #Converts user input into string
    comp_choice = ['rock', 'paper', 'scissors']
    computer = random.choice(comp_choice) #Takes random choice from list
    await ctx.send("Pick an option between Rock, Paper and Scissors")
  
    def check(m):
      return m.author == ctx.author and m.channel == ctx.message.channel #Checks if message is sent by same person who called command
    
    user = await bot.wait_for("message", check=check)

    if user.content == computer:
      await ctx.channel.send(f"I chose **{computer}**, it's a draw!")
    
    elif (user.content == 'rock' and computer == 'scissors') or (user.content == 'paper' and computer == 'rock') or (user.content == 'scissors' and computer == 'paper'):
      await ctx.channel.send(f"I chose **{computer}**, You win!")
        
    elif (user.content == 'rock' and computer == 'paper') or (user.content == 'paper' and computer == 'scissors') or (user.content == 'scissors' and computer == 'rock'):
      await ctx.send(f"I chose **{computer}**, I win")
          
    else:
      await ctx.channel.send(f"That is not an option. Please choose from: {comp_choice}") #If user option isn't it lists it sends this message    
#GIF
@bot.command(name = "gif")    
async def gif(ctx, category: str): #Converts user input into string
  cat = ["https://imgur.com/t/cat_gifs/fraQQDl", "https://imgur.com/t/cat_gifs/pSbwM5x"]
  catimg = random.choice(cat) #Random choice from list

  dog = ["https://imgur.com/t/dog_gif/1EYVlub", "https://imgur.com/t/dog_gif/WbNVTM1", "https://imgur.com/t/dog_gif/J8I3Dga"]
  dogimg = random.choice(dog) #Random choice from list
  
  if category == "cat":
    await ctx.channel.send(catimg) 
  if category == "dog":
    await ctx.channel.send(dogimg)

@bot.command(name = "who")
async def gif(ctx):
  await ctx.send("https://imgur.com/iLDcMmi")
#AVATAR
@bot.command(name = "avatar")
async def avatar(ctx, member: discord.Member = None):
  if member == None: #If no member is mentioned it takes the avatar of the person who sent it
    member = ctx.author
  embed = discord.Embed(title = member, colour = discord.Colour.red()).set_image(url = member.avatar.url) #Creates embed and assigns what each part will be, adds colour as well
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
#MRIGANK COMMAND
@bot.command(name = "das")
async def das(ctx):
  await ctx.send("mrigank built like")
  await ctx.send("https://imgur.com/k30OiY7")
#CALCULATOR
@bot.command(name = "cal")
async def cal(ctx, num1: float, sign: str, num2: float):
    if sign == "+":
        ans = num1 + num2
    elif sign == "-":
        ans = num1 - num2
    elif sign == "*":
        ans = num1 * num2
    elif sign == "/":
        ans = num1 / num2
    else:
        await ctx.send("That is not a valid equation, please enter 2 numbers in the format:\n**[num1] [sign] [num2]**")
        return
    await ctx.send(f"{num1} {sign} {num2} = {ans}")
  
#GUESSING GAME
@bot.command(name = "guess")
async def guess(ctx):
  rand_num = random.randint(0, 100)
  await ctx.send("The game has started, guess the correct number from 0 - 100 to win!")
  def check(m):
    return m.author == ctx.author and m.channel == ctx.message.channel #Checks if message is sent by same person who called command
  while True:
    guess = await bot.wait_for('message', check=check)

    if not guess.content.isdigit(): #If input isn't a a number, ask question
      await ctx.send("That is not a number, please **enter a number**")
      continue
    
    guess2 = int(guess.content)
    if guess2 == rand_num:
      await ctx.send(f"You guessed {rand_num} which is the correct number!")
      return
    elif guess2 >= rand_num:
      await ctx.send("Lower")
    elif guess2 <= rand_num:
      await ctx.send("Higher")



keep_alive()

bot.run(my_secret)