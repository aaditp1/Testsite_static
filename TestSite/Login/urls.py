from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Signup,name="login"),
    path('signup',views.Signup,name="signup"),
    path('login',views.login,name="actlogin"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate')
]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)