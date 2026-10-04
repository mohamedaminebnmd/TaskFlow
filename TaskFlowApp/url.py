from django.urls import path
from . import views

app_name = 'taskflow'

urlpatterns = [
    path('',views.home, name='home-page'),
    path('tasks/all', views.all_tasks, name='all-tasks'),
    path('tasks/add', views.add_task, name='add-task'),
    path('tasks/<int:pk>', views.task_details, name='task-details'),
    path('tasks/<int:pk>/edit', views.task_edit, name='edit-task'),
    path('tasks/<int:pk>/delete', views.delete_task, name='delete-task'),
    path('auth/signup', views.signup, name='signup'),
    path('auth/login', views.login, name='login'),
    path('auth/logout', views.logout, name='logout')
]