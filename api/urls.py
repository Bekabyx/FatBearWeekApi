from django.urls import path, include
from rest_framework import routers

from bears.views import BearViewSet, ChampionsViewSet, FinalistsViewSet, OverviewViewset

router = routers.DefaultRouter()
router.register(r"bears", BearViewSet)
router.register(r"overview", OverviewViewset, basename="overview")
router.register(r"champions", ChampionsViewSet, basename="champions")
router.register(r"finalists", FinalistsViewSet, basename="finalists")


urlpatterns = [
    path("api/", include(router.urls)),
]
