from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

open_weather_token = "5456177375:AAGTNXZ1R5GRjdeo3nfn4KSJwZQqut-k_ts"