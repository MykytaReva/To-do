from django.contrib import admin
from django.urls import path, include
from todo import views

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),

    path('To-Do/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_change/', views.PasswordChangeView.as_view(),
         name='password_change'),

]
