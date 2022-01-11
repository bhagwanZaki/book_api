from rest_framework import routers, urlpatterns
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register("",bookApi,"bookApi")

urlpatterns = [
    path("latest/",latestBookApi.as_view())
]
urlpatterns += router.urls
