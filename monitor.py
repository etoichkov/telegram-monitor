import asyncio
from telethon import TelegramClient, events

api_id = 31566646
api_hash = "ab2f5f3d41c1df52515c7f95edd4b74e"
palabra = "calendario electrónico"

client = TelegramClient("monitor", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    texto = event.raw_text.lower()
    if palabra in texto:
        alerta = f"""
🚨 ALERTA

Chat: {event.chat.title if event.chat else "Desconocido"}

Mensaje:
{event.raw_text}
"""
        await client.send_message("me", alerta)

async def main():
    await client.start()
    print("Monitor activo...")
    await client.run_until_disconnected()

asyncio.run(main())