from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project


class ProjectModelTest(TestCase):
    def test_project_str_representation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        project = Project.objects.create(
            title='Surprise',
            description='It was unexpected',
            author=user
        )
        self.assertEqual(str(project), project.title)


class ProjectViewTest(TestCase):
    def test_project_list_view_url_exists(self):
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)

    def test_project_list_uses_correct_template(self):
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_create_project_redirects_if_not_logged_in(self):
        response = self.client.get('/project/create/')
        self.assertEqual(response.status_code, 302)

