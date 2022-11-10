import asyncio
import logging
from aiogram import Bot, Dispatcher, types
# from config_reader import config
# bot = Bot(token=config.bot_token.get_secret_value())  -> это я пытался скрыть токен

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5456177375:AAGTNXZ1R5GRjdeo3nfn4KSJwZQqut-k_ts")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message_handler(commands=["joke"])
async def cmd_start(message: types.Message):
    await message.answer("Заходит однажды тестировщик в бар.Забегает в бар.Пролезает в бар.Танцуя, проникает в бар.Крадётся в бар.Врывается в бар.Прыгает в бар.")

@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    await message.answer("Выберите команду:\n/help\n/start\n/joke")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())