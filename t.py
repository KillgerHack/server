# -*- coding:utf-8 -*-
from telethon import TelegramClient
import logging
from telethon import connection
from telethon import events
from telethon import utils
import asyncio
import telethon
from telethon.tl.functions.messages import CheckChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest ,DeletePhotosRequest
from telethon import functions ,types
from telethon.tl.functions.channels import InviteToChannelRequest
from datetime import timedelta
from telethon.tl.functions.account import UpdateUsernameRequest
import json
import random
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetMessagesViewsRequest
import requests


user_id_bot = 1351756990
name_folder = 2

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
	level = logging.INFO)
logger = logging.getLogger(__name__)




admin_list = [1297252420,1473604756,1333166651]

api_id = 2028205

api_hash = '08b1f6b4c9f3aa6fc8115526d0171e1c'

phone_number = '+22545493248'


client = TelegramClient('accounti', api_id, api_hash)
client.start()




@client.on(events.NewMessage(from_users = admin_list))
async def sayHello(event):
	text = event.raw_text
	
	if ("-لفتت" in text):
		start = int(text.split(" ")[-2])
		stop = int(text.split(" ")[-1])
		rand_time = random.randint(start,stop)
		await client.send_message(event.chat_id,f"تا {rand_time} ثانیه دیگه لفت میدم")
		time.sleep(rand_time)
		if "joinchat/" in text:
			links = (text).split(" ")[1]
			link = await client.get_input_entity(links)
			try:
				await client(LeaveChannelRequest(link))
				await event.reply("لفت دادم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")

		elif "@" in text:
			links = (text).split(" ")[1]
			try:
				await client(LeaveChannelRequest(links))
				await event.reply("لفت دادم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")
	
		elif "t.me/" in text and "joinchat" not in text:
			limkss = (text).split(" ")[1]
			links = limkss.split("t.me/")[1]
			try:
				await client(LeaveChannelRequest(links))
				await event.reply("لفت دادم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")
		
		else:
			await client.send_message(event.chat_id,"لینک خراب است")
	
	elif (text == "-پینگ"):
		await client.send_message(event.chat_id,f"ربات‌ آنلاینه {name_folder}")

	elif ("-جوینن" in text):
		start = int(text.split(" ")[-2])
		stop = int(text.split(" ")[-1])
		rand_time = random.randint(start,stop)
		await client.send_message(event.chat_id,f"تا {rand_time} ثانیه دیگه جوین میدم")
		time.sleep(rand_time)
		
		if "joinchat/" in text:
			limkss = (text).split(" ")[1]
			limks = limkss.split("joinchat/")[1]
			try :
				await client(ImportChatInviteRequest(limks))
				await event.reply("جوین شدم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")
			except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
				await event.reply("از قبل داخل گروه / کانال عضو هستم")
			except telethon.errors.rpcerrorlist.ChannelPrivateError:
				await event.reply("کانال خصوصی است یا شما از کانال حذف شده اید")

		elif "@" in text:
			limks = (text).split(" ")[1]
			try:
				await client(JoinChannelRequest(limks))
				await event.reply("جوین شدم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")
			except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
				await event.reply("از قبل داخل گروه / کانال عضو هستم")
			except telethon.errors.rpcerrorlist.ChannelPrivateError:
				await event.reply("کانال خصوصی است یا شما از کانال حذف شده اید")

		elif "t.me/" in text and "joinchat" not in text:
			limkss = (text).split(" ")[1]
			limks = limkss.split("t.me/")[1]


			try:
				await client(JoinChannelRequest(limks))
				await event.reply("جوین شدم")
			except telethon.errors.rpcerrorlist.InviteHashInvalidError:
				await event.reply("لینک خراب است")
			except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
				await event.reply("از قبل داخل گروه / کانال عضو هستم")
			except telethon.errors.rpcerrorlist.ChannelPrivateError:
				await event.reply("کانال خصوصی است یا شما از کانال حذف شده اید")

	elif ("-تنظیم بیو" in text ):
			
			bio = text.split("-تنظیم بیو ")[1]
			await client(UpdateProfileRequest(about=bio))
			await client.send_message(event.chat_id,"بیو شما با موفقیت تغییر کرد")

	elif ( "-تنظیم اسم" in text):
			name = text.split("-تنظیم اسم")[1]
			await client(UpdateProfileRequest(first_name=name))
			await client.send_message(event.chat_id,"نام شما با موفقیت تغییر کرد")
	
	elif ( "-تنظیم نام کاربری" in text):
	
			try:
				username = text.split("-تنظیم نام کاربری ")[1]
				await client(UpdateUsernameRequest(username))
				await client.send_message(event.chat_id,"آیدی با موفقیت تغییر کرد")
			except telethon.errors.rpcerrorlist.UsernameInvalidError:
				await client.send_message(event.chat_id,"آیدی وارد شده اشتباه می باشد\nاگر با @ وارد کرده اید بدون @ وارد کنید")
			except telethon.errors.rpcerrorlist.UsernameOccupiedError:
				await client.send_message(event.chat_id,"آیدی مورد نظر در دسترس نمی باشد\nاحتمال دارد از قبل قفل شده باشد")
			except telethon.errors.rpcerrorlist.FloodWaitError as e:
				await client.send_message(event.chat_id,f"متاسفانه عملایت به ارور برخورد\nمتن ارور:\n{e}")
	
	elif ("-تنظیم پروفایل" in text ):
			await client(DeletePhotosRequest(await client.get_profile_photos(user_id_bot)))
			adress = text.split(" ")[-1]
			img = requests.get(adress).content
			name_image = text.split(".")[-1]
			with open(f'logo.{name_image}','wb')as f:
				f.write(img)
			try:
				await client(UploadProfilePhotoRequest(await client.upload_file(f'logo.{name_image}')))
				await client.send_message(event.chat_id,"پروفایل با موفقیت تنظیم شد")
			except requests.exceptions.MissingSchema:
				await client.send_message(event.chat_id,"لینک وارد شده خراب است")
			except telethon.errors.rpcerrorlist.PhotoExtInvalidError:
				await client.send_message(event.chat_id,"لینک وارد شده خراب است")
		
@client.on(events.NewMessage(from_users = admin_list))
async def ok(event):
    text = event.raw_text
    if ("-لفت" in text ):
        if "joinchat/" in text:
            text = (text).split("-لفت ")[1]
            link = await client.get_input_entity(text)
            try:
                await client(LeaveChannelRequest(link))
                await event.reply("لفت دادم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")

        elif "@" in text:
            text = (text).split("@",1)[1]
            try:
                await client(LeaveChannelRequest(text))
                await event.reply("لفت دادم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")
        elif "t.me/" in text and "joinchat" not in text:
            text = (text).split("t.me/",1)[1]
            try:
                await client(LeaveChannelRequest(text))
                await event.reply("لفت دادم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")
        else:
            await client.send_message(event.chat_id,"لینک خراباست")
		
    elif ("-جوین" in text ):
        if "joinchat/" in text:
            text = (text).split("joinchat/",1)[1]		
            try:
                await client(ImportChatInviteRequest(text))
                await event.reply("جوین شدم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")
        elif "@" in text:
            text = (text).split("@",1)[1]
            try:
                await client(JoinChannelRequest(text))
                await event.reply("جوین شدم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")
        elif "t.me/" in text and "joinchat" not in text:
            text = (text).split("t.me/",1)[1]
            try:
                await client(JoinChannelRequest(text))
                await event.reply("جوین شدم")
            except telethon.errors.rpcerrorlist.InviteHashInvalidError:
                await event.reply("لینک خراب است")
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                await event.reply("از قبل داخل گروه / کانال عضو هستم")

asyncio.get_event_loop().run_forever()
client.run_until_disconnected()
