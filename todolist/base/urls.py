from django.urls import path
from .views import Tasklist,Taskdetail,TaskcreateView,TaskUpadateView,TaskDeleteView,login,TaskReorder,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task'),
    path('task-create/', TaskcreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpadateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder')
]
