from .import views
from django.urls import path


urlpatterns = [
    path("btc", views.btc, name="btc"),
    path("gold", views.gold, name="gold"),
    path("boors", views.boors, name="boors"),
    path("tala", views.tala, name="tala"),
    path("ahrom", views.ahrom, name="ahrom"),
]
