from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription
from django.conf import settings


# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # 기존의 context 데이터를 가져옵니다.
        context = super().get_context_data(**kwargs)

        # settings에서 MAX_IMAGE_SIZE 값을 가져와 context에 추가합니다.
        context['max_image_size'] = settings.MAX_IMAGE_SIZE_MB
        return context


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object()).order_by('-id')
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription,
                                                               **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25


    def get_queryset(self):  # get_queryset 메소드를 override
        # order_by('?')를 사용하여 랜덤하게 객체를 가져옵니다.
        return self.model.objects.order_by('?')
