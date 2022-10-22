from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Обратно в меню', callback_data='btn5')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

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


inline_btn_0 = InlineKeyboardButton('⚙️ Сделать заказ', callback_data='btn0')

# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_0)

#inline_btn_0_1 = InlineKeyboardButton('📖Мои заказы', callback_data='btn0_1')
#inline_kb_full.add(inline_btn_0_1)

inline_btn_3 = InlineKeyboardButton('✏️ Отзывы', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('☎️ Контакты', callback_data='btn4')


inline_kb_full.add(inline_btn_3, inline_btn_4)

# inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
# inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))