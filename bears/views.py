from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from bears.models import Bear, Result, BracketContestant, Year
from bears.serializers import BearSerializer, ContestantSerializer, OverviewSerializer


class BearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer


class ChampionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BracketContestant.objects.champions()
    serializer_class = ContestantSerializer


class FinalistsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BracketContestant.objects.finalists()
    serializer_class = ContestantSerializer


class OverviewViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Year.objects.all()
    serializer_class = OverviewSerializer
