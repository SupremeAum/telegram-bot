from telethon import TelegramClient, events
import asyncio
import re

# Конфигурация
api_id = 21030092  # Числовое значение без кавычек
api_hash = 'db28fad31a2fa9e14d78875742d7e5fd'
phone = '+77475682855'

# ID каналов
SOURCE_CHANNEL_ID = 1002395299718  # Без минуса в начале и без кавычек
DESTINATION_CHANNEL_ID = 'tsardumaet'  # Без @ в строковом значении

# Инициализация клиента
client = TelegramClient('session_name', api_id, api_hash)

# Регулярное выражение для поиска ссылок
URL_PATTERN = re.compile(r'https?://\S+|www\.\S+')

# Обработчик новых сообщений
@client.on(events.NewMessage(chats=SOURCE_CHANNEL_ID))
async def forward_message(event):
    message_text = event.message.message  # Получаем текст сообщения
    
    # Проверяем, содержит ли сообщение ссылку
    if URL_PATTERN.search(message_text):
        print("Сообщение содержит ссылку. Пропускаем.")
        return  # Не отправляем сообщение, если найдена ссылка
    
    await client.send_message(DESTINATION_CHANNEL_ID, event.message)

async def main():
    await client.start(phone)
    print("Бот запущен. Пересылка сообщений активирована.")
    await client.run_until_disconnected()

# Запуск бота
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
