
from django.urls import path
from . import views



#آدرسهای زیر مجموعه challenges



urlpatterns = [
    path("saturday", views.saturday),
    path("sunday", views.sunday),
        path("", views.xxchallenges),

]
