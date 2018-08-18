import uuid
import telebot
import random
import PIL
from PIL import Image
from telebot import types


files = {}
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
token = "623719715:AAGp0aUDPWpvvrNjunn00c0jmig_vp81_zU"
bot = telebot.TeleBot(token=token)
def process1(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    i = (img.width)
    j = (img.height)
    yakov = Image.open('yakov.png')
    yakov = yakov.resize(img.size)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 2, j // 2), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 4, j // 4), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 8, j // 8), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 16, j // 16), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 32, j // 32), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 64, j // 64), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    img.save(files[user])
def process2(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
                pixels = img.load()
                r, g, b = pixels[i, j]
                z = (r + g + b) // 3
                if z > 100:
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0
                pixels[i, j] = r, g, b
        img.save(files[user])
def process3(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
            pixels = img.load()
            r, g, b = pixels[i, j]
            r, g, b = b, r, g
            pixels[i, j] = r, g, b
    img.save(files[user])
def process4(message):
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
            pixels = img.load()
            r, g, b = pixels[i, j]
            z = (r + g + b) // 3
            if z > 100:
                r, g, b = r + 20, g, b
            if z > 140:
                r, g, b = r + 45, g, b
            if z > 100:
                r, g, b = r, g + 30, b
            else:
                r, g, b = r + 80, g - 90, b + 120
            pixels[i, j] = r, g, b

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_id = message.chat.id
    user = message.chat.id
    bot.send_message(user, 'Скинь фото!')
    bot.send_photo(user, "https://wallpapertag.com/wallpaper/full/b/a/e/647146-free-2pac-wallpapers-1920x1200.jpg")
@bot.message_handler(content_types=['photo'])
def photo(message):
    keyboard = types.InlineKeyboardMarkup()
    user = message.chat.id
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file( path.file_path )
    extn = '.' + str( path.file_path ).split( '.' )[-1]
    pikcha = 'images/' + str( uuid.uuid4() ) + extn
    with open( pikcha, 'wb' ) as new_file:
        new_file.write( downloaded_file )
    files[user] = pikcha
    button1 = types.InlineKeyboardButton( text='Фильтр Якова', callback_data="button1" )
    button2 = types.InlineKeyboardButton( text='Шум', callback_data="button2" )
    button3 = types.InlineKeyboardButton( text='Наркотики', callback_data="button3" )
    button4 = types.InlineKeyboardButton( text='Диэтиламид-лизергиновая кислота', callback_data='button4' )
    keyboard.add( button1 )
    keyboard.add( button2 )
    keyboard.add( button3 )
    keyboard.add( button4 )
    bot.send_message( user, 'Пожалуйста выберите фильтр', reply_markup=keyboard )


@bot.callback_query_handler( func=lambda call: True )
def photoo(call):
    user = call.message.chat.id
    if call.message:
        if call.data == 'button1':
            process1( call.message )
        if call.data == 'button2':
            process2( call.message )
        if call.data == 'button3':
            process3( call.message )
        if call.data == 'button4':
            process4( call.message )
        with open( files[user], 'rb' ) as new_file:
            bot.send_photo( user, new_file.read() )
bot.polling( none_stop=True )