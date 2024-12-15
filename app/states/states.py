from aiogram.fsm.state import StatesGroup, State

class NewTask(StatesGroup):
    name = State()
    importance = State()
    urgency = State()