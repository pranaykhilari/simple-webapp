from django.conf.urls import url, include
from django.contrib import admin

from website.views import *
from website.views import profile, logout_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += [
    url(r"^$",Login.as_view(), name="account_login"),
    url(r"^accounts/login/$", Login.as_view(), name="account_login"),
    url(r"^accounts/signup/$", Signup.as_view(), name="account_signup"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", ConfirmEmail.as_view(), name="account_confirm_email"),
    url(r"^email/$",Email.as_view(), name="account_email"),
    url(r"^dashboard/$", profile, name="profile"),
    url(r"^logout/$", logout_user, name="logout"),
    url(r"^test/$",test_user, name="test"),
    url(r"^check_contact/$", check_user_contact, name="check_contact")
]