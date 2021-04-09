import discord
from discord.ext import commands
from Code.Core.bot import Cog_Template, BotAPI
from random import randint


class Commands(Cog_Template):

    @commands.command()
    async def ping(self, ctx, mode=None):
        colors = [0xf05030, 0xffaa00, 0x3df584]
        if mode is None:
            embed = self.get_embed(ctx, f"延遲時間：{round((self.bot.latency * 1000), 2)} 毫秒(ms)",
                                   "https://tinyurl.com/7ndn3pbh", colors[len(str(int(self.bot.latency * 1000))) - 2])
        else:
            embed=self.get_embed(ctx, "Pong!", "", 0x3939ff, True)
        await ctx.send(embed = embed)

    @commands.command()
    async def dice(self, ctx, times=1):
        """
        缺少圖片
        """

        while (times <= 0):
            num = randint(1, 6)
            await ctx.send(embed=self.get_embed(ctx, f"你骰出了 {num}", "", 0xeb4034))
            times -= 1

            # https://raw.githubusercontent.com/open3/openBot/master/res/dice{num}.png


def setup(bot):
    bot.add_cog(Commands(bot))


def main():
    pass


if __name__ == "__main__":
    main()
