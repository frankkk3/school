
from django.contrib.auth import views
from django.urls import path
from django.views.generic.base import View
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
 
    path('a/',a,name='a'),
    path('',index,name='Index'),
    path('<slug:category_slug>',comb,name="pro_cate"),
    path('blogdetail/<int:id>',blogdetail,name='blogdetail'),
    path('addProject/', addProject, name='addProject'),
    path('updateProject/<int:id>/', updateProject, name='updateProject'),
    path('deleteProject/<int:id>/',deleteProject, name='deleteProject'),
    path('home/',home,name='homepage'),
    path('about/',about,name='aboutpage'),
    path('contact/',contact,name='contactpage'),
    path('register/',register,name='registerpage'),
    path('searchstu/',searchstudent,name='searchpage'),
    path('profile/',EditProfile, name='editprofile'),
    path('upload/',upload,name='uploadpage'),
    path('search/', searchBar, name='search'),
    path('coma/',coma,name='com_a-page'),
    path('userup/',userup,name='userup-page'),
    path('comb/',comb,name='com_b-page'),
    path('teacher/',allteacher,name='teacherpage'),
    path('blogdetail/<int:id>/add-comment',add_comment, name='add-comment'),
    path('blogdetail/<int:id>/delete-comment',delete_comment, name='delete-comment'),
    
 
    
]




urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.MEDIA_ROOT)



