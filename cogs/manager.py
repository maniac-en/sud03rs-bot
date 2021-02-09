###########
# Imports #
###########

import discord
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure

############
# COG Body #
############

class Manager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        #  if isinstance(error, CheckFailure):
        #      if ctx.message.author.guild_permissions.administrator:
        #          await ctx.send('Don\'t mis-use your power')
        #      else:
        #          await ctx.send("That's not allowed")


        ignored = (commands.CommandNotFound, commands.MissingRequiredArgument, )
        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return

    @commands.command()
    async def load(self, ctx, extension):
        print(f'Loading cogs.{extension}...')
        try:
            self.bot.load_extension(f'cogs.{extension}')
            print(f'\tcogs.{extension} loaded successfully')
        except commands.ExtensionError as e:
            print(f'\tAn error occurred while loading cogs.{extension}\n\tReason:\n\t{e}')

    @commands.command()
    async def unload(self, ctx, extension):
        print(f'Unloading cogs.{extension}...')
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            print(f'\tcogs.{extension} unloaded successfully')
        except commands.ExtensionError as e:
            print(f'\tAn error occurred while unloading cogs.{extension}\n\tReason:\n\t{e}')

    @commands.command()
    async def reload(self, ctx, extension):
        print(f'Reloading cogs.{extension}')
        try:
            self.bot.reload_extension(f'cogs.{extension}')
            print(f'\tcogs.{extension} reloaded successfully')
        except commands.ExtensionError as e:
            print(f'\tAn error occurred while unloading cogs.{extension}\n\tReason:\n\t{e}')

def setup(bot):
    bot.add_cog(Manager(bot))
