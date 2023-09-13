from django.urls import path, include

from landingpageapp.views import PageView

app_name = "landingpageapp"

urlpatterns = [
    path('<str:page_name>', PageView),

]