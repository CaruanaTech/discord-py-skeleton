import json
import sys
from colorama import Fore as color, init
import logging
import discord
import os
from discord.ext import commands

# initialise colorama
init()

# set up logging
logging.basicConfig(filename="logs.log",
                    filemode="w",
                    format="[ %(asctime)s ] %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(logging.Formatter("[ %(asctime)s ] %(message)s", "%m/%d/%Y %I:%M:%S %p"))
logging.getLogger('').addHandler(console)

# load config
try:
    with open('config.json') as json_file:
        config = json.load(json_file)

except Exception as e:
    logging.warning(color.RED +
                    "unable to open config.json - please check it is in the root directory" +
                    color.RESET)
    logging.warning(color.RED + str(e) + color.RESET)
    sys.exit(1)

if "PREFIX" in config:
    bot = commands.Bot(command_prefix=config["PREFIX"])

else:
    logging.warning(color.RED +
                    "prefix value not found in config.json" +
                    color.RESET)
    sys.exit(1)


def start_bot():
    # initialise discord bot
    if "PREFIX" not in config or config["PREFIX"] == "":
        logging.warning(color.RED +
                        "prefix value not set, please check your config file" +
                        color.RESET)
        sys.exit(1)

    elif "TOKEN" not in config or config["TOKEN"] == "":
        logging.warning(color.RED +
                        "Unable to locate bot token, check your config.json" +
                        color.RESET)
        sys.exit(1)

    else:
        try:
            bot.run(config["TOKEN"])
        except Exception as e:
            logging.warning(color.RED +
                            "unable to start up bot, check error below:" +
                            color.RESET)
            logging.warning(color.RED + str(e) + color.RESET)


# load cogs
active_cogs = 0
logging.warning(color.CYAN +
                "Attempting to load cogs" +
                color.RESET)

for filename in os.listdir("./application/cogs"):
    if filename.endswith(".py"):
        cog_name = filename[:-3]
        bot.load_extension(f"application.cogs.{cog_name}")
        logging.warning(color.LIGHTBLUE_EX + f"loaded '{cog_name}'" + color.RESET)
        active_cogs += 1

if active_cogs < 1:
    logging.warning(color.RED +
                    "No cogs have been found in /application/cogs, quitting program." +
                    color.RESET)
    sys.exit(1)

else:
    start_bot()
