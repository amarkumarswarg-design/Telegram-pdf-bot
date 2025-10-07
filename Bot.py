import telebot
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import os

TOKEN = os.getenv("8243183150:AAGEbglFyjy_vXFSQ364gfMteKfwKfCTWyg")  # Render में environment variable से आएगा
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Text भेजो — मैं PDF बना दूंगा.")

@bot.message_handler(func=lambda msg: True, content_types=['text'])
def txt_to_pdf(m):
    text = m.text
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4
    y = h - 40
    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 14
        if y < 40:
            c.showPage()
            y = h - 40
    c.save()
    buffer.seek(0)
    bot.send_document(m.chat.id, ("converted.pdf", buffer))

bot.polling(none_stop=True)
