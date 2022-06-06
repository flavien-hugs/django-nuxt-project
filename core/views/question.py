# core.views.question.py

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Question
from core.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, url_path="current", methods=["GET"])
    def current_pools(self, request):
        questions = Question.active.all()
        serializer = self.get_serializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, url_path="closed", methods=["GET"])
    def closed_pools(self, request):
        questions = Question.closed.all()
        serializer = self.get_serializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
