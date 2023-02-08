import openai
import json
from pathlib import Path
from base64 import b64decode

from dotenv import load_dotenv
import os 

# load .env
load_dotenv()

mySecret = os.environ.get('OPENAI_API_KEY')


PROMPT = input("Ai가 그려줄 이미지에 대한 묘사: ")
api_key = mySecret



description = 'a flying hamburger in space, digital art'    # Ai가 그려줄 이미지에 대한 묘사
response = openai.Image.create(prompt=PROMPT            # 텍스트 입력
                               , n=1                    # 생성할 이미지 개수
                               , size= "1024x1024"      # 이미지 크기
                               , response_format= "b64_json"
                               , api_key = api_key) # openai API키

 
DATA_DIR = Path.cwd() # os.getcwd()
file_name = DATA_DIR / f"{PROMPT[:5]}_{response['created']}.json"  # 생성된 이미지파일 저장 경로

# json 파일로 저장하기 
with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)
    
# png 파일로 저장
for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = DATA_DIR / f"{file_name.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)
