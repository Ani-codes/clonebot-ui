
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Buttons used

home_button = [
    [InlineKeyboardButton("source", "source_btn"),
     InlineKeyboardButton("Fr. Id", "from_btn"),
     InlineKeyboardButton("Help", url="https://telegra.ph/Clonebot-UI-Help-05-30")],
    [InlineKeyboardButton("Target", "target_btn"),
     InlineKeyboardButton("To Id", "up_to_btn"),
     InlineKeyboardButton("Type ", "types_btn")],
    [InlineKeyboardButton("Delayed", "delay_btn"),
     InlineKeyboardButton("Caption", "caption_btn"),
     InlineKeyboardButton("FNAC", "f_caption_btn")],
    [InlineKeyboardButton("View", "view_btn"),
     InlineKeyboardButton("Reset", "rst_btn"),
     InlineKeyboardButton("Close", "close_btn")],
    [InlineKeyboardButton("📂 Clone Medias 📂", "clone_btn")]
]


start_button = [
    [InlineKeyboardButton("GitHub", url="github.com/m4mallu/clonebot-ui"),
     InlineKeyboardButton("Settings", "start_btn")]
]


types_button = [
    [InlineKeyboardButton(" Docs", "docs_btn"),
     InlineKeyboardButton(" Video", "video_btn"),
     InlineKeyboardButton(" Audio", "audio_btn")],
    [InlineKeyboardButton(" Photo", "photo_btn"),
     InlineKeyboardButton(" Voice", "voice_btn"),
     InlineKeyboardButton(" View", "view_types")],
    [InlineKeyboardButton(" Back", "start_btn")]
]


stop_button = [
    [InlineKeyboardButton("🚫 STOP 🚫", "stop_clone")]
]


finished_button = [
    [InlineKeyboardButton("HOME", "start_btn"),
     InlineKeyboardButton("CLOSE", "close_btn")]
]


terminate_btn = [
    [InlineKeyboardButton("Updates", url="https://github.com/m4mallu/clonebot-ui"),
     InlineKeyboardButton("Usage", url="https://telegra.ph/Clonebot-UI-Help-05-30")],
    [InlineKeyboardButton("Terminate", "terminate_btn"),
     InlineKeyboardButton("Home", "start_btn")]
]


# markups used

reply_markup_stop = InlineKeyboardMarkup(stop_button)

reply_markup_home = InlineKeyboardMarkup(home_button)

reply_markup_start = InlineKeyboardMarkup(start_button)

reply_markup_terminate = InlineKeyboardMarkup(terminate_btn)

reply_markup_finished = InlineKeyboardMarkup(finished_button)

reply_markup_types_button = InlineKeyboardMarkup(types_button)
