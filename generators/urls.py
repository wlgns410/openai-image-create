from django.urls import path
from generators.views import CreateImage

urlpatterns =[
    path('image', CreateImage.as_view())
]
