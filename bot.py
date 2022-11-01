# -*- coding: utf-8 -*-
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
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# import sqlite3


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
lang = 'rus'
o = []

class Form(StatesGroup):
    admin_login = State()
    admin = State()
    order = State()
    # deleting = State()
    date = State()
    price = State()
    lzt_link = State()
    social = State()
    urgency = State()
    

@dp.callback_query_handler(text_startswith='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    global lang
    order_list = []
    code = callback_query.data
    print(code)
    if code == 'btn0':
        await bot.send_message(callback_query.from_user.id, "🕓Введите желаемый срок выполнения зказа")
        await Form.date.set()
    if code == 'btn1':
        try:
            
            try:
                username = callback_query.from_user.username
                if username == 'None':
                    username = callback_query.from_user.id
            except:
                username = callback_query.from_user.id

            f = open('orders01.txt', 'r')
            f_m = ''.join(f.readlines())
            f_spis = f_m.split('------')
            print(f_spis)
            if f_spis != ['']:

                for h in f_spis:
                    if username in h:
                        order_list.append(h)
                button_list = [InlineKeyboardButton(text=order_list.index(x) + 1, callback_data=f'order_{order_list.index(x) + 1}') for x in order_list]
                orders_kb = InlineKeyboardMarkup(row_width=1).add(*button_list)
                await bot.send_message(callback_query.from_user.id, 'Все ваши заказы:', reply_markup=orders_kb)
                

            else:
                await bot.send_message(callback_query.from_user.id, "❌У вас еще не было заказов")
                
            await bot.send_message(callback_query.from_user.id, "Меню", reply_markup=kb.inline_kb_full)

            
        except Exception as e:
            print(e)
            await bot.send_message('1017470547', e)

        
    if code == 'btn3':
        await bot.send_message(callback_query.from_user.id, "📞Связаться напрямую -> t.me/use_digital")
        
    if code == 'btn2':
        await bot.send_message(callback_query.from_user.id, "t.me/studio_digital")
    # if code == 'btn5':
    #     if lang == 'rus':
    #         await bot.send_message(callback_query.from_user.id, "Меню", reply_markup=kb.inline_kb_full)
    #     else:
    #         await bot.send_message(callback_query.from_user.id, "Menu", reply_markup=kb.inline_kb_full_en)

    if code == 'btn_lang_ru':
        await bot.send_message(callback_query.from_user.id, "Menu", reply_markup=kb.inline_kb_full_en)
        lang = 'eng'

    if code == 'btn0_en':
        await bot.send_message(callback_query.from_user.id, "🕓 Enter the desired lead time")
        await Form.date.set()
    if code == 'btn1_en':
        try:
            try:
                username = callback_query.from_user.username
                if username == 'None':
                    username = callback_query.from_user.id
            except:
                username = callback_query.from_user.id
            f = open('orders01.txt', 'r')
            f_m = ''.join(f.readlines())
            f_spis = f_m.split('------')
            print(f_spis)
            if f_spis != ['']:

                for h in f_spis:
                    if username in h:
                        await bot.send_message(callback_query.from_user.id, h)
            else:
                await bot.send_message(callback_query.from_user.id, "❌You haven't had any orders yet")
                
            await bot.send_message(callback_query.from_user.id, "Menu", reply_markup=kb.inline_kb_full_en)

        except Exception as e:
            print(e)
            await bot.send_message('1017470547', e)

        
    if code == 'btn3_en':
        await bot.send_message(callback_query.from_user.id, "📞Contact us -> t.me/use_digital")
        
    if code == 'btn2_en':
        await bot.send_message(callback_query.from_user.id, "t.me/studio_digital")

    if code == 'btn_lang_en':
        await bot.send_message(callback_query.from_user.id, "Меню", reply_markup=kb.inline_kb_full)
        lang = 'rus'




@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "🤟Добро пожаловать. В данный момент бот находится на стадии разработки и тестирования, в случае некорректной работы бота пишите напрямую -> t.me/use_digital", reply_markup=kb.inline_kb_full)
    global lang
    lang = 'rus'


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



@dp.message_handler(state=Form.date)
async def process_date(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['date'] = message.text
            print(data['date'])
            if data['date'] == 'Обратно в меню':   
                if lang == 'rus':
                    await state.finish()
                    
                else:
                    
                    await message.answer('Menu', reply_markup=kb.inline_kb_full_en)
                    await state.finish()

                
            else:
                if lang == 'rus':
                    await message.answer('💰Введите бюджет')
                else:
                    await message.answer('💰Specify your desired budget')

                
    except Exception as e:
        await bot.send_message('1017470547', e)
    await Form.price.set()



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
                if lang == 'rus':
                    await message.answer('📞 Укажите ссылку на социальную сеть(username) или номер телефона, чтобы исполнитель смог с вами связаться, обсудить детали и передать ваш заказ')
                else:
                    await message.answer('📞 Specify how we can contact you to discuss the terms of the order(link, username)')
                
    except Exception as e:
        await bot.send_message('1017470547', e)
    await Form.lzt_link.set()

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
                if lang == 'rus':

                    await message.answer('❗️ Оцените срочность проекта от 1 до 3')
                else:
                    await message.answer('❗️ Rate the urgency of the project from 1 to 3 points')
                
    except Exception as e:
        await bot.send_message('1017470547', e)
    await Form.urgency.set()

@dp.message_handler(state=Form.urgency)
async def process_lzt(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            
            data['urg'] = message.text
            print(data['urg'])
            if data['urg'] == 'Обратно в меню':
                await message.answer('Меню', reply_markup=kb.inline_kb_full)
                await state.finish()
            else:
                if lang == 'rus':
                    await message.answer('✍️ Подробно опишите ваш заказ')
                else:
                    await message.answer('✍️ Describe your order in detail')
                
    except Exception as e:
        await bot.send_message('1017470547', e)
    await Form.order.set()


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
                if lang == 'rus':
                    await message.answer('Описание проекта должно составлять не менее 10 слов')
                else:
                    await message.answer('Description of the project must be at least 10 words')
                return
                
               

            elif len(ordr.split()) >= 10:
                data['order'] = ordr
                if lang == 'rus':

                    await message.answer('✅ Ваш заказ принят. Ожидайте, в ближайшее время с вами свяжутся', reply_markup=kb.inline_kb_full)
                else:
                    await message.answer('✅ Your order is accepted. Wait, you will be contacted shortly', reply_markup=kb.inline_kb_full_en)

                ind = len(o) + 1
                
                now = datetime.datetime.now()
                try:
                    username = message.from_user.username
                    info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + '@' + username
                except:
                    chat_id = message.chat.id
                    button_url = f'tg://openmessage?user_id={chat_id}'
                    info = str(now.strftime("%d.%m.%Y %H:%M")) + '   ' + button_url

                name = message.from_user.username
                try:
                    if name == 'None':
                        name = message.from_user.id
                except:
                    name = message.from_user.id
                try:
                    
                    if int(data['urg']) == 1:
                        urgen = 'Не срочно'
                        urgen_en = 'Do not rush'
                    elif int(data['urg']) == 2:
                        urgen = 'Средняя срочность'
                        urgen_en = 'Medium urgency'
                    elif int(data['urg']) >= 3:
                        urgen = 'Срочно'
                        urgen_en = 'Urgently'
                    else:
                        urgen = 'Не срочно'
                        urgen_en = 'Do not rush'
                except:
                    urgen = 'Средняя срочность'
                    urgen_en = 'Medium urgency'

                full_order = 'Дата и время:  {}👤 Пользователь:  {}\n⏱  Срок:  {}\n💰  Бюджет:  {}\nСрочность: {}\nПисать сюда->:  {}\n🗒  ТЗ:  '.format(str(now.strftime("%d.%m.%Y %H:%M")), name, data['date'], data['price'], urgen, data['lolz']) + data['order']
                o.append([info, full_order])
                try:
                    await bot.send_message('1017470547', full_order)
                    await bot.send_message('-1001827951943', full_order)
                except Exception as e:
                    await bot.send_message('1017470547', e)
                    await bot.send_message('1017470547', 'Какая то хуйня с чатом, вот заказ:')
                    await bot.send_message('1017470547', full_order)

                if lang == 'rus':
                    full_order2 = 'Пользователь:  {}\nСрок:  {}\nБюджет:  {}\nСрочность: {}\nПисать сюда->:  {}\nТЗ:  '.format(name, data['date'], data['price'], urgen, data['lolz']) + data['order']
                else:
                    full_order2 = 'User:  {}\nDeadline:  {}\nBudget:  {}\nUrgency: {}\nHow do I want to be contated->:  {}\nТЗ:  '.format(name, data['date'], data['price'], urgen_en, data['lolz']) + data['order']
                f = open('orders01.txt', 'a')
                f.write(full_order2 + '\n')
                f.write("------"+'\n')

    except Exception as e:
        try:
                    
            if int(data['urg']) == 1:
                urgen = 'Не срочно'
                urgen_en = 'Do not rush'

            elif int(data['urg']) == 2:
                urgen = 'Средняя срочность'
                urgen_en = 'Medium urgency'
            elif int(data['urg']) >= 3:
                urgen = 'Срочно'
                urgen_en = 'Urgently'
            else:
                urgen = 'Не срочно'
                urgen_en = 'Do not rush'
        except:
            urgen = 'Средняя срочность'
            urgen_en = 'Medium urgency'

        full_order = 'Дата и время:  {}👤 Пользователь:  {}\n⏱  Срок:  {}\n💰  Бюджет:  {}\nСрочность: {}\nПисать сюда->:  {}\n🗒  ТЗ:  '.format(str(now.strftime("%d.%m.%Y %H:%M")), name, data['date'], data['price'], urgen, data['lolz']) + data['order']
        o.append([info, full_order])
        await bot.send_message('1017470547', full_order)
        await bot.send_message('-1001827951943', full_order)
        if lang == 'rus':
            full_order2 = 'Пользователь:  {}\nСрок:  {}\nБюджет:  {}\n Срочность: {}\n Писать сюда->:  {}\nТЗ:  '.format(name, data['date'], data['price'], urgen, data['lolz']) + data['order']
        else:
            full_order2 = 'User:  {}\nDeadline:  {}\nBudget:  {}\nUrgency: {}\nHow do I want to be contated->:  {}\nТЗ:  '.format(name, data['date'], data['price'], urgen_en, data['lolz']) + data['order']
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