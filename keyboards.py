from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


#button_hi = KeyboardButton('Обратно в меню', callback_data='btn5')
#button_hi = KeyboardButton('Switch to English', callback_data='btn6')

greet_kb = ReplyKeyboardMarkup()
#greet_kb.add(button_hi)

#greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

#greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)




# markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
# ).add(
#     KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
# )

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))

inline_btn_lang_ru = InlineKeyboardButton('Switch language to 🇺🇸', callback_data='btn_lang_ru')
inline_btn_0 = InlineKeyboardButton('⚙️ Сделать заказ', callback_data='btn0')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_lang_ru)
inline_kb_full.add(inline_btn_0)
inline_btn_0_1 = InlineKeyboardButton('📖 Мои заказы', callback_data='btn1')
inline_kb_full.add(inline_btn_0_1)
inline_btn_3 = InlineKeyboardButton('✏️ Отзывы', callback_data='btn2')
inline_btn_4 = InlineKeyboardButton('☎️ Контакты', callback_data='btn3')
inline_kb_full.add(inline_btn_3, inline_btn_4)



inline_btn_lang_en = InlineKeyboardButton('Поменять язык на 🇷🇺', callback_data='btn_lang_en')
inline_btn_0_en = InlineKeyboardButton('⚙️ Make an order', callback_data='btn0_en')

inline_kb_full_en = InlineKeyboardMarkup(row_width=2).add(inline_btn_lang_en)
inline_kb_full_en.add(inline_btn_0_en)
inline_btn_0_1_en = InlineKeyboardButton('📖 My orders', callback_data='btn1_en')
inline_kb_full_en.add(inline_btn_0_1_en)
inline_btn_3_en = InlineKeyboardButton('✏️ Reviews', callback_data='btn2_en')
inline_btn_4_en = InlineKeyboardButton('☎️ Contacts', callback_data='btn3_en')
inline_kb_full_en.add(inline_btn_3_en, inline_btn_4_en)
