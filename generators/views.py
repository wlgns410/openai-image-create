import openai
from pathlib import Path
from base64 import b64decode
import json
import os 

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.views import View

from generators.serializers import ImageSerializer
from rest_framework.views import APIView
from dotenv import load_dotenv

class CreateImage(generics.CreateAPIView):
    serializer_class = ImageSerializer

    # json 데이터 형식으로 뽑았음
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data.get('prompt')
            n = serializer.validated_data.get('n')
            size = serializer.validated_data.get('size')
            response_format = serializer.validated_data.get('response_format')
            api_key = serializer.validated_data.get('api_key')

            response = openai.Image.create(prompt=prompt, n=n, size=size, response_format=response_format, api_key=api_key)
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

### 이부분 주석 해제하고 쓰세요(위 class 는 주석하시고!)
# load_dotenv()
# mySecret = os.environ.get('OPENAI_API_KEY')

# class CreateImage(APIView):
#     def post(self, request):

#         data = json.loads(request.body)
#         prompt = data.get("prompt", None)
#         response = openai.Image.create(prompt=prompt, 
#                                         n=1, 
#                                         size='256x256', 
#                                         response_format='b64_json', 
#                                         api_key=mySecret)
#         data_dir = Path.cwd()
#         file_name = data_dir / f"{prompt[:5]}_{response['created']}.json"
#         with open(file_name, mode="w", encoding="utf-8") as file:
#             json.dump(response, file)
    
#         for index, image_dict in enumerate(response["data"]):
#             image_data = b64decode(image_dict["b64_json"])
#             image_file = data_dir / f"{file_name.stem}-{index}.png"
#             with open(image_file, mode="wb") as png:
#                 png.write(image_data)
#         return response
