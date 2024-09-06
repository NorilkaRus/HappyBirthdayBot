import os
import asyncio
from dotenv import load_dotenv

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb

load_dotenv('.env')
router = Router()

class Quest(StatesGroup):
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()
    answer_4 = State()

# Хэндлер на команду /start
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer_sticker(os.getenv('HELLO_STICKER'))
    await message.answer(os.getenv('HELLO_MESSAGE'), reply_markup=kb.start_quest)


#Запуск квеста
@router.message(F.text == '🎁Начать квест!🎁')
async def quest(message: types.Message, state: FSMContext):
    await state.set_state(Quest.answer_1)
    await message.answer_sticker(os.getenv('STICKER_1'))
    await message.answer(os.getenv('QUEST_1'))


#Вопрос 1
@router.message(Quest.answer_1)
async def question1(message: types.Message, state: FSMContext):
    await state.update_data(answer_1 = message.text.lower().strip().split())
    data = await state.get_data()
    if os.getenv('ANSWER_1') in data['answer_1']:
        await message.answer_sticker(os.getenv('STICKER_2'))
        await message.answer(os.getenv('QUEST_2'))
        await state.set_state(Quest.answer_2)
    else:
        await message.answer(os.getenv('WRONG_ANSWER'))


#Вопрос 2
@router.message(Quest.answer_2)
async def question2(message: types.Message, state: FSMContext):
    await state.update_data(answer_2 = message.text.lower().strip().split())
    data = await state.get_data()
    if os.getenv('ANSWER_2') in data['answer_2']:
        await message.answer_sticker(os.getenv('STICKER_3'))
        await message.answer(os.getenv('QUEST_3'))
        await state.set_state(Quest.answer_3)
    else:
        await message.answer(os.getenv('WRONG_ANSWER'))


#Вопрос 3
@router.message(Quest.answer_3)
async def question2(message: types.Message, state: FSMContext):
    await state.update_data(answer_3 = message.text.lower().strip().split())
    data = await state.get_data()
    if os.getenv('ANSWER_3') in data['answer_3']:
        await message.answer_sticker(os.getenv('STICKER_4'))
        await message.answer(os.getenv('QUEST_4'))
        await state.set_state(Quest.answer_4)
    else:
        await message.answer(os.getenv('WRONG_ANSWER'))


#Вопрос 4
@router.message(Quest.answer_4)
async def question2(message: types.Message, state: FSMContext):
    await state.update_data(answer_4 = message.text.lower().strip().split())
    data = await state.get_data()
    if os.getenv('ANSWER_4') in data['answer_4']:
        await message.answer_sticker(os.getenv('FINISH_STICKER'))
        await message.answer(os.getenv('FINISH_MESSAGE'))
        await asyncio.sleep(30)
        await message.answer(os.getenv('FINISH_MESSAGE_2'))
        await state.clear()
    else:
        await message.answer(os.getenv('WRONG_ANSWER'))

@router.message(F.text)
async def Dd(message: types.Message):
    await message.answer("Не понимаю тебя.")
