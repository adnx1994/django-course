from .import views
from django.urls import path


urlpatterns = [
    path("btc",views.btcView.as_view(),name="btc"),
    path("gold",views.goldView.as_view(),name="gold"),
    path("boors",views.boorsView.as_view(),name="boors"),
    path("tala",views.talaView.as_view(),name="tala"),
    path("ahrom",views.ahromView.as_view(),name="ahrom"),
]