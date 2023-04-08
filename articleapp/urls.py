from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("list/", TemplateView.as_view(template_name='articleapp/list.html'), name='list'), # Django에서 기본적으로 제공해준다. 우리가 Template만 지정해주면 나머지는 다 만들어준다
]