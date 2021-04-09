import discord
import logging
import time
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="/")
token = input()


@bot.event
async def on_ready():
    print(f"[系統]　openBot 已套用至使用者 {bot.user}")
    print("[系統]　openBot 已啟動")


def logger():
    localtime = time.strftime("%Y%m%d%I%M%S", time.localtime())

    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename=f"./Data/Logs/{localtime}.txt", encoding="utf-8", mode="w")
    handler.setFormatter(logging.Formatter(
        "%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
    logger.addHandler(handler)


def main():
    print("[系統]　正在啟動 openBot")
    logger()

    for theclass in os.listdir("./Code"):
        if theclass.endswith(".py"):
            bot.load_extension(f"Code.{theclass[:-3]}")

    bot.run(token)


if __name__ == "__main__":
    main()
