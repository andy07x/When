#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hᴇʟʟᴏ Fᴇʟʟᴏᴡ Usᴇʀ ! \n\nI ᴀᴍ ᴀɴ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴡʜɪᴄʜ ᴇɴᴄᴏᴅᴇ ᴠɪᴅᴇᴏs.</b>. \n\nI ᴄᴀɴ ᴅᴏ ᴀ ʟᴏᴛ ᴏғ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ɪᴜsᴛ ᴇɴᴄᴏᴅɪɴɢ ᴀ ᴠɪᴅᴇᴏ.</b> \n\nᴅᴏ /help ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ."
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = " ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ sᴇʀᴠᴇʀ... \n"
    
    UPLOAD_START = " ᴜᴘʟᴏᴀᴅɪɴɢ...  \n"
    
    COMPRESS_START = " ᴇɴᴄᴏᴅɪɴɢ ... "
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "720p"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n⚔️ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "ᴄᴜꜱᴛᴏᴍ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ. ᴛʜɪꜱ ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ."
    
    CUSTOM_CAPTION_UL_FILE = "720p"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @Linux_Repo"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
