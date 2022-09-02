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



bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

o = []

class Form(StatesGroup):
    admin = State()
    order = State()
    

@dp.callback_query_handler(text_startswith='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    print(code)

    if code.isdigit():
        code = int(code)
    if code == 0:
        await bot.send_message(callback_query.from_user.id, "Дайте точное описание вашему заказу, укажите желаемую стоимость проекта и срок, обязательно укажите свой тег telegram через '@', при необходимости свяжитесь с администратором", reply_markup=kb.greet_kb1)
        await Form.order.set()
    if code == 4:
        await bot.send_message(callback_query.from_user.id, "Связаться напрямую -> @rolex0nmywrist")
        
    if code == 3:
        await bot.send_message(callback_query.from_user.id, "https://lolz.guru/threads/3933835/")



@dp.message_handler(commands=['start', 'menu'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Меню", reply_markup=kb.inline_kb_full)


@dp.message_handler(commands=['admin'])
async def adminka(message: types.Message):
    await message.answer('Обезьяна')
    await Form.admin.set()


@dp.message_handler(Text(equals="Обратно в меню"))

async def menu(message: types.Message):
    print('yep')
    await message.answer("Меню", reply_markup=kb.inline_kb_full)





@dp.message_handler(state=Form.admin)
async def process_name(message: types.Message, state: FSMContext):
    
    
    async with state.proxy() as data:
        password = message.text
    if password == 'admin':
        await message.answer(o)
        await Form.next()

@dp.message_handler(state=Form.order)
async def ordering(message: types.Message, state: FSMContext):
    global o
    async with state.proxy() as data:
        ordr = message.text
        
    if len(list(ordr)) > 20:

        ind = len(o) + 1
        o.append([ind, ordr])
        await message.answer('Ваш заказ принят. Ожидайте, в ближайшее время с вами свяжутся')
        await bot.send_message('1017470547', '{} - {}'.format(o[-1][0], o[-1][1]))
    await Form.next()
        



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