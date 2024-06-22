from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
urlpatterns += [
    path('bulletins/', views.bulletin_list, name='bulletin_list'),
    path('bulletin/<int:pk>/', views.bulletin_detail, name='bulletin_detail'),
    path('bulletin/new/', views.bulletin_create, name='bulletin_create'),
    path('bulletin/<int:pk>/edit/', views.bulletin_edit, name='bulletin_edit'),
    path('bulletin/<int:pk>/delete/', views.bulletin_delete, name='bulletin_delete'),
]