from aiogram import Bot, Dispatcher, types, filters, F
import asyncio
import openai

SECRET_KEY = "sk-proj-ial1WuAymUn2Rwn09BLsT3BlbkFJGyktK0UlQqn0o0kOgSom"
openai.api_key = SECRET_KEY

bot = Bot(token='6459329359:AAHu94Zhtq4LjHSBeKv7z3bIHzdVpQA0k_A')
dp = Dispatcher(bot=bot)


def answer_process(question):
    response = openai.Completion.create(
            model='gpt-3.5-turbo-instruct',
        prompt=f"Hey bro, i have question to and the question is {question}."
               f"After answering please just answer in Uzbek language",
        max_tokens=1000,
    )
    if response['choices'][0]['text']:
        answer = response['choices'][0]['text']
        answer.replace("_", "\\_")
        answer.replace("*", "\\*")
        answer.replace("[", "\\[")
        answer.replace("`", "\\`")
        answer.replace("=", "\\=")
        return answer
    else:
        return "Nima deb yozding?"


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Xush kelibsiz, men ChatGPT botman. Qanaqa savoling bor?")


@dp.message(F.text)
async def text_function(message: types.Message):
    result = await answer_process(question=message.text)

    await message.answer(text=result)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
