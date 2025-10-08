from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index_view, contact_view, ProjectDetailView, ProjectListView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView, SignUpView, ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', index_view),
    path('project/', ProjectListView.as_view(), name='project_view'),
    path('contacts/', contact_view, name='contacts'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/', include(router.urls))
]
