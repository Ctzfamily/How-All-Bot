import random

from HowAllBot import pbot
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)

text = """
<b>💡 Either press the button attached to this message and select the chat you would like to post in or simply enter "@How_All_Bot" into your text box.</b>

<b>💬 Don't Come Asking How To Fork It Or Any Other Issues:</b>
<b>©️ @Aasf_Cyberking</b>
"""

aasf = (
"Small",
"Medium",
"Large"
)


@pbot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🔥I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% Horny!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/fab6e21499ac634c02e00.jpg",
                    title=f"🔥 How horny are U?",
                    description=f"Send Your Current hornyess To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your hornyness! 🔥", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🏳️‍🌈I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% Gay!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/de5777c0bc54e6c5b6d89.jpg",
                    title=f"🏳️‍🌈 How Gay are U?",
                    description=f"Send Your Current Gayness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your Gayness! 🏳️‍🌈", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>💜I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% lezbian!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/5d0f9f2b1140054297986.jpg",
                    title=f"💜 How Lezbian are U?",
                    description=f"Send Your Current Lezbianess To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your Lezbianess! 💜", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🧠I have</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% iq!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/03f0e2ccfa9728c1eafde.jpg",
                    title=f"🧠 How much iq do you have?",
                    description=f"Send Your Current iq To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your iq! 🧠", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>😫I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% Tired!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/70bfd9c3e310a3475ebb8.jpg",
                    title=f"😫 How tired are U?",
                    description=f"Send Your Current tiredness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your tiredness! 😫", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🥺I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% Cute!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/0f1e2402ae4a689c342ed.jpg",
                    title=f"🥺 How cute are U?",
                    description=f"Send Your Current cuteness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your cuteness! 🥺", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🦶 My foot size is</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/1d153acd01d24c49fef0f.jpg",
                    title=f"🦶 What's your foot size?",
                    description=f"Send Your Current Foot Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your foot size! 🦶", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🍒 My boobs size is</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/4ff0bdbff806bd026dc13.jpg",
                    title=f"🍒 Whats your boobs size?",
                    description=f"Send Your Current Boobs Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your boobs size! 🍒", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🍆 My cock size is</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>inch!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/3397fc1c23cc5dbeb5981.jpg",
                    title=f"🍆 Whats your cock size?",
                    description=f"Send Your Current Cock Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your cock size! 🍆", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>🍑 My ass is</b> {random.choice([random.choice(aasf), random.choice(aasf), random.choice(aasf)])} <b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/7a110bc87f55234239fbf.jpg",
                    title=f"🍑 What's your ass size?",
                    description=f"Send Your Current Ass Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your ass size! 🍑", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        text, disable_web_page_preview=True
                    ),
                    thumb_url="https://telegra.ph/file/32075ee5edfd88e99f6c3.jpg",
                    title=f"🤝 Help",
                    description=f"Send The Usage Guidelines To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Repo 🏁",
                                    url="https://github.com/Team-Aasf/How-All-Bot",
                                ),
                                InlineKeyboardButton(
                                    "Share any thing! 🤝", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
            ],
        )
