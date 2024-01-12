from langchain.chat_models import ChatOpenAI
from apikey import OPENAI_API_KEY
import os

import asyncio
import time
from langchain.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

## Stream Test
# chat = ChatOpenAI(model="gpt-3.5-turbo")

# response = chat.stream("너는 어떤 모델이고, 어떤 일을 할 수 있어?")

# for chunk in response:
#     print(chunk.content, end="", flush=True)

## Async TEST with LCEL

async def generate_concurrently():
    model = ChatOpenAI(model="gpt-3.5-turbo-1106")
    prompt = ChatPromptTemplate.from_template("이 인물에 대해 어떻게 생각하는지 이야기해줘. 인물 : {who}")
    chain = prompt | model

    tasks = [async_generate(chain) for _ in range(3)] ## 여기 수정하면 됨
    await asyncio.gather(*tasks)

async def async_generate(chain):
    response = await chain.ainvoke(input={"who":"넬슨 만델라"})

    # for chunk in response:
    #     print(chunk.content, end="", flush=True)
    print(response.content)


s = time.perf_counter()

asyncio.run(generate_concurrently())
elapsed = time.perf_counter()-s
print("\033[1m" + f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")

