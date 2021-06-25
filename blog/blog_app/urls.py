from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login, name='login'),
    path('add_blog/', views.add, name='add'),
    path('delete/<int:blogid>/', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update')
]
