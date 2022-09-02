from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addStudent/', views.addStudent, name='addStudent'),
    path('delData/<int:id>', views.delData, name='delData'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updateData/<int:id>', views.updateData, name='updateData'),
]