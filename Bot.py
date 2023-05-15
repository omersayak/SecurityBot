import asyncio
from pyrogram import Client, filters, utils
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import ChatPermissions , Message
from datetime import datetime, timedelta
import re
from telegraph import upload_file
import os
import requests
import json
import time 



print("API bilgilerinizi girin:")
api_id = input("API ID: ")
api_hash = input("API Hash: ")
bot_token = input("Bot Token: ")

bot = Client(
    "my_first_project",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)


START_MESSAGE = "Merhabalar Ben SİberGüvenlik Grubuna Aİt Güvenlik Botuyum."

START_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton('CHANNEL', url='https://t.me/safaksiz_egitim'),
        InlineKeyboardButton('GROUP', url='https://t.me/SiberGuvenlikChat_TR')
    ],
    [
        InlineKeyboardButton('OWNER', url='https://t.me/Professore_1/')

    ]
   
]

@bot.on_message(filters.command('start') & filters.private) # Creating a command
async def command1(bot, message): # Creating a function
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview = True
    )


COMMANDS = [
    "/start - Botu başlatır",
    "/help - Komut listesini gösterir",
    "/photo - Rastgele Fotoğraf atar",
    "/leave - Bot grupdan ayrılır",
    "/tlg - Telegraph Linki oluşturmak için bilgi",
    "/tl - Telegraph Linki oluşturmak",
    "/ban - Kulanıcı banlar",
    "/unban - Banlanan kullanıcının banı kaldırılır",
    "/mute - Kullanıcıyı muteler",
    "/unmute - Mutelenen kullanıcının mutesini kaldırır.",
    "",
    "",
    # Diğer komutlar buraya eklenebilir
]

@bot.on_message(filters.command('help')) 
async def command1(bot, message): 
    command_list = "\n".join(COMMANDS)
    await message.reply_text(f"Komut Listesi:\n\n{command_list}")





# #echobot
# @bot.on_message(filters.text & filters.group)
# async def echobot(client, message):
#    await message.reply_text(message.text)



#welcomebot
GROUP = "SiberGuvenlikChat_TR" # Group İd/Username, Can also be a list of multiple GROUP ids/usernames
WELCOME_MESSAGE = "Merhaba, SiberGüvenlik Grubuna Hoşgeldinnn Dostumm!" # Welcome message


@bot.on_message(filters.chat(GROUP) & filters.new_chat_members) # filter is only new chat members updates generated in GROUP chat
async def welcomebot(client, message):
    await message.reply_text(WELCOME_MESSAGE) # Send the welcome message






@bot.on_message(filters.command('photo')) 
async def command3(bot, message): 
   await bot.send_photo(message.chat.id, "https://imgur.com/gallery/wYTCtRu") 



@bot.on_message(filters.audio & filters.private)
async def audio(bot, message):
    await message.reply(message.audio.file_id) 



@bot.on_message(filters.command('audio')) 
async def command4(client, message): 
   await client.send_audio(message.chat.id, "CQACAgQAAxkBAANRZF39fXATfFuTTLO0nSYOFHoRjtAAAlURAAI0PvBSMLdLIYWMDvceBA") 



@bot.on_message(filters.video & filters.private)
async def audio(bot, message):
    await message.reply(message.video.file_id) 


@bot.on_message(filters.command('leave') & filters.group)
async def leave(client, message):
    await client.send_message(message.chat.id, "Görüşmek üzere dostlar!!")
    await client.leave_chat(message.chat.id)


#ban user forever
@bot.on_message(filters.command('ban') & filters.group)
async def ban(client, message):
    await message.delete()
    await client.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Banned")




@bot.on_message(filters.command('unban') & filters.group)
async def ban(client, message):
    await message.delete()
    await client.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Unbanned")











@bot.on_message(filters.command('mute') & filters.group)
async def mute(client, message):
    await message.delete()
    # Parse the time duration from the command
    try:
        duration_str = re.search(r'(\d+)([dhma])', message.command[1]).groups()
        duration_num = int(duration_str[0])
        duration_unit = duration_str[1]

        if duration_unit == 'm':
            duration = timedelta(minutes=duration_num)
        elif duration_unit == 'h':
            duration = timedelta(hours=duration_num)
        elif duration_unit == 'd':
            duration = timedelta(days=duration_num)
        elif duration_unit == 'a':
            duration = timedelta(days=365 * duration_num)
    except (IndexError, AttributeError):
        await client.send_message(chat_id=message.chat.id, text="Lütfen bir zaman periyodu belirtin. Örneğin: `.mute 4h`")
        return

    # Apply the mute
    await client.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        permissions=ChatPermissions(),
        until_date=datetime.now() + duration
    )

        # Send a message to confirm the mute
    duration_str = re.search(r'(\d+[dhma])+', message.command[1]).group()
    await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} {duration_str} boyunca mutelendi.")

    
        



@bot.on_message(filters.command('unmute') & filters.group)
async def kick(client, message: Message):
    await message.delete()
    await client.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        permissions=ChatPermissions(can_send_messages=True),
        until_date=datetime.now() + timedelta(days=1)
    )
    await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Mute  Kaldırıldı")   







      

@bot.on_message(filters.command('tlg') & filters.private)
async def start(client, message):
    text = f"""
Heya {message.from_user.mention},
I am here to generate Telegraph links for your media files.

Simply send a valid media file directly to this chat.
Valid file types are 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

To generate links in **group chats**, add me to your supergroup and send the command <code>/tl</code> as a reply to a valid media file.

🏠 | [Home](https://t.me/SiberGuvenlikChat_TR)
            """
    await bot.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@bot.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 Downloading media... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@bot.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 Downloading media... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                  





# @bot.on_message(filters.text)
# async def delete_text(client, message):
#     word_list = [
#         "Aq",
#         "amk",
#         "amq",
#         "amcık",
#         "yarrak",
#         "sik",
#         "daşşak"
#     ]
#     if message.text in word_list:
#         await message.delete()
#         await client.send_message(message.chat.id, "Bloklisted word!!")



mute_count = {}

async def process_message(client, message):
    word_list = [
        "aq",
        "amk",
        "amq",
        "amcık",
        "yarrak",
        "sik",
        "daşşak",
        "amcık",
        "sikerim",
        "yavşak",
        "sikik",
        "gevşek",
        "orospu",
        "oruspu",
        "piç",
        "kavat",
        "gavat",
        "amcık ağızlı",
        "sevişmek",
        "sokuşmak"
    ]
    user_id = message.from_user.id
    lower_text = message.text.lower()  # Mesajdaki kelimeyi küçük harflere dönüştür
    if lower_text in word_list:
        if user_id in mute_count:
            mute_count[user_id] += 1
            remaining_attempts = 5 - mute_count[user_id]
            if remaining_attempts > 0:
                delete_message = await message.reply_text(
                    f"{message.from_user.mention} {remaining_attempts} daha fazla uyarı alırsanız mute yiyeceksiniz!"
                )
                await asyncio.sleep(2)  # 2 saniye bekle
                await message.delete()  # Mesajı sil
                await delete_message.delete()  # Uyarı mesajını sil
                
            if mute_count[user_id] >= 5:
                message_copy = message.copy()
                await mute_user(client, message_copy)
                
        else:
            mute_count[user_id] = 1

@bot.on_message(filters.text & filters.group)
async def delete_text(client, message):
    await process_message(client, message)

async def mute_user(client, message):
    user_id = message.from_user.id
    duration = timedelta(minutes=10)
    
    await client.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        permissions=ChatPermissions(),
        until_date=datetime.now() + duration
    )
    
    await message.reply_text(
        f"{message.from_user.mention} 10 dakika boyunca mutelendi."
    )
    
    mute_count[user_id] = 0 
    await message.delete()  # Mesajı sil






print("I AM ALIVE")


bot.run()