import html

from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

from KiritoRobot import LOGGER, dispatcher
from KiritoRobot.modules.helper_funcs.chat_status import user_admin, user_not_admin

REPORT_GROUP = 12

@user_not_admin
def report(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    chat_name = chat.title or chat.first or chat.username
    admin_list = chat.get_administrators()
    message = update.effective_message

    msg = (
        "<b>⚠️ ATTENTION!</b>\n"
        f"{mention_html(user.id, user.first_name)} [<code>{user.id}</code>] has required an admin action in the group: <b>{html.escape(chat.title)}</b>\n"
        f"\n👉🏻 <a href='{message.link}'>Go to message</a>"
    )

    for admin in admin_list:
        if admin.user.is_bot:  # can't message bots
            continue
        try:
            if message.reply_to_message:
                bot.send_message(
                    admin.user.id,
                    msg,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
                message.reply_to_message.forward(admin.user.id)

                if (
                        len(message.text.split()) > 1
                ):  # If user is giving a reason, send his message too
                    message.forward(admin.user.id)
            else:
                bot.send_message(
                    admin.user.id,
                    msg,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
        except Unauthorized:
            pass
        except BadRequest as excp:  # TODO: cleanup exceptions
            LOGGER.exception("Exception while reporting user")

    bot.send_message(
        chat.id,
        "Report sent.",
        parse_mode=ParseMode.HTML,
    )
    return msg


__help__ = """
We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?

Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.

❂ /report <reason>*:* reply to a message to report it to admins.
❂ @admin*:* reply to a message to report it to admins.

*NOTE:* Neither of these will get triggered if used by admins.
"""

REPORT_HANDLER = CommandHandler(
    "report", report, filters=Filters.chat_type.groups, run_async=True
)
ADMIN_REPORT_HANDLER = MessageHandler(
    Filters.regex(r"(?i)@admin(s)?"), report, run_async=True
)

dispatcher.add_handler(REPORT_HANDLER, REPORT_GROUP)
dispatcher.add_handler(ADMIN_REPORT_HANDLER, REPORT_GROUP)

__mod_name__ = "Reports"
__handlers__ = [
    (REPORT_HANDLER, REPORT_GROUP),
    (ADMIN_REPORT_HANDLER, REPORT_GROUP),
]
