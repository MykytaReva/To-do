from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.TodoListView.as_view(), name='todo_list'),
    path('list/active/', views.TodoActiveListView.as_view(), name='todo_list_active'),
    path('list/completed/', views.TodoCompletedListView.as_view(), name='todo_list_completed'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>/', views.ToDoDeleteView.as_view(), name='todo_delete'),
    path('details/<int:pk>/', views.ToDoDetailView.as_view(), name='todo_details'),


]
