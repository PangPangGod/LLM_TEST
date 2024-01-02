import asyncio
import time

import os
from apikey import GOOGLE_API_KEY
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY #SET API KEY

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'),)

#model_config
generation_config = {
    "temperature":0, #자유도
    "top_p":1, #token 순위(누적확률)
    "top_k":1, 
    "max_output_tokens":1024,
}

#여기에 safety 관련해서 넣는것, 일단 안 건듬.
safety_settings = [
    {}
]

## generate sequentially
def generate_with_sequence():
    model = genai.GenerativeModel(model_name='gemini-pro',generation_config=generation_config)

    for _ in range(3):
        response = model.generate_content("asyncio는 무엇이야? 한 문장으로 대답해.")
        print(response.text)

### run
s = time.perf_counter()
generate_with_sequence()
elapsed = time.perf_counter()-s
print("\033[1m" + f"Sequence Run executed in {elapsed:0.2f} seconds." + "\033[0m")

## generate asynchronously
async def async_generate(model):
    response = await model.generate_content_async("asyncio는 무엇이야? 한 문장으로 대답해.")
    print(response.text)

async def generate_concurrently():
    model = genai.GenerativeModel(model_name='gemini-pro',generation_config=generation_config)
    tasks = [async_generate(model) for _ in range(3)]
    await asyncio.gather(*tasks)
    
### run   
s = time.perf_counter()
asyncio.run(generate_concurrently())
elapsed = time.perf_counter()-s
print("\033[1m" + f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")

