from django.urls import path
from . import views  # импорт из той папки где находится файл urls

urlpatterns = [
    path('', views.index, name='index')  # импорт функции для маршрута
]
# '' главный путь маршрута
