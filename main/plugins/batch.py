import time
import asyncio
import random  # Import the random module
import logging

from .. import bot as Drone, userbot, Bot, AUTH, FORCESUB as fs
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link
from telethon import events, Button
from pyrogram.errors import FloodWait
from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."
batch = []

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/cancel'))
async def cancel(event):
    if event.sender_id not in batch:
        return await event.reply("No batch active.")
    batch.clear()
    await event.reply("Done.")

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s:
        await event.reply(r)
        return
    if event.sender_id in batch:
        return await event.reply("You've already started one batch, wait for it to complete!")

    async with Drone.conversation(event.chat_id) as conv:
        await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
        try:
            link = await conv.get_reply()
            _link = get_link(link.text)
        except Exception as e:
            await conv.send_message(f"Error: {e}")
            return await conv.cancel()

        await conv.send_message("Send me the number of files/range you want to save from the given message, as a reply to this message.", buttons=Button.force_reply())
        try:
            _range = await conv.get_reply()
            value = int(_range.text)
            if value > 10000:
                await conv.send_message("You can only get up to 10000 files in a single batch.")
                return await conv.cancel()
        except ValueError:
            await conv.send_message("Range must be an integer!")
            return await conv.cancel()
        except Exception as e:
            await conv.send_message(f"Error: {e}")
            return await conv.cancel()

        batch.append(event.sender_id)
        await run_batch(userbot, Bot, event.sender_id, _link, value)
        await conv.cancel()
        batch.clear()

def parse_message_id_from_link(link):
    try:
        # Assuming the link format is https://t.me/c/1635107642/6
        parts = link.split('/')
        message_id = int(parts[-1])
        chat_id = -1001635107642
        return chat_id, message_id
    except (ValueError, IndexError) as e:
        logger.error(f"Error parsing message ID from link '{link}': {e}")
        raise ValueError("Invalid message link")

async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = random.uniform(2, 10)
        elif i < 100:
            timer = random.uniform(5, 15)
        elif i < 200:
            timer = random.uniform(25, 35)
        elif i < 300:
            timer = random.uniform(10, 20)
        elif i < 400:
            timer = random.uniform(30, 45)
        elif i < 500:
            timer = random.uniform(22, 28)
        elif i < 600:
            timer = random.uniform(2, 10)
        elif i < 700:
            timer = random.uniform(25, 40)
        elif i < 800:
            timer = random.uniform(15, 20)
        elif i < 900:
            timer = random.uniform(45, 60)
        elif i < 1000:
            timer = random.uniform(5, 12)
        else:
            timer = random.uniform(2, 60)

        if 't.me/c/' not in link:
            timer = 2 if i < 25 else 3

        try:
            if sender not in batch:
                await client.send_message(sender, "Batch completed.")
                break
        except Exception as e:
            logger.error(f"Error during batch completion check: {e}")
            await client.send_message(sender, "Batch completed.")
            break

        try:
            chat_id, message_id = parse_message_id_from_link(link)
            await get_bulk_msg(userbot, client, sender, chat_id, message_id + i)
        except FloodWait as fw:
            if int(fw.value) > 300:  # 300 seconds = 5 minutes
                await client.send_message(sender, "Cancelling batch since you have a floodwait more than 5 minutes.")
                break
            await asyncio.sleep(fw.value + random.uniform(5, 60))
            await get_bulk_msg(userbot, client, sender, chat_id, message_id + i)

        protection = await client.send_message(sender, f"Sleeping for `{timer:.2f}` seconds to avoid Floodwaits and protect account!")
        await asyncio.sleep(timer)
        await protection.delete()

