from django.urls import path
from . import views  # импорт из той папки где находится файл urls

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),  # импорт функции для маршрута
    path('<int:course_id>', views.single_course, name='single_course')
    # path('course/<int:course_id>', views.single_course, name='single_course')  # http://127.0.0.1:8000/shop/course/2
]
# '' главный путь маршрута
