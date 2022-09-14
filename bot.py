from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
import keyboards as kb
import datetime
import sqlite3


# conn = sqlite3.connect('data.db')
# cur = conn.cursor()
# cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}", "@{message.from_user.username}")')
# conn.commit()



bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

o = []

class Form(StatesGroup):
    admin_login = State()
    admin = State()
    order = State()
    deleting = State()
    

@dp.callback_query_handler(text_startswith='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    print(code)

    if code.isdigit():
        code = int(code)
    if code == 0:
        await bot.send_message(callback_query.from_user.id, "Дайте точное описание вашему заказу, обязательно укажите желаемую стоимость проекта и дедлайн, при необходимости свяжитесь с администратором", reply_markup=kb.greet_kb1)
        await Form.order.set()
    if code == 1:
        try:
            conn = sqlite3.connect('accounts.db')
            cur = conn.cursor()
            cur.execute(f'SELECT "order" FROM users WHERE user_id = "{callback_query.from_user.id}"')
            result_bd = cur.fetchall()
            if result_bd == []:
                await bot.send_message(callback_query.from_user.id, "Ваш список заказов пуст")
            else:
                await bot.send_message(callback_query.from_user.id, '\n\n'.join(''.join(elems) for elems in result_bd))
            
        except Exception as e:
            print(e)
            await bot.send_message('1017470547', e)

        
    if code == 4:
        await bot.send_message(callback_query.from_user.id, "Связаться напрямую -> @rolex0nmywrist")
        
    if code == 3:
        await bot.send_message(callback_query.from_user.id, "https://lolz.guru/threads/3933835/")



@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=kb.inline_kb_full)


@dp.message_handler(commands=['admin'])
async def adminka(message: types.Message):
    await message.answer('Обезьяна')
    await Form.admin_login.set()

@dp.message_handler(commands=['delete'])
async def adminka(message: types.Message):
    await Form.deleting.set()



@dp.message_handler(Text(equals="Обратно в меню"))

async def menu(message: types.Message):
    await message.answer("Меню", reply_markup=kb.inline_kb_full)


@dp.message_handler(state=Form.deleting)
async def process_delete(message: types.Message, state: FSMContext):
    try:
        global o
        numder = message.text
        for i in range(int(numder)):
            del o[0]
        await message.answer('Заказы успешно удалены')
        await state.finish()

    except:
        await message.answer('Неверный формат данных')
        await state.finish()





@dp.message_handler(state=Form.admin_login)
async def process_name(message: types.Message, state: FSMContext):
    
    
    password = message.text
    print(password)
    
    if password != 'admin':
        await message.answer('Долбаеб, ты печатать не умеешь')
        return
    await Form.admin.set()

        

@dp.message_handler(state=Form.admin)
async def process_name_admin(message: types.Message, state: FSMContext):
    print('хуй')
    global o
    orders = ''
    for i in o:
        orders += '{} ----> {}'.format(i[0], i[1])
        orders += '\n'
    try:
        print('lol')
        await message.answer(orders)
    except:
        await message.answer('Пусто, хуйланище')

    await state.finish()


@dp.message_handler(state=Form.order)
async def ordering(message: types.Message, state: FSMContext):

    global o
    async with state.proxy() as data:
        ordr = message.text
        
        if 'Обратно в меню' in ordr:
            await message.answer('Меню', reply_markup=kb.inline_kb_full)
            await state.finish()

        elif len(ordr.split()) < 10:
            await message.answer('Слишком короткое тз, распишите подробнее')
            
           

        elif len(ordr.split()) >= 10:
            data['order'] = ordr
            await message.answer('Ваш заказ принят. Ожидайте, в ближайшее время с вами свяжутся',
                                 reply_markup=kb.inline_kb_full)
            ind = len(o) + 1
            username = message.from_user.username
            now = datetime.datetime.now()
            try:
                info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + '@' + username
            except:
                chat_id = message.chat.id
                button_url = f'tg://openmessage?user_id={chat_id}'
                info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + button_url

            o.append([info, data['order']])
            try:
                conn = sqlite3.connect('accounts.db')
                cur = conn.cursor()
                cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}", "{ordr}")')
                conn.commit()
            except Exception as e:
                print(e)
                await bot.send_message('1017470547', e)
            
            await state.finish()
           

            
            
            #await bot.send_message('2115781605', '{} - {}'.format(o[-1][0], o[-1][1]))
        



# @dp.callback_query_handler(text="back_menu")
# async def call_main_menu(call: CallbackQuery):
#     await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


# @dp.message_handler(commands=['hi6'])
# async def process_hi6_command(message: types.Message):
#     await message.reply("Шестое - запрашиваем контакт и геолокацию\n"
#                         "Эти две кнопки не зависят друг от друга",
#                         reply_markup=kb.markup_request)






if __name__ == '__main__':
    executor.start_polling(dp)