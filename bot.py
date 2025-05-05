import requests
import datetime
import os

TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Exam date
exam_date = datetime.datetime(2025, 10, 10)
today = datetime.datetime.today()
days_left = (exam_date - today).days

message = f"2025 A/L ට දිනයන් {days_left}යි! 📚💪📢\n\n\n\n\n අද දිනය: {today.strftime('%Y-%m-%d')}"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {'chat_id': CHAT_ID, 'text': message}

response = requests.post(url, data=payload)
print(response.text)
