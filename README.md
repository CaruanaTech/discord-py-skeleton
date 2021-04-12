# discord-py-skeleton
A discord.py skeleton repository for making python discord bots. 

## Features
Basic features such as
- "rich" coloured logging
- cogs

are currently implemented. I plan to expand this but not by too much as it is a skleton bot for users to add upon based on their needs (I will not be adding )

## How to install
I am under the assumption you have your bot's token at hand and have already created a bot (without all the code).
 1. To get started,install all of the requirementss fot this bot to run.
    - `pip install -r requirements.txt`.
    - this can be in a virtual environment or your default python interpreter, up to you!
2. enter any code you want (familiarise yourself with the README in /application/cogs to make commands and cogs)
3. enter your discord bot token into the `config.json` file, along with your desired prefix
4. enter the root directory in your command prompt and type `python3 bot.py`

note: if your config isnt set correctly then the bot will not run. make sure that you have followed the steps correctly.

## Common methods file
this file is for storing all of the methods that are called frequently within your code, some examples being:
- input validation/sanitisation
- data manipulation
- etc

## Logging
This code uses `colorama` and `logging` to make your bot's code output clean. here is a below snippet of how to log *stuff*:
- input:
   ```py
   logging.warning(color.RED + "text goes here" + color.RESET)```
- output:

   `[DD/MM/YY HH:MM:SS AM/PM] text goes here`

to look at what colors are available for logging check the [colorama docs](https://pypi.org/project/colorama/) 