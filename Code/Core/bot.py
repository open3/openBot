import discord
from discord.ext import commands


class BotAPI:

    def __init__(self):
        pass

    def get_embed(self, ctx, text, icon_url, color, hiddenfoot=False):
        embed = discord.Embed(color=color)
        embed.set_author(name=text, icon_url=icon_url)
        if hiddenfoot is not True:
            embed.set_footer(text=f"本指令由 {str(ctx.author)[:5]} 使用")

        return embed

    def get_botinfo(self):
        pass


class Cog_Template(commands.Cog, BotAPI):

    def __init__(self, bot):
        super().__init__()

        self.bot = bot


def main():
    print("你無法執行 bot.py，因為該檔案是作為模組使用。")


if __name__ == "__main__":
    main()
