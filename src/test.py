import discord
from discord.ext import commands

TOKEN = "MTA5MzQ3NjU2ODMyOTg4MzcyOQ.Gfn6QJ.PDMGlZVKOXeBeTqwJFUyWiW3ypbGrPOsYgn7No"

#Intents
intents=discord.Intents.default()
intents.message_content = True

def main():
    
    #Bot Constructor
    bot = commands.Bot(command_prefix ='&', intents=intents)

    #On Launch
    @bot.event
    async def on_ready():
        print(f'Tick Tock.... Hi, I am {bot.user}')
    
    #Basic Hello!, Command using @bot.command. (time is the command, 
    #prefix not needed as already stated)
    @bot.command()
    async def time(ctx):
        await ctx.send('Hello!')

    #Running Bot
    bot.run(TOKEN)



if __name__ == "__main__":
    main()

