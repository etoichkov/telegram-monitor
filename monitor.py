import asyncio
import unicodedata
from telethon import TelegramClient, events

# Tus credenciales de Telegram
api_id = 31566646
api_hash = "ab2f5f3d41c1df52515c7f95edd4b74e"

# Palabras que quieres detectar
palabras_clave = [
    "calendario electronico"
]

# Crear cliente
client = TelegramClient("monitor", api_id, api_hash)


# Función para normalizar texto (quitar acentos y pasar a minúsculas)
def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto


@client.on(events.NewMessage)
async def handler(event):

    if not event.raw_text:
        return

    texto = normalizar(event.raw_text)

    for palabra in palabras_clave:
        if palabra in texto:

            print("🔔 Palabra detectada")

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
