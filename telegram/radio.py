import asyncio
import ffmpeg

from pyrogram import Client, filters, idle
from pytgcalls import GroupCall

"""
Modified to run standalone from MarshalX tgcall's smart plugin
https://github.com/MarshalX/tgcalls/blob/main/examples/radio_as_smart_plugin.py

Note: .raw file will grow over time, if radio has to run indefinetly: 
modify script to stop radio, delete .raw and restart every x hours
"""

API_ID = 1234
API_HASH = ""
CHAT_ID = ""
stream_url = ""
raw_file = "radio.raw"


async def main(client):
    await client.start()
    while not client.is_connected:
        await asyncio.sleep(1)

    group_call = GroupCall(client, raw_file, path_to_log_file='')
    await group_call.start(CHAT_ID)

    ffmpeg.input(stream_url).output(
        raw_file,
        format='s16le',
        acodec='pcm_s16le',
        ac=2,
        ar='48k'
    ).overwrite_output().run_async()

    await idle()

if __name__ == '__main__':
    app = Client(
        "AtomTGCall",
        api_id=API_ID,
        api_hash=API_HASH
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(app))
