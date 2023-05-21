"""MiniBlog URL Configuration

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
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from blog.forms import LoginForm,MyPasswordResetForm,MySetPasswordForm,MyPasswordChangeForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.miniblog, name='miniblog'),
    path('miniblog/', views.miniblog1, name='miniblog1'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name="about"),
    path('user_contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.user_signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('addpost/',views.add_post,name="addpost"),
    path('updatepost/<int:id>',views.update_post,name="updatepost"),
    path('contact/',views.user_contact,name="contact"),
    path('delete/<int:id>',views.delete_post,name="deletepost"),

    #  Authentication Code


    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='blog/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='blog/passwordchangedone.html'),name='passwordchangedone'),

    path("password-reset/",auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html',form_class=MyPasswordResetForm), name="password_reset"),

    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html',form_class=MySetPasswordForm), name="password_reset_confirm"),

    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name="password_reset_complete"),


]
