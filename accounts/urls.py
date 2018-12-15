from django.urls import re_path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^login/$', LoginView.as_view(), {'template_name': 'accounts/login.html'}),
    re_path(r'^logout/$', LogoutView.as_view(), {'template_name': 'accounts/logout.html'}),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^profile/$', views.view_profile, name='view_profile'),
    re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    re_path(r'^change-password/$', views.change_password, name='change_password'),
    re_path(r'^reset-password/$', PasswordResetView.as_view(), name='reset_password'),
    re_path(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset-password/confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^accounts/$', views.account, name='accounts'),
    re_path(r'^doctor_home/$', views.doctor_home, name='doctor_home'),
    re_path(r'^see-employees/$', views.see_employees, name='see_employees'),
]