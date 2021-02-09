###########
# Imports #
###########

from discord.ext import commands

############
# COG Body #
############

help_msg = """
```md
# N/A
```
"""

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[''])
    async def help(self, ctx, *, args = None):
        await ctx.send(help_msg)

def setup(bot):
    bot.add_cog(Help(bot))
