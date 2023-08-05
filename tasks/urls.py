from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks'),
    # administrator
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('get-otp/', views.get_otp, name='get_otp'),
    path('forget-password/', views.forget_password, name='forget_password'),
    path('change-password/<token>/', views.change_password, name='change_password'),

    # tasks
    path('add/', views.add_task, name='add'),
    path('update/<int:tid>/', views.update_task, name='update'),
    path('delete/<int:tid>/', views.delete_task, name='delete'),
]
