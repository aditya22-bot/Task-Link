
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='home'),
                  path('website/', include('website.urls')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  # path('api-auth/',include("rest_framework.urls")),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
