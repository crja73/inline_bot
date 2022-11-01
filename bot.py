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
# import sqlite3


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
    # deleting = State()
    date = State()
    price = State()
    lzt_link = State()
    

@dp.callback_query_handler(text_startswith='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    
    if code.isdigit():
        code = int(code)
        print(code)
    if code == 0:
        await bot.send_message(callback_query.from_user.id, "🕓Введите желаемый срок выполнения зказа", reply_markup=kb.greet_kb1)
        await Form.date.set()
    if code == 1:
        try:
            username = callback_query.from_user.username
            f = open('orders01.txt', 'r')
            f_m = ''.join(f.readlines())
            f_spis = f_m.split('------')
            print(f_spis)
            if f_spis != ['']:

                for h in f_spis:
                    if username in h:
                        await bot.send_message(callback_query.from_user.id, h)
            else:
                await bot.send_message(callback_query.from_user.id, "❌У вас еще не было заказов")

    #        conn = sqlite3.connect('accounts.db')
    #         cur = conn.cursor()
    #         cur.execute(f'SELECT "order", "status", "comments" FROM users WHERE user_id = "{callback_query.from_user.id}"')
    #         result_bd = cur.fetchall()
    #         if result_bd == []:
    #             await bot.send_message(callback_query.from_user.id, "❌Ваш список заказов пуст")
    #         else:
    #             for i in range(len(result_bd)):
    #                 print(result_bd)
    #                 new = ''.join(result_bd[i][0])
    #                 new_2 = new.split(', ')
    #                 stat = ' ' + result_bd[i][1]
    #                 comm = result_bd[i][2]

                    
    #                 await bot.send_message(callback_query.from_user.id, '№{}   {}'.format(i + 1, '\n\n'.join(new_2) + '\n\n' + '♻️Статус: ' + stat + '\n\n' + '📝Комментарии: ' + comm))
                          
           
            #     await bot.send_message(callback_query.from_user.id, '\n\n\n'.join('🔸' + ''.join(elems) for elems in result_bd))
            
        except Exception as e:
            print(e)
            await bot.send_message('1017470547', e)

        
    if code == 4:
        await bot.send_message(callback_query.from_user.id, "📞Связаться напрямую -> @rolex0nmywrist")
        
    if code == 3:
        await bot.send_message(callback_query.from_user.id, "https://lolz.guru/threads/3933835/")
    if code == 5:
        await bot.send_message(message.from_user.id, "Меню", reply_markup=kb.inline_kb_full)



@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "🤟Добро пожаловать", reply_markup=kb.inline_kb_full)


@dp.message_handler(commands=['killniggers'])
async def adminka(message: types.Message):
    await Form.admin_login.set()

# @dp.message_handler(commands=['delete'])
# async def adminka(message: types.Message):
#     await message.answer('Укажите номер заказа')
#     await Form.deleting.set()


@dp.message_handler(Text(equals="⬅️Обратно в меню"))

async def menu(message: types.Message):
    await message.answer("Меню", reply_markup=kb.inline_kb_full)


# @dp.message_handler(state=Form.deleting)
# async def process_delete(message: types.Message, state: FSMContext):
#     #try:
#     #await message.answer('лоллич')
#     conn = sqlite3.connect('accounts.db')
#     cur = conn.cursor()
#     print(message.text)
#     cur.execute(f'DELETE FROM users WHERE user_id = "1017470547"')
#     conn.commit()
#     await state.finish()

    # except:
    #     await message.answer('Неверный формат данных')
    #     await state.finish()





@dp.message_handler(state=Form.admin_login)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    
        password = message.text
        data['password'] = password
        if password != 'admin':
            await message.answer('Долбаеб, ты печатать не умеешь')
            return

        f = open('orders01.txt', 'r')
        try:
            f_l = ''.join(f.readlines())
            await message.answer(f_l)
            
        except:
            await message.answer('Список заказов пуст')
        await state.finish()


        

# @dp.message_handler(state=Form.admin)
# async def process_name_admin(message: types.Message, state: FSMContext):
#     f = open('orders01.txt', 'r')
#     f_l = ''.join(f.readlines())
#     await message.answer(f_l)
    
#     # print('хуй')
#     # conn = sqlite3.connect('accounts.db')
#     # cur = conn.cursor()
#     # cur.execute(f'SELECT "order", "status", "comments" FROM users')
#     # result_bd = cur.fetchall()
#     # if result_bd == []:
#     #     await bot.send_message(callback_query.from_user.id, "❌Ваш список заказов пуст")
#     # else:
#     #     for i in range(len(result_bd)):
#     #         print(result_bd)
#     #         new = ''.join(result_bd[i][0])
#     #         new_2 = new.split(', ')
#     #         stat = ' ' + result_bd[i][1]
#     #         comm = result_bd[i][2]       
#     #         await message.answer('№{}   {}'.format(i + 1, '\n\n'.join(new_2) + '\n\n' + '♻️Статус: ' + stat + '\n\n' + '📝Комментарии: ' + comm))

#     await state.finish()


@dp.message_handler(state=Form.date)
async def process_date(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['date'] = message.text
            print(data['date'])
            if data['date'] == 'Обратно в меню':
                await message.answer('Меню', reply_markup=kb.inline_kb_full)
                await state.finish()
            else:
                await message.answer('💰Введите бюджет')
                await Form.price.set()
    except Exception as e:
        await bot.send_message('1017470547', e)



@dp.message_handler(state=Form.price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            
            data['price'] = message.text
            print(data['price'])
            if data['price'] == 'Обратно в меню':
                await message.answer('Меню', reply_markup=kb.inline_kb_full)
                await state.finish()
            else:
                await message.answer('Укажите ваш профиль на Lolz.guru, если его нет, то потсавьте -')
                await Form.lzt_link.set()
    except Exception as e:
        await bot.send_message('1017470547', e)

@dp.message_handler(state=Form.lzt_link)
async def process_lzt(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            
            data['lolz'] = message.text
            print(data['lolz'])
            if data['lolz'] == 'Обратно в меню':
                await message.answer('Меню', reply_markup=kb.inline_kb_full)
                await state.finish()
            else:

                await message.answer('✍️Подробно опишите ваш заказ')
                await Form.order.set()
    except Exception as e:
        await bot.send_message('1017470547', e)



@dp.message_handler(state=Form.order)
async def ordering(message: types.Message, state: FSMContext):
    try:

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
                await message.answer('✅ Ваш заказ принят. Ожидайте, в ближайшее время с вами свяжутся',
                                     reply_markup=kb.inline_kb_full)
                ind = len(o) + 1
                
                now = datetime.datetime.now()
                try:
                    username = message.from_user.username
                    info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + '@' + username
                except:
                    chat_id = message.chat.id
                    button_url = f'tg://openmessage?user_id={chat_id}'
                    info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + button_url

                try:
                    name = message.from_user.username
                except:
                    name = message.from_user.url

                full_order = 'Дата и время:  {}👤 Пользователь:  {}\n⏱  Срок:  {}\n💰  Бюджет:  {}\nСсылка на Lolz:  {}\n🗒  ТЗ:  '.format(str(now.strftime("%d.%m.%Y %H:%M")), name, data['date'], data['price'], data['lolz']) + data['order']
                o.append([info, full_order])
                await bot.send_message('1017470547', full_order)
                await bot.send_message('2115781605', full_order)
                full_order2 = 'Пользователь:  {}\nСрок:  {}\nБюджет:  {}\nСсылка на Lolz:  {}\nТЗ:  '.format(name, data['date'], data['price'], data['lolz']) + data['order']
                f = open('orders01.txt', 'a')
                f.write(full_order2 + '\n')
                f.write("------"+'\n')
    except Exception as e:
        full_order = 'Дата и время:  {}👤 Пользователь:  {}\n⏱  Срок:  {}\n💰  Бюджет:  {}\nСсылка на Lolz:  {}\n🗒  ТЗ:  '.format(str(now.strftime("%d.%m.%Y %H:%M")), name, data['date'], data['price'], data['lolz']) + data['order']
        o.append([info, full_order])
        await bot.send_message('1017470547', full_order)
        full_order2 = 'Пользователь:  {}\nСрок:  {}\nБюджет:  {}\nСсылка на Lolz:  {}\nТЗ:  '.format(name, data['date'], data['price'], data['lolz']) + data['order']
        f = open('orders01.txt', 'a')
        f.write(full_order2 + '\n')
        f.write("------"+'\n')
        await bot.send_message('1017470547', e)
    await state.finish()
                
            # try:
            #     conn = sqlite3.connect('accounts.db')
            #     cur = conn.cursor()
            #     processing = 'В обработке'
            #     comment = 'нет'
            #     cur.execute(f'INSERT INTO users VALUES("{message.from_user.id}", "{full_order}", "{processing}", "{comment}")')
            #     conn.commit()
            # except Exception as e:
            #     print(e)
                
            
    
           

            
            
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