from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import *

command_router = Router()

@command_router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Start Command work')

@command_router.message(F.text == '⚙ Настройки')
async def new_task(message: Message):
    await message.answer(f'⚙ | <b>Настройки</b>')

#Add new task
@command_router.message(F.text == '✏ Новая задача')
async def new_task(message: Message, state: FSMContext):
    await state.set_state(NewTask.name)
    await message.answer(f'📎 | <b>Добавление новой задачи</b>\n\nВведите название новой задачи')

@command_router.message(NewTask.name)
async def new_task_addname(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(NewTask.importance)
    await message.answer(f'<b>Прекрасно!</b>\nТеперь введите уровень важности для задачи <b>{message.text}</b>\n\nВводить требуется число от 1 до 5, где 1 - неважно, а 5 - очень важно')

@command_router.message(NewTask.importance)
async def new_task_addimportance(message: Message, state: FSMContext):
    await state.update_data(importance = message.text)
    await state.set_state(NewTask.urgency)
    await message.answer(f'<b>Великолепно!</b>\nТеперь введите уровень срочности\n\nВводить требуется число от 1 до 5, где 1 - несрочно, а 5 - очень срочно')

@command_router.message(NewTask.urgency)
async def new_task_addurgency(message: Message, state: FSMContext):
    await state.update_data(urgency = message.text)
    data = await state.get_data()
    await message.answer(f'📒 | Добавлена новая задача!\n\nНазвание: {data['name']}\nСтепень важности: {data['importance']}\nСтепень срочности: {data['urgency']}')
    await state.clear()

#fc
@command_router.message(F.text == '📄 Последняя задача')
async def new_task(message: Message):
    await message.answer(f'📄 | <b>Последняя задача</b>\n\n')


