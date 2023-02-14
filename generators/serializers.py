import os 
import openai
import json
from pathlib import Path
from base64 import b64decode
from dotenv import load_dotenv
from rest_framework import serializers


# load_dotenv()
# mySecret = os.environ.get('OPENAI_API_KEY')
mySecret="test"

class ImageSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    n = serializers.IntegerField(default=1)
    size = serializers.CharField(default='256x256')
    response_format = serializers.CharField(default='b64_json')
    api_key = serializers.CharField(default=mySecret)
    
    # 사진으로 나오게 
    # def create(self, validated_data):
    #     response = openai.Image.create(prompt=validated_data['prompt'], 
    #                                     n=validated_data['n'], 
    #                                     size=validated_data['size'], 
    #                                     response_format=validated_data['response_format'], 
    #                                     api_key=validated_data['api_key'])
    #     data_dir = Path.cwd()
    #     file_name = data_dir / f"{validated_data['prompt'][:5]}_{response['created']}.json"
    #     with open(file_name, mode="w", encoding="utf-8") as file:
    #         json.dump(response, file)
    
    #     for index, image_dict in enumerate(response["data"]):
    #         image_data = b64decode(image_dict["b64_json"])
    #         image_file = data_dir / f"{file_name.stem}-{index}.png"
    #         with open(image_file, mode="wb") as png:
    #             png.write(image_data)
    #     return response
