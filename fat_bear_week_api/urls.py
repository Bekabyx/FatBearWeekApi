from django.contrib import admin
from django.urls import path, include
from .views import (
    BearsView,
    ChampionsView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/', include(fbw_urls)),
    path('api/bears', BearsView.as_view()),
    path('api/champions', ChampionsView.as_view()),
]

