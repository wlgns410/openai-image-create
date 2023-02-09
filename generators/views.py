import openai

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from generators.serializers import ImageSerializer


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

