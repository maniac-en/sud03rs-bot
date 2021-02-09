###########
# Imports #
###########

from discord.ext import commands

############
# COG Body #
############

class Ping(commands.Cog, name='ping command'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Sends a ping request to the bot.")
    async def ping(self, ctx):

        # Send an intial calculating ping message
        msg_ping = await ctx.send('Ping: Calulating...')

        # We round up the latency for a cleaner output.
        ping = round(self.bot.latency * 100, 3)

        # Instead of sending a new msg, we edit the previous one.
        await msg_ping.edit(content = f'Ping: {ping}ms')

def setup(bot):
    bot.add_cog(Ping(bot))
