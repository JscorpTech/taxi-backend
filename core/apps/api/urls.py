from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarBrandView, CarView, TaxiView, BotView, BotUserView

router = DefaultRouter()
router.register("bot", BotView, basename="bot")
router.register("car-brand", CarBrandView, basename="car-brand")
router.register("car", CarView, basename="car")
router.register("taxi", TaxiView, basename="taxi")
router.register("bot-user", BotUserView, basename="bot-user")


urlpatterns = [
    path("", include(router.urls)),
]
