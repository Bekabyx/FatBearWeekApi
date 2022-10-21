from rest_framework import serializers
from bears.models import Bear, BracketContestant, Round, Year, Bracket


class BearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bear
        fields = "__all__"


class BasicBearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bear
        fields = ["bear_uuid", "bear_name", "bear_number"]


class ContestantSerializer(serializers.HyperlinkedModelSerializer):
    bracket_date = serializers.StringRelatedField(source="bracket.bracket_date")
    bear = BasicBearSerializer()

    class Meta:
        model = BracketContestant
        fields = ["bracket_date", "bear"]


class BracketContestantBearSerializer(serializers.Serializer):
    bear_uuid = serializers.UUIDField(source="bear.bear_uuid", default=None)
    bear_name = serializers.StringRelatedField(source="bear.bear_name", default=None)
    bear_number = serializers.IntegerField(source="bear.bear_number", default=None)

    class Meta:
        model = BracketContestant
        fields = ["bear_uuid", "bear_name", "bear_number"]


class BracketSerializer(serializers.HyperlinkedModelSerializer):
    bracket_date = serializers.StringRelatedField()
    contestants = BracketContestantBearSerializer(many=True, source="bracket_bc")

    class Meta:
        model = Bracket
        fields = ["bracket_date", "contestants"]


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    brackets = BracketSerializer(source="round_brackets", many=True)

    class Meta:
        model = Round
        fields = ["round_number", "brackets"]


class OverviewSerializer(serializers.HyperlinkedModelSerializer):
    rounds = RoundSerializer(source="year_rounds", many=True)

    class Meta:
        model = Year
        fields = ["competition_year", "rounds"]
