from django.urls import path
from dogs.apps import DogsConfig

from dogs.views import DogListView, DodDetail, DogCreateView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
    path('', DogListView.as_view(), name='dog_list'),
    path('dogs/<int:pk>/', DodDetail.as_view(), name='dog_detail'),
    path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    path('dogs/<int:pk>/update/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),
]
