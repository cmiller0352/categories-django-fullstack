from django.urls import path
from . import views

urlpatterns = [
  path('categories/', views.category_list, name='category_list'),
  path('categories/<int:pk>', views.category_detail, name='category_detail'),
  path('categories/new', views.new_category, name='new_category'),
  path('categories/<int:pk>/edit', views.edit_category, name='edit_category'),
  path('categories/<int:pk>/delete', views.delete_category, name='delete_category'),

  path('categories/<int:pk>/posts', views.post_list, name='post_list'),
  path('categories/<int:pk>/posts/new', views.new_post, name='new_post'),
  path('categories/<int:pk>/posts/<int:fk>/edit', views.edit_post, name='edit_post'),
  path('categories/<int:fk>/posts/<int:pk>', views.post_detail, name='post_detail'),
  path('categories/<int:fk>/posts/<int:pk>/delete', views.delete_post, name='delete_post')

]