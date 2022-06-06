# core.router.py

from rest_framework.routers import DefaultRouter

from core.views import QuestionViewSet

router = DefaultRouter()

router.register(r"pools", QuestionViewSet, basename="pool")
