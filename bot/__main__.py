from datetime import datetime as dt
import os
from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    
    data,
    app,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    watermark 
)
from bot.helper_funcs.utils import add_task, on_task_complete
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)


from bot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)

from bot.commands import Command
from bot.plugins.call_back_button_handler import button
sudo_users = "1666551439" 
crf.append("24")
codec.append("libx264")
resolution.append("1920x1080")
preset.append("veryfast")
audio_b.append("40k")
# 🤣


uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    
    
    #
    app.set_parse_mode("html")
    #
    # STATUS ADMIN Command

    # START command
    incoming_start_message_handler = MessageHandler(
        incoming_start_message_f,
        filters=filters.command(["start", f"start@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_start_message_handler)
    
    
    @app.on_message(filters.incoming & filters.command(["crf", f"crf@{BOT_USERNAME}"]))
    async def changecrf(app, message):
        if message.from_user.id in AUTH_USERS:
            cr = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {cr} crf"
            crf.insert(0, f"{cr}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")
    #@app.on_message(filters.incoming & filters.command(["nothumb", f"nothumb@{BOT_USERNAME}"]))
    #async def rmt(app, message):
        #if message.from_user.id in AUTH_USERS:
            #os.system('rm thumb.jpg')
           # F = "Ok! I will be uploading files with no thumbnail"
            #await message.reply(F)
                 
    @app.on_message(filters.incoming & filters.command(["settings", f"settings@{BOT_USERNAME}"]))
    async def settings(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text(f"<b>ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪʟʟ ʙᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ꜰɪʟᴇ :</b>\n\n<b>ᴄᴏᴅᴇᴄ</b> : {codec[0]} \n<b>ᴄʀꜰ</b> : {crf[0]} \n<b>ʀᴇꜱᴏʟᴜᴛɪᴏɴ</b> : {resolution[0]} \n<b>ᴘʀᴇꜱᴇᴛ</b> : {preset[0]} \n<b>ᴀᴜᴅɪᴏ ʙɪᴛʀᴀᴛᴇꜱ</b> : {audio_b[0]}")
            
            
               
    @app.on_message(filters.incoming & filters.command(["resolution", f"resolution@{BOT_USERNAME}"]))
    async def changer(app, message):
        if message.from_user.id in AUTH_USERS:
            r = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {r} resolution"
            resolution.insert(0, f"{r}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

            
               
    @app.on_message(filters.incoming & filters.command(["preset", f"preset@{BOT_USERNAME}"]))
    async def changepr(app, message):
        if message.from_user.id in AUTH_USERS:
            pop = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {pop} preset"
            preset.insert(0, f"{pop}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

            
    @app.on_message(filters.incoming & filters.command(["codec", f"codec@{BOT_USERNAME}"]))
    async def changecode(app, message):
        if message.from_user.id in AUTH_USERS:
            col = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {col} codec"
            codec.insert(0, f"{col}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")
             
    @app.on_message(filters.incoming & filters.command(["audio", f"audio@{BOT_USERNAME}"]))
    async def changea(app, message):
        if message.from_user.id in AUTH_USERS:
            aud = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {aud} audio"
            audio_b.insert(0, f"{aud}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")
            
        
    @app.on_message(filters.incoming & filters.command(["compress", f"compress@{BOT_USERNAME}"]))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ")
        query = await message.reply_text("ᴘʟᴇᴀꜱᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ, ᴇɴᴄᴏᴅᴇ ᴡɪʟʟ ꜱᴛᴀʀᴛ ꜱᴏᴏɴ", quote=True)
        data.append(message.reply_to_message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message.reply_to_message)     
 
    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("ʀᴇꜱᴛᴀʀᴛɪɴɢ ᴛʜᴇ ʙᴏᴛ")
            quit(1)
        
    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
      data.clear()
      await message.reply_text("Successfully cleared Queue ...")
         
        
    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ")
        query = await message.reply_text("ᴘʟᴇᴀꜱᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ, ᴇɴᴄᴏᴅᴇ ᴡɪʟʟ ꜱᴛᴀʀᴛ ꜱᴏᴏɴ", quote=True)
        data.append(message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message)
            
    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ")
        os.system('rm thumb.jpg')
        await message.download(file_name='/app/thumb.jpg')
        await message.reply_text('Thumbnail Added')
        
    @app.on_message(filters.incoming & filters.command(["cancel", f"cancel@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await incoming_cancel_message_f(app, message)
        
        
    @app.on_message(filters.incoming & filters.command(["exec", f"exec@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await exec_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["eval", f"eval@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await eval_message_f(app, message)
        
    @app.on_message(filters.incoming & filters.command(["stop", f"stop@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await on_task_complete()    
   
    @app.on_message(filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("ʜᴇʀᴇ ᴀʀᴇ ᴍʏ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.</b>\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ʜɪɢʜ ʟᴇᴠᴇʟ ᴇғғɪᴄɪᴇɴᴄʏ ᴠɪᴅᴇᴏ ᴇɴᴄᴏᴅɪɴɢ ʙᴏᴛ ᴄᴏᴅᴇᴅ ɪɴ ᴘʏᴛʜᴏɴ.\nʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴇɴᴄᴏᴅɪɴɢ sᴇᴛᴛɪɴɢs sᴜᴄʜ ᴀs ᴄʀғ, ᴄᴏᴅᴇᴄ, ᴀᴜᴅɪᴏ ʙɪᴛʀᴀᴛᴇs, sᴘᴇᴇᴅ ᴀɴᴅ ǫᴜᴀʟɪᴛʏ.</b>\nʏᴏᴜ ᴄᴀɴ sᴛᴏᴘ ᴘʀᴏᴄᴇssᴇs ɪɴ ʙᴇᴛᴡᴇᴇɴ ᴘʀᴇssɪɴɢ ᴛʜᴇ ᴄᴀɴᴄᴇʟ ʙᴜᴛᴛᴏɴ. \nꜰᴏʀ ꜰꜰᴍᴘᴇɢ ʟᴏᴠᴇʀꜱ - ᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴄʀꜰ ʙʏ /eval crf.insert(0, 'crf value')\nᴊᴏɪɴ @anime_channelz ꜰᴏʀ ᴀɴɪᴍᴇꜱ \n\nᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴡɪʟʟ ʙᴇ ᴀᴅᴅᴇᴅ ᴀs sᴏᴏɴ ᴀs ᴘᴏssɪʙʟᴇ.", quote=True)

    @app.on_message(filters.incoming & filters.command(["corrupt", f"corrupt@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("hmm listen there are some files which doesn't have proper metadata or have been corrupted so we can't encode that so find some good source files", quote=True)

    @app.on_message(filters.incoming & filters.command(["series", f"series@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("check @seriez_encoded and @series_encoded for Series", quote=True)

    @app.on_message(filters.incoming & filters.command(["anime", f"movies@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("join here @animedubed", quote=True)

    @app.on_message(filters.incoming & filters.command(["request", f"request@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("@Mk255 to Request movies or series", quote=True)


    @app.on_message(filters.incoming & filters.command(["rules", f"rules@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("RULES TO FOLLOW\n\n1)Encode your Files one by one or leave a time of gap inbetween\n\n2)Bot restarts every 6 hours so check /ping for uptime\n\n3)If bot stops encoding or stucks at 0% use #restart\n\nUsing #restart unnecessary leads ban/warn\n check /corrupt to know why bot won't encode some files", quote=True)

    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)
    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
      stt = dt.now()
      ed = dt.now()
      v = ts(int((ed - uptime).seconds) * 1000)
      ms = (ed - stt).microseconds / 1000
      p = f"hey I'm up 🥶 = {ms}ms"
      await message.reply_text(v + "\n" + p)

    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    # run the APPlication
    app.run()
