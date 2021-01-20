import discord
from discord.ext import commands
import logging
from colorama import Fore as color


def create_avatar_link(ctx, size):
    link = f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.png?size={size}"
    return link
