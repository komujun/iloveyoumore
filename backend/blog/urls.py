from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
app_name = 'blog'

urlpatterns= [
    path('docs/',get_swagger_view(title="API문서"),name="swagger"),
    #path('login/'),#post
    path('getResult/',views.get_result),#get
    #path('mypage/'),#get
    #path('mypage/<str:name>/'),#get,delete
    #path('mypage/<str:name>/<str:image_path>/'),
]