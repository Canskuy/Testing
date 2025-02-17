from pyrogram import filters
from KiritoRobot import pbot as komsol
from KiritoRobot.utils.errors import capture_err
from KiritoRobot.utils.functions import make_carbon


@komsol.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await komsol.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()
