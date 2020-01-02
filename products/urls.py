from . import views
from django.urls import path

urlpatterns = [
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote')

]
