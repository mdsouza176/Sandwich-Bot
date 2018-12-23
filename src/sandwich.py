import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio

#These two lines of code below create acces to the bot
#and the client on discord
Client = discord.Client()
bot = commands.Bot(command_prefix= '!')

breadlist = {
    1:"Italian",
    2:"French",
    3:"Whole-Wheat"
}
cheeseList = {
    1: "Mozzarella",
    2:"American Cheese",
    3:"Cheddar"
}
meatList = {
    1:"Turkey",
    2:"Salami",
    3: "Roast Beef",
    4: "bacon"
}
#Nice helper function to return different dictionary
#values in ordered list form
def get_Options_In_List(dictionary):
    i =1
    list = ""
    while i <= len(dictionary):
        option = dictionary.get(i)
        list += str(i) + ". " + str(option) + "\n"
        i += 1
    return list


#premptive measure to tell when the program has connected to discord and
#the bot is therfore up are running.
@bot.event
async def on_ready():
    print("Bot is Ready!")

#TODO- Add more parses and perhaps filtering of bad words
@bot.event
async def on_message(message):
    await bot.process_commands(message)

#helper function to check if the type of bread user picked is in the breadList
def valid_option(choice, dictionary):
    try:
        if int(choice) in dictionary.keys():
            return True
    except ValueError:
        return False
    return False

#main Function which runs CoolBots main skill, making a sandwhich

@bot.command()
async  def sub():
    ask = "Hello, this is sandwich, please enter the type of bread you'd like: \n"
    ask += get_Options_In_List(breadlist)
    await bot.say(ask)
    sandwhich = "Your Sandwich: "
    result = await bot.wait_for_message(10)
    isValid = False
    if result:
            if valid_option(result.content, breadlist):
                sandwhich += "Bread: " + breadlist[int(result.content)] + " "
                isValid = True
            else:
                if not(result.content == "!sub"):
                    await bot.say("Not Valid Option")
    if isValid:
        isValid = False
        ask = "Pick what cheese you would like to go with the bread: \n"
        ask += get_Options_In_List(cheeseList)
        await  bot.say(ask)
        result = await bot.wait_for_message(10)
        if result:
            if valid_option(result.content, cheeseList):
                sandwhich += "Cheese: " + cheeseList[int(result.content)] + " "
                isValid = True
            else:
                if not(result.content == "!sub"):
                    await bot.say("Not Valid Option")
    if isValid:
        isValid = False
        ask = "Pick what meat you would like: \n"
        ask += get_Options_In_List(meatList)
        await  bot.say(ask)
        result = await bot.wait_for_message(10)
        if result:
            if valid_option(result.content, meatList):
                sandwhich += "Meat: " + meatList[int(result.content)]
                await bot.say(sandwhich)
                isValid = True
            else:
                if not(result.content == "!sub"):
                    await bot.say("Not Valid Option")
bot.run("TOKEN")


