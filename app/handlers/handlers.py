from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

command_router = Router()

@command_router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Start Command work')

@command_router.message(F.text == 'настройки')
async def settings(message: Message):
    await message.answer('Settings work')