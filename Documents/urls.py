from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Documents.views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/', contact, name='contact'),
    path('user_login/', user_login, name='user_login'),
    path('login_admin/', login_admin, name='login_admin'),
    path('signup/', signupUser, name='signup'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('changepassword/', changepassword, name='changepassword'),
    path('editprofile/', editprofile, name='editprofile'),
    path('upload_documents/', upload_documents, name='upload_documents'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)