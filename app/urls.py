from django.urls import path
from .views import CreateUser,LoginUser
from django.conf import settings
from django.conf.urls.static import static

user = CreateUser.as_view({
    'get' : 'list',
    'post':'create'
})
user1 = CreateUser.as_view({
    'get':'retrieve',
    'delete':'destroy',
    'put':'update',
    'patch':'partial_update'
})

urlpatterns = [
    path('createUser/',user),
    path('createUser/<int:pk>',user1),
    path('loginUser/',LoginUser.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)