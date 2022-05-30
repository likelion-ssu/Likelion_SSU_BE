"""EverytimeClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from EverytimeApp import views as et
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', et.landing),
    path('main/', et.main, name='main'),
    path('freeBoard/', et.freeBoard, name='freeBoard'),
    path('graduateBoard/', et.graduateBoard,  name='graduateBoard'),
    path('create/', et.create, name='create'), # 글 생성하기
    path('auth/', include('accounts.urls')),
    path('freeBoard/<int:post_id>/', et.detail, name="detail"),
    path('freeBoard/<int:post_id>/update/', et.update, name='update'),
    path('freeBoard/<int:post_id>/delete/', et.delete, name='delete'),
    path('comment/<int:post_id>', et.createComment, name='createComment'),
    path('freeBoard/<int:post_id>/<int:comment_id>/update', et.updateComment, name='updateComment'),
    path('freeBoard/<int:post_id>/<int:comment_id>/delete', et.deleteComment, name='deleteComment'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
