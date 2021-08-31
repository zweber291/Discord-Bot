import discord
import random
import json
import requests
from discord.ext import commands
from discord.utils import get

TOKEN = '' #Bot token goes here (redacted for privacy)

description = '''NNO Python Bot''' #Bot Name
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description = description, intents = intents) #Sets bot command prefix
bot.remove_command('help') #Disables default help command (new one below)

@bot.event
async def on_ready():
    #Sends login message to console
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #Changes name of the game the bot is 'playing'
    await bot.change_presence(activity=discord.Game(name='?help'))

#When a user reacts with a specific reaction, add specified role
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != 832694147390373928:
        return
    if payload.emoji.name == "clem":
        #print("Added user to warframe")
        role = get(payload.member.guild.roles, name='Warframe')
        await payload.member.add_roles(role)
    if payload.emoji.name == "creeper":
        #print("Added user to minecraft")
        role = get(payload.member.guild.roles, name='Minecraft')
        await payload.member.add_roles(role)
        
#Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please put all required arguments!")
   
#New help command
@bot.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(color = discord.Color.blue())
    embed.set_author(name='Help')
    
    embed.add_field(name = '?help', value = 'Messages you this menu.', inline = False)
    embed.add_field(name = '?ip', value = 'Says the IP of our Minecraft server.', inline = False)
    embed.add_field(name = '?facebook', value = 'Says the link of our Facebook page.', inline = False)
    embed.add_field(name = '?twitter', value = 'Says the link of our Twitter page.', inline = False)
    embed.add_field(name = '?steam', value = 'Says the link of our Steam group.', inline = False)
    embed.add_field(name = '?destiny', value = 'Says the link of our Destiny 2 clan.', inline = False)
    embed.add_field(name = '?pacer', value = 'The FitnessGram Pacer Test.', inline = False)
    embed.add_field(name = '?nou', value = 'A good way to tell someone "No u".', inline = False)
    embed.add_field(name = '?potofgreed', value = 'Play the card Pot of Greed.', inline = False)
    embed.add_field(name = '?catfact', value = 'Says a random cat fact.', inline = False)
    embed.add_field(name = '?dadjoke', value = 'Says a random dad joke.', inline = False)
    embed.add_field(name = '?dice <number of sides>', value = 'Rolls a dice with the number of sides you specify.', inline = False)
    embed.add_field(name = '?shop', value = 'Displays the shop.', inline = False)
    embed.add_field(name = '?buy <item>', value = 'Buy an item from the shop.', inline = False)
    embed.add_field(name = '?balance', value = 'Displays your current balance.', inline = False)
    embed.add_field(name = '?leaderboard', value = 'Displays money leaderboard.', inline = False)
    embed.add_field(name = '?rps <selection>', value = 'Play rock paper scissors with the bot.', inline = False)
    embed.add_field(name = '?doggo', value = 'Gets a random dog image.', inline = False)
    
    await ctx.author.send(embed=embed)
    await ctx.author.send('If you have any questions, ask smack17!')

#Sends MC Server IP
@bot.command()
async def ip(ctx):
    await ctx.send("Minecraft Server IP: SERVER NAME HERE")
    
#Sends Facebook page link
@bot.command()
async def facebook(ctx):
    await ctx.send("Facebook page: FACEBOOK PAGE HERE")
    
#Sends Twitter page link
@bot.command()
async def twitter(ctx):
    await ctx.send("Twitter page: TWITTER PAGE HERE")
    
#Sends Steam group link
@bot.command()
async def steam(ctx):
    await ctx.send("Steam group: STEAM LINK HERE")
    
#Sends Destiny 2 clan link
@bot.command()
async def destiny(ctx):
    await ctx.send("Destiny 2 clan: DESTINY 2 LINK HERE")
    
#Fitnessgram Pacer Test
@bot.command()
async def pacer(ctx):
    await ctx.send("The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. beep A single lap should be completed each time you hear this sound. ding Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")

#Sends an uno reverse card
@bot.command()
async def nou(ctx):
    color = pick_color(random.randint(1,5)) #Picks color of card
    await ctx.send(color)
    
    
#Plays the card Pot of Greed, which allows you to draw 2 cards and put them in your hand
@bot.command()
async def potofgreed(ctx):
    await ctx.send("I play the magic card Pot of Greed, which allows me to draw 2 cards and put them in my hand!")
    await ctx.send("https://images-na.ssl-images-amazon.com/images/I/51uITWtTYFL._AC_.jpg")
    
    
#Picks color of uno reverse card
def pick_color(argument):
    switcher = {
        1: 'https://i.imgur.com/yXEiYQ4.png',
        2: 'https://i.imgur.com/CSuB3ZW.png',
        3: 'https://i.imgur.com/3WDcYbV.png',
        4: 'https://i.imgur.com/IxDEdxW.png'
    }
    return switcher.get(argument, 'https://i.imgur.com/yXEiYQ4.png')

    
#Sends a random cat fact
@bot.command()
async def catfact(ctx):
    fact = requests.get('https://catfact.ninja/fact')
    await ctx.send(fact.json()['fact'])

#Sends a random dad joke
@bot.command()
async def dadjoke(ctx):
    joke = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    await ctx.send(joke.json()['joke'])

#Rolls a dice specified by command sender
@bot.command()
async def dice(ctx, sides : int):
    result = random.randint(1,sides) #Gets random number from 1 to sides specified
    await ctx.send("You rolled a " + str(result) + "!")

#Money shop (WIP)
# @bot.command()
# async def shop(ctx): #Displays shop items
#     embed = discord.Embed(color = discord.Color.blue())
#     embed.set_author(name='Shop (Note: All roles are purely cosmetic)')
#     embed.add_field(name = '?buy coolguy', value = 'Cost: 1000 | Changes your role to "Cool Guy".', inline = False)
#     embed.add_field(name = '?buy coolgal', value = 'Cost: 1000 | Changes your role to "Cool Gal".', inline = False)
#     embed.add_field(name = '?buy dankmemer', value = 'Cost: 3000 | Changes your role to "Dank Memer".', inline = False)
#     embed.add_field(name = '?buy moneybags', value = 'Cost: 10,000,000 | Changes your role to "Moneybags".', inline = False)
#     
#     await ctx.send(embed=embed)
# 
# #Buy command for shop items
# @bot.command(pass_context = True)
# async def buy(ctx, item):
#     with open('users.json', 'r') as f:
#         users = json.load(f)
#         
#     user = ctx.message.author
#     money = users[str(user.id)]['money']
#     
#     #Dictionary for items. Add stuff as needed.
#     shop_items = {'coolguy': {'name': 'Chill Squad',
#                               'price': 1000},
#                   'dankmemer': {'name': 'Dank Memer',
#                                 'price': 3000},
#                   'moneybags': {'name': 'Moneybags',
#                                 'price': 10000000}
#                   }
#     #Check if command argument is in the shop
#     if item in shop_items.keys():
#         #Check if sender has the amount of money
#         if money < shop_items[item]['price']:
#             await ctx.send('You cant afford this item!')
#         else:
#             role = discord.utils.get(user.guild.roles, name = shop_items[item]['name']) #Finds the role
#             #If user has the role
#             if role in user.roles:
#                 await ctx.send('You already have that role!')
#             #If they dont
#             else:
#                 await user.add_roles(role)
#                 users[str(user.id)]['money'] -= shop_items[item]['price']
#                 await ctx.send('You have purchased {}!'.format(shop_items[item]['name']))
#                 
#     #If the item isnt in the shop            
#     else:
#         await ctx.send('Item is not in shop!')
# 
#     with open('users.json', 'w') as f:
#         json.dump(users, f)

#Exp/Currency System
@bot.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member) #Adds user to json file when they join the server

    with open('users.json', 'w') as f:
        json.dump(users, f)

@bot.event #Adds exp to user and checks for level up when user sends message
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    #If message author isnt the bot
    if message.author != bot.user:
        #If message author in the database
        if str(message.author.id) in users:
            await add_experience(users, message.author, 5)
            await level_up(users, message.author, message.channel)
        else:
            await update_data(users, message.author)
            print("Adding user to json file")
            print(message.author.id)
        
        #Updates database with correct names
        if message.author.name != users[str(message.author.id)]['username']:
            users[str(message.author.id)]['username'] = message.author.name

    with open('users.json', 'w') as f:
        json.dump(users, f)
    
    #Lets normal messages be sent instead of read as commands by the bot
    await bot.process_commands(message)
        
#Updates JSON with new user
async def update_data(users, user):
    users[str(user.id)] = {}
    users[str(user.id)]['username'] = user.name
    users[str(user.id)]['experience'] = 0
    users[str(user.id)]['base_experience'] = 25
    users[str(user.id)]['level'] = 1
    users[str(user.id)]['money'] = 500
        
#Adds xp to users json entry
async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp
    
#Adds money to users json entry
async def add_money(users, user, money, ctx):
    users[str(user.id)]['money'] += money
    await ctx.send(str(money) + " has been added to " + user.name + "'s account.")

#Levels up user
async def level_up(users, user, ctx):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    experience_base = users[str(user.id)]['base_experience']
    lvl_end = int(lvl_start)
    
    if experience >= experience_base:
        users[str(user.id)]['base_experience'] += int(experience_base + lvl_start * lvl_start ** (1/3)) #Level formula
        lvl_end = int(lvl_start + 1)
    
    if lvl_start < lvl_end:
        await ctx.send('{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[str(user.id)]['level'] = lvl_end
        await add_money(users, user, lvl_end*100, ctx) #Gives 100*level up level in money

#Give Money
@bot.command(pass_context = True) #Need to pass context to get the arguments
@commands.is_owner() #Checks for bot owner
async def givemoney(ctx, username, money : int):
    with open('users.json', 'r') as f:
        users = json.load(f)
        
    user = discord.utils.get(ctx.message.author.guild.members, name = username) #Converts username argument into user object to find ID
    await add_money(users, user, money, ctx)
        
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Show balance
@bot.command(pass_context = True)
async def balance(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        
    user = ctx.message.author
    money = users[str(user.id)]['money']
    await ctx.send('{} has {} in their account.'.format(user.name, money))
    
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Level Leaderboard
@bot.command()
async def leaderboard(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    #Starts at 1st place
    i = 1
    board = []
    board_embed = discord.Embed(color = discord.Color.blue())
    board_embed.set_author(name='Level Leaderboard')
    
    for item in users:
        temp_name = users[item]['username']
        temp_score = users[item]['level']
        board.append((temp_name, temp_score))
    
    #Sorts the list to start in 1st place and goes to the last place
    board.sort(reverse=True)
    for n in board:
        board_embed.add_field(name = str(i), value = '{}: {}'.format(n[0], n[1]), inline = False)
        i += 1
        
    await ctx.send(embed = board_embed)

#Rock Paper Scissors
@bot.command(pass_context = True)
async def rps(ctx, move):
    cpu_result = cpu_move(random.randint(1,4))
    
    #Rock Results
    if move == 'rock':
        if cpu_result == 'Paper':
            await ctx.send("I play paper! You lose!")
        elif cpu_result == 'Scissors':
            await ctx.send("I play scissors! You win!")
        elif cpu_result == 'Rock':
            await ctx.send("I play rock! We tied!")
    
    #Paper results
    elif move == 'paper':
        if cpu_result == 'Paper':
            await ctx.send("I play paper! We tied!")
        elif cpu_result == 'Scissors':
            await ctx.send("I play scissors! You lose!")
        elif cpu_result == 'Rock':
            await ctx.send("I play rock! You win!")
    
    #Scissors results
    elif move == 'scissors':
        if cpu_result == 'Paper':
            await ctx.send("I play paper! You win!")
        elif cpu_result == 'Scissors':
            await ctx.send("I play scissors! We tied!")
        elif cpu_result == 'Rock':
            await ctx.send("I play rock! You lose!")
            
    #If input isnt rock paper or scissors
    else:
        ctx.send("Invalid input!")

#Gets bot rock paper scissors result
def cpu_move(argument):
    switcher = {
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors'
    }
    return switcher.get(argument)

#Random dog image
@bot.command()
async def doggo(ctx):
    dog_json = requests.get('https://random.dog/woof.json').json()
    url = dog_json['url']
    await ctx.send(url)

#Shuts down bot
@bot.command()
@commands.is_owner() #Checks for bot owner
async def shutdown(ctx):
    await ctx.bot.close()
    
#Run the bot
bot.run(TOKEN)
