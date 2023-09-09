from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('instagram/',InstagramView.as_view(), name='instagram'),
    path('telegram/',TelegramView.as_view(), name='telegram'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('facebook/',FacebookView.as_view(),name='facebook'),
    path('time/',SoatView.as_view(),name='soat'),
]