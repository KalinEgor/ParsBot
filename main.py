#bot_token = '6154259586:AAFlD8A_CssEPn3srFbVF0xO0A3eq9--9qs'
#api_hash = 'd57c7b210ab654a50b5f760807db7d43'
#api_id = '28749707'

import os
from telethon import TelegramClient, events

from telethon import functions, types

api_hash = os.environ['api_hash']
api_id = int(os.environ['api_id'])
bot_token = os.environ['bot_token']
bot = TelegramClient('user', api_id, api_hash)
bot.start()

# обработка команд бота
@bot.on(events.NewMessage(pattern='/pars'))
async def handler(event):
    # получение списка пользователей канала
    channel_username = 'mnogosdelal'
    channel_entity = await bot.get_entity('https://t.me/'+channel_username)
    participants = await bot.get_participants(channel_entity)
    # сохранение информации о пользователях в базу данных
    for participant in participants:
        print(participant.id, participant.phone, participant.first_name, participant.last_name, participant.username)

@bot.on(events.NewMessage(pattern='/parsi'))
async def handler(event):
    chat = await bot.get_entity('https://t.me/mnogosdelal')
    async for message in bot.iter_messages(chat):
        print(message.id, message.text)
@bot.on(events.NewMessage(pattern='/example'))
async def example(event):
    async for dialog in bot.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

def main():
    bot.run_until_disconnected()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


