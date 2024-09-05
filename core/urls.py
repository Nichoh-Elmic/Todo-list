from django.urls import path
from . import views
from .views import ToDoListCreate, ToDoDetailUpdateDelete

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'), 
    path('todos/', ToDoListCreate.as_view(), name='todo_list'),  
    path('todos/<int:pk>/', ToDoDetailUpdateDelete.as_view(), name='todo_detail'),  
]