import os

import asyncio
import time

from telethon import TelegramClient, events


API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

assert(API_ID, "API_ID must be set")
assert(API_HASH, "API_HASH must be set")

ignored_user_ids = [372150322]

message = "Привет! Я либо сплю, либо работаю, если что-то серьезное, то лучше звони!"
timeout_time = 10 * 60

def main():
    client = TelegramClient("tele_session", API_ID, API_HASH)
    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        sender_id = event.message.from_id.user_id
        if sender_id not in ignored_user_ids:
            print(time.asctime(), '-', event.message)
            time.sleep(timeout_time)
            await event.reply(message)
    
    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')

if __name__ == "__main__":
    main()