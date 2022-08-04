from django.urls import path, include
from todo import views
app_name = 'todo'

urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='todo_list'),
    path('list/active/', views.TodoActiveListView.as_view(), name='todo_list_active'),
    path('list/completed/', views.TodoCompletedListView.as_view(), name='todo_list_completed'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>/', views.ToDoDeleteView.as_view(), name='todo_delete'),
    path('details/<int:pk>/', views.ToDoDetailView.as_view(), name='todo_details'),
    path('login/', views.ToDoLoginView.as_view(), name='todo_login'),
    path('register/', views.signup, name='todo_register'),
    path('reg/', views.regist, name='regist'),
    # path('password_change/', views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change')

]