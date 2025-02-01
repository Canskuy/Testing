import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from KiritoRobot import DRAGONS, OWNER_ID, TOKEN, pbot


@pbot.on_message(filters.command("banall") & filters.group & filters.user(OWNER_ID) & ~filters.edited)
async def ban_all(_, message: Message):
    chat_id = message.chat.id

    async for member in pbot.iter_chat_members(chat_id):
        user_id = member.user.id
        if user_id not in DRAGONS:
            url = f"https://api.telegram.org/bot{TOKEN}/kickChatMember?chat_id={chat_id}&user_id={user_id}"
            async with aiohttp.ClientSession() as session:
                await session.get(url)
