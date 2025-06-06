import random
from info import *
import logging
logger = logging.getLogger(__name__)
from util.human_readable import humanbytes
from databse import db
from pyrogram import filters, enums, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from util.file_properties import get_name, get_hash, get_media_file_size
from pyrogram.types import ReplyKeyboardMarkup

@Client.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹\n\nᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲\n\nSᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔</b>\n\n <blockquote>Nᴏ Iɴᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, Nᴏ ∇ΞʀɪꜰɪᴄΔᴛɪᴏɴ, FЯΞΞ ᴏꜰ Cᴏꜱᴛ</blockquote> ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    )
                    
                )
                return
            except Exception:
                await m.reply_photo(
                    photo="https://graph.org/file/8653b4816d7a19dd4f267.jpg",
                    caption="**ʜᴇʟʟᴏ...⚡\n\nɪ,ᴀᴍ ᴀ ᴩʀᴏ✨️ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ. A sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ʙᴇꜱᴛ ꜰᴇᴀᴛᴜʀᴇꜱ⚡️.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ...**",
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_Moviez_X")],
                            [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                            [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                       ]
                    ),
            
                )
                return
        await m.reply_photo(
                    photo="https://graph.org/file/8653b4816d7a19dd4f267.jpg",
                    caption="**ʜᴇʟʟᴏ...⚡\n\nɪ,ᴀᴍ ᴀ ᴩʀᴏ✨️ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ. A sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ʙᴇꜱᴛ ꜰᴇᴀᴛᴜʀᴇꜱ⚡️.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ...**",
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_Moviez_X")],
                            [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                            [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                       ]
                    ),
                )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲**\n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**\n\n<blockquote>Nᴏ Iɴᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, Nᴏ ∇ΞʀɪꜰɪᴄΔᴛɪᴏɴ, FЯΞΞ ᴏꜰ Cᴏꜱᴛ</blockquote>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    )
                    
                )
                return
            except Exception:
                await message.reply_photo(
                    photo="https://graph.org/file/8653b4816d7a19dd4f267.jpg",
                    caption="**ʜᴇʟʟᴏ...⚡\n\nɪ,ᴀᴍ ᴀ ᴩʀᴏ✨️ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ. A sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ʙᴇꜱᴛ ꜰᴇᴀᴛᴜʀᴇꜱ⚡️.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ...**",
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_Moviez_X")],
                            [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                            [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                       ]
                   ),
            
                )

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@Client.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲**\n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**\n\n<blockquote>Nᴏ Iɴᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, Nᴏ ∇ΞʀɪꜰɪᴄΔᴛɪᴏɴ, FЯΞΞ ᴏꜰ Cᴏꜱᴛ</blockquote>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    )
                    
                )
                return
        except Exception:
                await message.reply_photo(
                    photo="https://graph.org/file/b13a16615914952c141e4.jpg",
                    caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ , ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴀ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴀʟꜱᴏ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ [ᴩʀᴏ✨️, ᴩᴀɪᴅ ꜰᴇᴀᴛᴜʀᴇ...ꜰᴏʀ ᴍᴏʀᴇ ᴄᴏɴᴛᴀᴄᴛ @Syd_xyz ]. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsᴛ../\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\n⚠Cᴜᴀᴛɪᴏɴ ᴀʜᴇᴀᴅ ;\n✧ sᴘᴀᴍ = ʙᴀɴ \n✧ ᴅᴏɴᴛ ᴜꜱᴇ ᴀᴅᴜʟᴛ ᴠɪᴅᴇᴏꜱ, ɪꜰ yᴏᴜ ᴡᴀɴᴛ yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ꜱɪᴛᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴏɢʟᴇ ᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ꜰɪʟᴇꜱ,\nᴅᴏɴᴛ ᴜꜱᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴏʀ ᴛʜᴀᴛ [ʙᴇ ᴀ ɢᴏᴏᴅ ᴏɴᴇ😇 #yᴏᴜᴡɪʟʟᴀɢᴇᴛᴄʜᴀɴᴄᴇᴀʟꜱᴏ] \n\nᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜᴩᴩᴏʀᴛ ᴜꜱ!!!**", 
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ Gᴇᴛ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_Moviez_X/228")],
                            [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Pʀᴏ-ꜱɪᴛᴇ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                            [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                       ]
                    )
                )
                return
    await message.reply_photo(
                    photo="https://graph.org/file/b13a16615914952c141e4.jpg",
                    caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ , ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴀ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴀʟꜱᴏ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ [ᴩʀᴏ✨️, ᴩᴀɪᴅ ꜰᴇᴀᴛᴜʀᴇ...ꜰᴏʀ ᴍᴏʀᴇ ᴄᴏɴᴛᴀᴄᴛ @Syd_xyz ]. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsᴛ../\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\n⚠Cᴜᴀᴛɪᴏɴ ᴀʜᴇᴀᴅ ;\n✧ sᴘᴀᴍ = ʙᴀɴ \n✧ ᴅᴏɴᴛ ᴜꜱᴇ ᴀᴅᴜʟᴛ ᴠɪᴅᴇᴏꜱ, ɪꜰ yᴏᴜ ᴡᴀɴᴛ yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ꜱɪᴛᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴏɢʟᴇ ᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ꜰɪʟᴇꜱ,\nᴅᴏɴᴛ ᴜꜱᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴏʀ ᴛʜᴀᴛ [ʙᴇ ᴀ ɢᴏᴏᴅ ᴏɴᴇ😇 #yᴏᴜᴡɪʟʟᴀɢᴇᴛᴄʜᴀɴᴄᴇᴀʟꜱᴏ] \n\nᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜᴩᴩᴏʀᴛ ᴜꜱ!!!**", 
                    reply_markup=InlineKeyboardMarkup(
                       [
                            [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ Gᴇᴛ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_Moviez_X/228")],
                            [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Pʀᴏ-ꜱɪᴛᴇ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                            [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                       ]
                    )
                )

@Client.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
             
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲**\n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**\n\n<blockquote>Nᴏ Iɴᴅɪʀᴇᴄᴛ ʟɪɴᴋꜱ, Nᴏ ∇ΞʀɪꜰɪᴄΔᴛɪᴏɴ, FЯΞΞ ᴏꜰ Cᴏꜱᴛ</blockquote>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await message.reply_photo(
                 photo="https://graph.org/file/bee17850e842b8ecaad3c.jpg",
                 caption="""<b>╭━━━━━━━⦍ ⸢ʙᴏᴛ-ᴅᴇᴛᴀɪʟꜱ⸥ ⦐</b>
┃
┣⪼<b>Bᴏᴛ ɴΔᴍᴇ : <a href='https://t.me/Ms_FiLe2LINk_bOt'>˹ᴍꜱ˼ ˾ꜰɪʟᴇ 2 ʟɪɴᴋ˺ 𐂴</a></b>
┣⪼<b>Oᴡɴᴇʀ : <a href='http://t.me/Syd_Xyz'>мґ 𝕾𝖄𝕯 ️✨️️</a></b>
┣⪼<b>Uᴘᴅᴀᴛᴇꜱ : <a href='https://t.me/Bot_cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 𐂭</a></b>
┣⪼<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/MrMoviez_Group'>Mʀ Mᴏᴠɪᴇᴢ Gʀᴩ ⍟</a></b>
┣⪼<b>sᴇʀᴠᴇʀ : <a href='https://mrsydoo.blogspot.com/2023/05/you-cant-count-no-of-ads-ad-site.html'>Bʟᴏɢɢᴇʀ; TʜΞ Δᴅ SɪΓΞ 😊</a></b>
┣⪼<b>ʟɪʙʀᴀʀʏ : <a href='https://t.me/+amIvlfZkOQZlYTY1'>Tɢ 🫥</a></b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: <a href='https://t.me/+iHakK2FaA5dhNTg1'>ΞИGLISH🤕🤕</a></b>
┣⪼<b>Cʀᴇᴅɪᴛꜱ : <a href='https://t.me/+RuD7qZl8PFJiNTI1'>PᴀʀΔʟʟᴇʟ CɪɴᴇᴍΔꜱ ™</a></b>
┣⪼<b>Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ : <a href='https://t.me/+d7djWG_VLfcwMzg9'>RᴇQᴜᴇꜱᴛ-MᴏVɪᴇꜱ</a></b>
┣⪼<b>Bᴜɪʟᴅ ∇ᴇʀꜱɪᴏɴ : v1 [≛ Bƴ ʍɾ Sчᴅ ≛]</b>
┃
<b>╰━━━━━━━⦍ ⸢Tʜᴇ-Ξɴᴅ⸥ ⦐</b>""",
                 reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ☆", url="https://t.me/Gettglinks"), InlineKeyboardButton("☼ MᴏVɪᴇꜱ ☼", url="https://t.me/Mod_Moviez_x/228")],
                [InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/nt_Backup/4"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                [InlineKeyboardButton("♤ Mᴏᴠɪᴇꜱ Cʜᴀɴɴᴇʟ ♤", url="https://t.me/Mod_MovIez_X")]
            ]
        )
            )
            return
    await message.reply_photo(
            photo="https://graph.org/file/bee17850e842b8ecaad3c.jpg",
            caption="""<b>╭━━━━━━━⦍ ⸢ʙᴏᴛ-ᴅᴇᴛᴀɪʟꜱ⸥ ⦐</b>
┃
┣⪼<b>Bᴏᴛ ɴΔᴍᴇ : <a href='https://t.me/Ms_FiLe2LINk_bOt'>˹ᴍꜱ˼ ˾ꜰɪʟᴇ 2 ʟɪɴᴋ˺ 𐂴</a></b>
┣⪼<b>Oᴡɴᴇʀ : <a href='http://t.me/Syd_Xyz'>мґ 𝕾𝖄𝕯 ️✨️️</a></b>
┣⪼<b>Uᴘᴅᴀᴛᴇꜱ : <a href='https://t.me/Bot_cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 𐂭</a></b>
┣⪼<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/MrMoviez_Group'>Mʀ Mᴏᴠɪᴇᴢ Gʀᴩ ⍟</a></b>
┣⪼<b>sᴇʀᴠᴇʀ : <a href='https://mrsydoo.blogspot.com/2023/05/you-cant-count-no-of-ads-ad-site.html'>Bʟᴏɢɢᴇʀ; TʜΞ Δᴅ SɪΓΞ 😊</a></b>
┣⪼<b>ʟɪʙʀᴀʀʏ : <a href='https://t.me/+amIvlfZkOQZlYTY1'>Tɢ 🫥</a></b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: <a href='https://t.me/+iHakK2FaA5dhNTg1'>ΞИGLISH🤕🤕</a></b>
┣⪼<b>Cʀᴇᴅɪᴛꜱ : <a href='https://t.me/+RuD7qZl8PFJiNTI1'>PᴀʀΔʟʟᴇʟ CɪɴᴇᴍΔꜱ ™</a></b>
┣⪼<b>Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ : <a href='https://t.me/+d7djWG_VLfcwMzg9'>RᴇQᴜᴇꜱᴛ-MᴏVɪᴇꜱ</a></b>
┣⪼<b>Bᴜɪʟᴅ ∇ᴇʀꜱɪᴏɴ : v1 [≛ Bƴ ʍɾ Sчᴅ ≛]</b>
┃
<b>╰━━━━━━━⦍ ⸢Tʜᴇ-Ξɴᴅ⸥ ⦐</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ☆", url="https://t.me/Gettglinks"), InlineKeyboardButton("☼ MᴏVɪᴇꜱ ☼", url="https://t.me/Mod_Moviez_x/228")],
                [InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/nt_Backup/4"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                [InlineKeyboardButton("♤ Mᴏᴠɪᴇꜱ Cʜᴀɴɴᴇʟ ♤", url="https://t.me/Mod_MovIez_X")]
            ]
        )
    )
