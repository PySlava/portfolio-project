from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .forms import ProjectForm
from .models import Project
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly
from .pagination import CustomPagination


def index_view(request):
    return render(request, 'index.html', {'user_name': 'Slava'})


def contact_view(request):
    menu_contacts = {
        'email': 'test@example.com',
        'telegram': '@test_user',
    }
    return render(request, 'contacts.html', {'contacts': menu_contacts})


@method_decorator(cache_page(60), name='dispatch')
class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'my_project'

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', None)
        queryset = Project.objects.all()
        if search_query:
            vector = SearchVector('title', 'description')
            query = SearchQuery(search_query)
            queryset = queryset.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'detail'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_view')
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user


class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_view')

    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = CustomPagination
