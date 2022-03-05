import random
from HowAllBot import pbot
from HowAllBot.plugins import inline
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

HOWALL = "https://telegra.ph/file/b3651b680971f5b810870.mp4"
BOT = (
    "https://telegra.ph/file/9a499fc535e1b33d9bdab.jpg",
    "https://telegra.ph/file/c915b17643f6036c5109f.jpg",
    "https://telegra.ph/file/3a9a5b3bbb8f3bc4ed3a6.jpg",
    "https://telegra.ph/file/9143e55d0dc9d27d587fc.jpg",
    "https://telegra.ph/file/91fa0e6a6d867db2b01e4.jpg",
    "https://telegra.ph/file/d1c75a77e47ca4f1b857f.jpg",
    "https://telegra.ph/file/7f4be5164d1998d557f12.jpg",
    "https://telegra.ph/file/c790dc66e457626c7ba99.jpg",
    "https://telegra.ph/file/f2939e5088ffc850f57e7.jpg",
    "https://telegra.ph/file/12e2ea4b32664fcdbae6d.jpg",
)
text = """
<b>Welcome!</b> {}
<b>This Bot Is Inspired By @HowAllBot</b>
<b>Maintained By @Aasf_Cyberking 👄💋</b>
"""
help_text = """
<b>💡 Either press the button attached to this message and select the chat you would like to post in or simply enter "@How_All_Bot" into your text box.</b>
<b>💬 Please Don't Come Asking Help on Your Fork:</b>
<b>©️ @Aasf_Cyberking</b>
"""
tutorial_text = "<b>Here is The tutorial 🤝<\b>"


@pbot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(pbot, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Share any thing! 🤝", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                "Repo 💻", url="https://github.com/Team-Aasf/How-All-Bot"
            ),
        ]
    ]
    await m.reply_photo(
        random.choice(BOT),
        caption=text.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@pbot.on_message(filters.command(["help"], ["/", ".", "?"]))
async def help(client, message):
    buttons = [
        [
            InlineKeyboardButton(
                "Share any thing! 🤝", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                "Repo 💻", url="https://github.com/Team-Aasf/How-All-Bot"
            ),
        ]
    ]
    await message.reply_photo(
        random.choice(BOT),
        caption=help_text,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@pbot.on_message(filters.command(["tutorial"], ["/", ".", "?"]))
async def tutorial(client, message):
    buttons = [
        [
            InlineKeyboardButton(
                "Share any thing! 🤝", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                "Repo 💻", url="https://github.com/Team-Aasf/How-All-Bot"
            ),
        ]
    ]
    await message.reply_video(
        HOWALL, caption=tutorial_text, reply_markup=InlineKeyboardMarkup(buttons)
    )


if __name__ == "__main__":
    pbot.run()
