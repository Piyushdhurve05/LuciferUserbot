import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Devil's Son"

@borg.on(admin_cmd(pattern="hell$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "**★Hell!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"**★ Lucifer**\n★ 😈{ms}👿\n★ My Peru Master:-{DEFAULTUSER}"
    )


CMD_HELP.update(
    {
        "hell": "__**PLUGIN NAME :** hell__\
    \n\n📌** CMD ★** `.hell`\
    \n**USAGE   ★  **Shows you the ping speed of server"
    }
)
