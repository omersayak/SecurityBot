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
from pyrogram.errors import PeerIdInvalid, UserAdminInvalid
from pyrogram import errors
from pyrogram import types
import random




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








photo_list = [
    "https://unsplash.com/photos/HZQC3rEm6JY",
    "https://pixabay.com/tr/photos/k%c3%b6pek-yavrusu-evcil-hayvan-k%c3%b6pek-2785074/",
    "https://pixabay.com/tr/vectors/k%c3%b6pek-hayvan-evcil-hayvan-vesika-1728494/",
    "https://pixabay.com/tr/photos/k%c3%b6pek-yavrusu-k%c3%b6pek-evcil-hayvan-1903313/",
    "https://pixabay.com/tr/photos/istif-hayvanlar-peri-masal%c4%b1-1651945/",
    "https://pixabay.com/tr/photos/hayvan-k%c3%b6pek-evcil-hayvan-4118585/",
    "https://pixabay.com/tr/photos/husky-k%c3%b6pek-evcil-hayvan-malamut-3380548/",
    "https://pixabay.com/tr/photos/sokak-gece-ak%c5%9fam-kent-kentsel-89197/",
    "https://pixabay.com/tr/photos/walking-man-ladder-man-people-dark-4949569/",
    "https://pixabay.com/tr/photos/gizli-orman-karanl%c4%b1k-do%c4%9fa-a%c4%9fa%c3%a7lar-3120483/",
    "https://pixabay.com/tr/photos/ay-dolunay-g%c3%b6ky%c3%bcz%c3%bc-gece-g%c3%b6ky%c3%bcz%c3%bc-1859616/",
    "https://pixabay.com/tr/photos/moda-kad%c4%b1n-vesika-model-k%c4%b1z-3080644/",
    "https://pixabay.com/tr/photos/do%c4%9fa-orman-manzara-geceleyin-3194001/",
    "https://pixabay.com/tr/photos/tesett%c3%bcr-ba%c5%9f%c3%b6rt%c3%bcs%c3%bc-vesika-duvak-3064633/",
    "https://pixabay.com/tr/photos/ay-dolunay-deniz-g%c3%b6ky%c3%bcz%c3%bc-2762111/",
    "https://pixabay.com/tr/photos/k%c4%b1z-y%c3%bcz-renkli-renkler-sanatsal-2696947/",
    "https://pixabay.com/tr/illustrations/suluboya-vesika-karakter-k%c4%b1z-kad%c4%b1n-1020509/",
    "https://pixabay.com/tr/vectors/maymun-mandala-sanat-eseri-sanat-786858/",
    "https://pixabay.com/tr/illustrations/tablo-%c5%9f%c3%b6valye-ya%c4%9fl%c4%b1boya-resim-ay-3995999/",
    "https://pixabay.com/tr/photos/telefon-duvar-ka%c4%9f%c4%b1d%c4%b1-suluboya-tablo-2681039/",
    "https://pixabay.com/tr/photos/bisiklet-%c3%a7ocuklar-duvar-yaz%c4%b1s%c4%b1-3045580/",
    "https://pixabay.com/tr/illustrations/fantezi-i%cc%87nsanlar-mistisizm-mistik-2964231/",
    "https://pixabay.com/tr/photos/foto%c4%9fraf-manip%c3%bclasyonu-dijital-sanat-2110496/",
    "https://pixabay.com/tr/photos/tokyo-gece-lamborghini-street-car-4132144/",
    "https://pixabay.com/tr/photos/kopyalar-rent-a-car-minyat%c3%bcrler-810316/",
    "https://pixabay.com/tr/photos/street-car-oto-trafik-g%c3%bcnbat%c4%b1m%c4%b1-5183446/",
    "https://pixabay.com/tr/photos/akdeniz-adas%c4%b1-mountan-bulut-112003/",
    "https://pixabay.com/tr/photos/pinewood-yang%c4%b1n-yanm%c4%b1%c5%9f-%c3%a7am-3710491/",
    "https://pixabay.com/tr/photos/peri%c5%9fan-yang%c4%b1n-i%cc%87%c3%a7mek-koy-%c3%a7al%c4%b1-3710502/",
    "https://pixabay.com/tr/illustrations/tutulma-g%c3%bcne%c5%9f-uzay-ay-gezegen-1492818/",
    "https://pixabay.com/tr/photos/s%c4%b1cak-hava-balonu-g%c3%b6l-balon-g%c3%b6ky%c3%bcz%c3%bc-736879/",
    "https://pixabay.com/tr/photos/ay-evren-uzay-samanyolu-g%c3%b6kada-2048727/",
    "https://pixabay.com/tr/photos/dolunay-gece-g%c3%b6ky%c3%bcz%c3%bc-luna-ay-1869760/",
    "https://pixabay.com/tr/photos/a%c4%9fa%c3%a7-g%c3%bcn-bat%c4%b1m%c4%b1-bulutlar-g%c3%b6ky%c3%bcz%c3%bc-736885/",
    "https://pixabay.com/tr/photos/bulvar-a%c4%9fa%c3%a7lar-yol-g%c3%bcne%c5%9f-%c4%b1%c5%9f%c4%b1nlar%c4%b1-815297/",
    "https://pixabay.com/tr/illustrations/tutulma-g%c3%bcne%c5%9f-uzay-ay-gezegen-1492818/",
    "https://pixabay.com/tr/photos/k%c4%b1z-g%c3%bczellik-peri-masallar%c4%b1-fantezi-2436545/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-at%c4%b1%c5%9f-b%c3%bcy%c3%bcl%c3%bc-hayal-kurmak-3551832/",
    "https://pixabay.com/tr/illustrations/kad%c4%b1n-k%c4%b1z-g%c3%bczel-vesika-moda-di%c5%9fi-3219507/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-k%c4%b1z%c4%b1l-sa%c3%a7l%c4%b1-atk%c4%b1-%c3%b6rme-triko-1867093/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-k%c4%b1z-g%c3%b6z-model-atk%c4%b1-arap%c3%a7a-590490/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-y%c4%b1kama-vietnam-asya-gen%c3%a7-1822646/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-at%c4%b1%c5%9f-g%c3%bczellik-at-di%c5%9fi-k%c4%b1z-3481756/",
    "https://pixabay.com/tr/photos/bikini-model-dudaklar-di%c5%9fi-k%c4%b1z-885382/",
    "https://pixabay.com/tr/photos/marilyn-monroe-sanat-berabere-885229/",
    "https://pixabay.com/tr/photos/spor-salonu-spor-a%c4%9f%c4%b1rl%c4%b1k-%c3%a7al%c4%b1%c5%9fmas%c4%b1-457072/",
    "https://pixabay.com/tr/photos/adam-kad%c4%b1n-k%c3%b6pek-evcil-hayvan-2425121/",
    "https://pixabay.com/tr/photos/adam-siyah-vesika-erkek-siyah-adam-2442565/",
    "https://pixabay.com/tr/photos/adam-hindistan-hindu-vesika-613601/",
    "https://pixabay.com/tr/photos/beste-maymun-kad%c4%b1n-kahkaha-sepya-2925179/",
    "https://pixabay.com/tr/photos/kedi-kedi-yavrusu-evcil-hayvanlar-2934720/",
    "https://pixabay.com/tr/photos/aslan-k%c3%bckreme-afrika-hayvan-3012515/",
    "https://pixabay.com/tr/photos/y%c3%bcz-buru%c5%9fturma-e%c4%9flenceli-ifade-388987/",
    "https://pixabay.com/tr/photos/k%c3%b6pek-evcil-hayvan-corgi-do%c4%9furmak-3389729/",
    "https://pixabay.com/tr/photos/mount-cook-yeni-zelanda-7323246/",
    "https://pixabay.com/tr/photos/tibet-%c3%a7in-da%c4%9flar-manzara-4025999/",
    "https://pixabay.com/tr/photos/k%c3%b6pek-bal%c4%b1%c4%9f%c4%b1-bal%c4%b1k-deniz-okyanus-164899/",
    "https://pixabay.com/tr/photos/yal%c4%b1%c3%a7apk%c4%b1n%c4%b1-ku%c5%9f-bal%c4%b1k-yakalamak-1338235/",
    "https://pixabay.com/tr/photos/do%c4%9fa-arka-plan-do%c4%9fa-arka-plan%c4%b1-2739115/",
    "https://pixabay.com/tr/photos/kartal-ku%c5%9f-y%c4%b1rt%c4%b1c%c4%b1-ku%c5%9f-kanatlar-1753002/",
    "https://pixabay.com/tr/photos/%c3%a7ocuklar-kazan%c3%a7-ba%c5%9far%c4%b1-video-oyunu-593313/",
    "https://pixabay.com/tr/photos/k%c4%b1z-y%c3%bcr%c3%bcme-oyuncak-ay%c4%b1-%c3%a7ocuk-447701/",
    "https://pixabay.com/tr/photos/kad%c4%b1n-yaln%c4%b1zl%c4%b1k-%c3%bcz%c3%bcnt%c3%bc-duygular-1958723/",
    "https://pixabay.com/tr/photos/adam-yaln%c4%b1zl%c4%b1k-deniz-ak%c5%9fam-siluet-2915187/",
    "https://pixabay.com/tr/illustrations/d%c3%bc%c5%9fen-mobil-karanl%c4%b1k-gece-7372662/",
    "https://pixabay.com/tr/photos/ayna-adam-karanl%c4%b1k-%c3%bcz%c3%bcnt%c3%bc-3864155/",
    "https://pixabay.com/tr/photos/el-korkmak-%c3%a7aresizlik-ifade-2593743/",
    "https://pixabay.com/tr/photos/ya%c4%9fmur-yaln%c4%b1z-%c3%a7ocuk-%c3%a7ocuk-yaln%c4%b1zl%c4%b1k-1570854/",
    "https://pixabay.com/tr/photos/%c3%bcz%c3%bcnt%c3%bc-affetmek-%c3%bczg%c3%bcn-insanlar-699606/"

]

@bot.on_message(filters.command('photo'))
async def command3(bot, message):
    await message.delete()

    # Randomly select a photo from the list
    random_photo = random.choice(photo_list)

    # Send the photo
    await bot.send_photo(message.chat.id, random_photo)




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


# #ban user forever
# @bot.on_message(filters.command('ban') & filters.group)
# async def ban(client, message):
#     await message.delete()
#     await client.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
#     await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Banned")







@bot.on_message(filters.command('ban') & filters.group)
async def ban(client, message):
    await message.delete()

    # Check if the user trying to ban is an administrator
    try:
        user = await client.get_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        if user.status == "administrator":
            raise UserAdminInvalid
    except UserAdminInvalid:
        await client.send_message(chat_id=message.chat.id, text="Bir yöneticiyi banlamaya çalışıyorsunuz.")
        return
    except errors.FloodWait as e:
        await client.send_message(chat_id=message.chat.id, text=f"Bir hata oluştu: {str(e)}")
        return

    # Ban the user
    try:
        await client.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} banlandı.")
    except errors.FloodWait as e:
        await client.send_message(chat_id=message.chat.id, text=f"Bir Yöneticiyi Banlayamam Dostummm!!")
    except errors.exceptions.BadRequest as e:
        await client.send_message(chat_id=message.chat.id, text=f"Bir Yöneticiyi Banlayamam Dostummm!!")



@bot.on_message(filters.command('unban') & filters.group)
async def ban(client, message):
    await message.delete()
    await client.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Unbanned")











# @bot.on_message(filters.command('mute') & filters.group)
# async def mute(client, message):
#     await message.delete()
#     # Parse the time duration from the command
#     try:
#         duration_str = re.search(r'(\d+)([dhma])', message.command[1]).groups()
#         duration_num = int(duration_str[0])
#         duration_unit = duration_str[1]

#         if duration_unit == 'm':
#             duration = timedelta(minutes=duration_num)
#         elif duration_unit == 'h':
#             duration = timedelta(hours=duration_num)
#         elif duration_unit == 'd':
#             duration = timedelta(days=duration_num)
#         elif duration_unit == 'a':
#             duration = timedelta(days=365 * duration_num)
#     except (IndexError, AttributeError):
#         await client.send_message(chat_id=message.chat.id, text="Lütfen bir zaman periyodu belirtin. Örneğin: `.mute 4h`")
#         return

#     # Apply the mute
#     await client.restrict_chat_member(
#         chat_id=message.chat.id,
#         user_id=message.reply_to_message.from_user.id,
#         permissions=ChatPermissions(),
#         until_date=datetime.now() + duration
#     )

#         # Send a message to confirm the mute
#     duration_str = re.search(r'(\d+[dhma])+', message.command[1]).group()
#     await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} {duration_str} boyunca mutelendi.")

    
        




from pyrogram.errors import UserAdminInvalid

@bot.on_message(filters.command('mute') & filters.group)
async def mute(client, message):
    await message.delete()

    # Check if the user trying to mute is an administrator
    user = await client.get_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    if user.status == "administrator":
        await client.send_message(chat_id=message.chat.id, text="Bir yöneticiyi muteleyemem.")
        return

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
    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(),
            until_date=datetime.now() + duration
        )

        # Send a message to confirm the mute
        duration_str = re.search(r'(\d+[dhma])+', message.command[1]).group()
        await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} {duration_str} boyunca mutelendi.")
    except UserAdminInvalid:
        await client.send_message(chat_id=message.chat.id, text="Bir yöneticiyi mutelemeye çalışıyorsunuz.")










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



# mute_count = {}

# async def process_message(client, message):
#     word_list = [
#         "aq",
#         "amk",
#         "amq",
#         "amcık",
#         "yarrak",
#         "sik",
#         "daşşak",
#         "amcık",
#         "sikerim",
#         "yavşak",
#         "sikik",
#         "gevşek",
#         "orospu",
#         "oruspu",
#         "piç",
#         "kavat",
#         "gavat",
#         "amcık ağızlı",
#         "sevişmek",
#         "sokuşmak"
#     ]
#     user_id = message.from_user.id
#     lower_text = message.text.lower()  # Mesajdaki kelimeyi küçük harflere dönüştür
#     if lower_text in word_list:
#         if user_id in mute_count:
#             mute_count[user_id] += 1
#             remaining_attempts = 5 - mute_count[user_id]
#             if remaining_attempts > 0:
#                 delete_message = await message.reply_text(
#                     f"{message.from_user.mention} {remaining_attempts} daha fazla uyarı alırsanız mute yiyeceksiniz!"
#                 )
#                 await asyncio.sleep(2)  # 2 saniye bekle
#                 await message.delete()  # Mesajı sil
#                 await delete_message.delete()  # Uyarı mesajını sil
                
#             if mute_count[user_id] >= 5:
#                 message_copy = message.copy()
#                 await mute_user(client, message_copy)
                
#         else:
#             mute_count[user_id] = 1

# @bot.on_message(filters.text & filters.group)
# async def delete_text(client, message):
#     await process_message(client, message)

# async def mute_user(client, message):
#     user_id = message.from_user.id
#     duration = timedelta(minutes=10)
    
#     await client.restrict_chat_member(
#         chat_id=message.chat.id,
#         user_id=user_id,
#         permissions=ChatPermissions(),
#         until_date=datetime.now() + duration
#     )
    
#     await message.reply_text(
#         f"{message.from_user.mention} 10 dakika boyunca mutelendi."
#     )
    
#     mute_count[user_id] = 0 
#     await message.delete()  # Mesajı sil

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
    
    user = await client.get_chat_member(chat_id=message.chat.id, user_id=user_id)
    if lower_text in word_list:
        if user.status != "administrator":
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
                    await mute_user(client, message)
            else:
                mute_count[user_id] = 1
                await message.delete()  # Mesajı silmek için delete() kullanın
        else:
            await message.reply_text(
                "Üzgünüm, yönetici üyeler bu tür kelimeleri kullanabilir."
            )

@bot.on_message(filters.text & filters.group)
async def delete_text(client, message):
    await process_message(client, message)

async def mute_user(client, message):
    user_id = message.from_user.id
    duration = timedelta(minutes=10)

    try:
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
        await message.delete()  # Mesajı silmek için delete() kullanın

    except errors.exceptions.bad_request_400.UserAdminInvalid:
        await message.reply_text(
            "Üzgünüm, bir yöneticiyi muteleyemem. Ama bu düzgün kelimleri kullanmayacağı anlamına gelmez. Lütfen düzgün kelimler kullanın."
        )


print("I AM ALIVE")


bot.run()