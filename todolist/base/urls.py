from django.urls import path
from .views import Tasklist,Taskdetail,TaskcreateView,TaskUpadateView,TaskDeleteView,login

urlpatterns = [
    path('login/',login,name='login'),
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task'),
    path('task-create/', TaskcreateView.as_view(), name='task-view'),
    path('task-update/<int:pk>/', TaskUpadateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete')
]
