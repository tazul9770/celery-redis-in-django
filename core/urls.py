from django.contrib import admin
from django.urls import path
from emailar.views import home, send_welcome_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('send_welcome_email/', send_welcome_email, name='send-welcome-email')
]
