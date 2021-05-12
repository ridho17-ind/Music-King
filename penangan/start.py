# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""🤖 Hai Kamu,Bot ini bisa di pake di vcg!""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📱Bot Music📱", url="https://t.me/Skyzo_Music_Bot")
                  ],[
                    InlineKeyboardButton(
                        "📱Assistant Bot📱", url="https://t.me/SkyzoAssistant"
                    ),
                    InlineKeyboardButton(
                        "👑Owner Bot👑", url="https://t.me/SkyzoGanss"
                    ),
                    InlineKeyboardButton(
                        "🎁Grup Support🎁", url="https://t.me/sahurbabi"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Grup Gabut Online", url="https://t.me/Coba_Aja_Pencet"
                    ),
                    InlineKeyboardButton(
                        "Petunjuk Penggunaan", url="https://telegra.ph/Ultroid-05-12"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📱Grup Support📱", url="https://t.me/sahurbabi"
                    ),
                    InlineKeyboardButton(
                        "👑Owner👑", url="https://t.me/SkyzoGanss"
"
                    )
                ]
            ]
        )
   )
