from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.form, name='form'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]