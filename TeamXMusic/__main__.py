import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TeamXMusic import LOGGER, app, userbot
from TeamXMusic.core.call import Teamy
from TeamXMusic.misc import sudo
from TeamXMusic.plugins import ALL_MODULES
from TeamXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS, COOKIES_URL
from TeamXMusic.plugins.sudo.cookies import set_cookies

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TeamXMusic.plugins" + all_module)
    LOGGER("TeamXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Teamy.start()
    try:
        await Teamy.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("TeamXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    res = await set_cookies(COOKIES_URL)
    LOGGER("TeamXMusic").info(f"{res}")
    await Teamy.decorators()
    await idle()
    await app.stop()
    LOGGER("TeamXMusic").info("Stopping TeamX Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
