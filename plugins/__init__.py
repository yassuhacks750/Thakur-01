from pyrogram import Client as bot, filters
from pyrogram.types import Message
import asyncio
from master import helper
from config import Config

class Data:
    START = (
        "🌟 Welcome {0}! 🌟\n\n"
    )

@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    user = await bot.get_me()
    mention = user.mention
    start_message = await bot.send_message(
        m.chat.id,
        Data.START.format(m.from_user.mention, mention)
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(m.from_user.mention, mention) +
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: [⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 0%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(m.from_user.mention, mention) +
        "Loading features... ⏳\n\n"
        "Progress: [🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 25%\n\n"
    )
    
    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(m.from_user.mention, mention) +
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: [🟧🟧🟧🟧🟧⬜️⬜️⬜️⬜️⬜️] 50%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(m.from_user.mention, mention) +
        "Checking subscription status... 🔍\n\n"
        "Progress: [🟨🟨🟨🟨🟨🟨🟨🟨⬜️⬜️] 75%\n\n"
    )

    await asyncio.sleep(1)
    if m.chat.id in Config.AUTH_USERS:
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "`Great! You are a premium member! `🌟\n\n"
            f"**If you face any problem contact - ** {Config.CREDIT}"
        )
    else:
        await asyncio.sleep(2)
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "`Great! You are a premium member! `🌟\n\n"
            f"**If you face any problem contact - ** {Config.CREDIT}"
        )


@bot.on_message(filters.command("stop"))
async def restart_handler(bot, m):
    await helper.clear(m)

