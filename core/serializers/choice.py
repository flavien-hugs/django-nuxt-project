# core.serializers.choice.py

from rest_framework.serializers import(
	ModelSerializer, IntegerField
)

from core.models import Choice


class ChoiceSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = Choice
        fields = ["id", "text", "question"]
        read_only_fields = ("question",)