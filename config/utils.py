#!/usr/bin/env python3
from discord.utils import get
import aiohttp

def sanitize_check(data, banned_char=None):
    """Checks if the input is sanitized."""

    default_chars = ["/", ";", "-", ">", "\\", "!","<", ":", "`", "\"", "|", ")", "("]

    if banned_char == None:
        banned_char = default_chars

    if any((c in banned_char) for c in data):
        return False
    else:
        return True

async def add_role(member, id):
    """Add the role to the member."""

    await member.add_roles(get(member.guild.roles, id=id))

def bool_to_yesno(value: bool) -> str:
    return 'Yes' if value else 'No'
