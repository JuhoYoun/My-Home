from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from django.conf import settings




# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # 기존의 context 데이터를 가져옵니다.
        context = super().get_context_data(**kwargs)

        # settings에서 MAX_IMAGE_SIZE 값을 가져와 context에 추가합니다.
        context['max_image_size'] = settings.MAX_IMAGE_SIZE_MB
        return context


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    form_class = CommentCreationForm


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 25

    def get_queryset(self):  # get_queryset 메소드를 override
        # order_by('?')를 사용하여 랜덤하게 객체를 가져옵니다.
        return self.model.objects.order_by('?')
