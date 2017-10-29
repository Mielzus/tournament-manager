import logging

import discord
from discord.ext import commands

from secrets import discord_token

description = '''Tournament Manager is a bot to track video game tournaments hosted on a user's Discord server'''

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

bot = commands.Bot(command_prefix='!', descrption=description)

formats = {
    'swiss': 'Swiss',
    'round_robin': 'Round Robin',
    'single_elimination': 'Single Elimination'
}


@bot.event
async def on_ready():
    logger.info('-----------------------------')
    logger.info('Logged in as {0.name}'.format(bot.user))
    logger.info('ID {0.id}'.format(bot.user))
    invite_link = 'Invite to your server: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'
    logger.info(invite_link.format(bot.user.id))
    logger.info('-----------------------------')


@bot.command()
async def create(style: str, size: int):
    """
    Creates a new tournament with the specified number of players

    Currently supported formats:

    In development:
    Swiss (swiss) - https://en.wikipedia.org/wiki/Swiss-system_tournament
    Round Robin (round_robin) - https://en.wikipedia.org/wiki/Round-robin_tournament
    Single Elimination (single_elimination) - https://en.wikipedia.org/wiki/Single-elimination_tournament
    Double Elimination (double_elimination) - https://en.wikipedia.org/wiki/Double-elimination_tournament
    """

    await bot.say('Creating a new {0} style tournament with {1} players'.format(style, size))
    if style in formats:
        await bot.say('Creating a new {0} tournament'.format(formats.get(style)))
    else:
        await bot.say('Unrecognized tournament format {0}. Use !help create to see supported formats.'.format(style))
        return
    await bot.say('New {0} tournament created. Add players with the ID {1}'.format(style, '238'))


@bot.command()
async def add(player: discord.Member, match: str):
    """
    Adds a discord member to a tournament with the given id

    To get a the id and description of a tournament use the view command
    """
    print(player.name)
    print(player.bot)
    print(player.discriminator)
    print(player.id)
    print(player)
    await bot.say('Adding {0} to tournament {1}'.format(player.name, match))


@bot.command()
async def view():
    """
    Lists all currently active tournaments
    """
    await bot.say('There are no active tournaments')


@bot.command()
async def start(match : str):
    """
    Generates initial matchups for a tournament
    """
    bot.say('Generating matchups for {0}'.format(match))


@bot.command()
async def advance(match : str):
    """
    Generates matchups for the next round of a tournament
    """
    bot.say('Generating matchups for {0}'.format(match))


bot.run(discord_token)
