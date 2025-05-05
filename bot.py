import os
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

TOKEN = os.getenv('TELEGRAM_TOKEN') or '7880981460:AAGXWRqEm-Qui94rSC0kNCwWzHUTdLbQzLs'
CHAT_ID = os.getenv('CHAT_ID') or '1503038067'

exam_date = datetime(2025, 10, 21)
today = datetime.now()
delta = exam_date - today

months = delta.days // 30
weeks = delta.days // 7
days = delta.days
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60

img = Image.new('RGB', (600, 400), color=(160, 110, 255))
draw = ImageDraw.Draw(img)
font_big = ImageFont.truetype('arial.ttf', 120)
font_small = ImageFont.truetype('arial.ttf', 30)

draw.text((150, 100), f"{days}", font=font_big, fill='white')
draw.text((200, 250), "DAYS LEFT", font=font_small, fill='white')

image_path = 'countdown.png'
img.save(image_path)

message = (
    "🏅 2025 A/L විභාගයට කාලය 📢\n"
    f"මාස: {months}\n"
    f"සති: {weeks}\n"
    f"දින: {days}\n"
    f"පැය: {hours}\n"
    f"මිනිත්තු: {minutes}\n"
    "📅 දිනය: 2025-10-21"
)

with open(image_path, 'rb') as photo:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            'chat_id': CHAT_ID,
            'caption': message
        },
        files={'photo': photo}
    )
