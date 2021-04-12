# Creating cogs
cogs are the most important piece of this bot, as they hold the commands that your users will use. Please use this readme to understand how to add a new cog into your code.
## Creating the file for your cog
1. create a new python file in application/cogs with a simple name. (userModeration.py for example)
2. paste the below snippet of code into the new file

    ```py import discord
    from discord.ext import commands

    class className(commands.Cog):

        def __init__(self, bot):
            self.bot = bot

    def setup(bot):
        bot.add_cog(className(bot))
    ```
    make sure to replace `className` with the name of your cog (this can be the name of your python file, if you want).
## Adding commands to your cog
Now that your file is created, it is time to add a command!
Inside your new class, under the `__init__` method, add this code snippet, replacing "command_name" with your command name (duh):
```py
@commands.command()
async def command_name(self, ctx):
    # place command stuff here!
```
- as you can see here, the difference between this code snippet and a regular discord.py command is that we pass `self` in as a parameter. this is because our methods are now in a class!
- to make the bot process information here (such as `bot.get_channel()`) you must prefix this with `self`:
    - `self.bot.get_channel()`
