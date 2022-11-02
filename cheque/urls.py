
from django.urls import path
from .views import RegisterPage,CustomLoginView,homepage,success

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('register/',RegisterPage.as_view(), name='Register'),
    path('login/',CustomLoginView.as_view(),name='Login'),
    path('image_upload/', homepage, name = 'homepage'),
    path('success', success, name = 'success'),

    path('logout/',LogoutView.as_view(next_page='Login'),name='Logout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
