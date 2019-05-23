from unittest.mock import patch
from django.contrib import auth
from django.test import TestCase
from django.urls import reverse
from .tools import create_admin_user, create_regular_user, create_user_social_auth


class TestMainPage(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('repo:main_page')

    def setUp(self):
        super().setUp()
        self.post_data = {
            'name': 'test-repo',
            'description': 'description',
            'homepage': '',
            'has_issues': False,
            'has_projects': False,
            'has_wiki': False
        }

    def test_access_denied(self):
        self.assertEqual(302, self.client.get(self.url).status_code)  # redirect user to login page

    def test_user_admin_redirect(self):
        user = create_admin_user()
        self.client.force_login(user)
        self.assertEqual(302, self.client.get(self.url).status_code)  # redirect user to login page

    def test_get_success(self):
        user = create_regular_user()
        create_user_social_auth(user)
        self.client.force_login(user)
        self.assertEqual(200, self.client.get(self.url).status_code)

    @patch('repo.views.GitHubAPI.git_push')
    @patch('repo.views.GitHubAPI.create_repo')
    def test_post_success(self, create_repo, git_push):

        def side_effect(arg):
            return {'git_url': 'some://github.com/test/test.git'}

        create_repo.side_effect = side_effect
        git_push.side_effect = None
        user = create_regular_user()
        create_user_social_auth(user)
        self.client.force_login(user)
        self.assertEqual(302, self.client.post(self.url, self.post_data).status_code)

    def test_form_invalid(self):
        user = create_regular_user()
        create_user_social_auth(user)
        self.client.force_login(user)
        self.post_data['name'] = ''
        response = self.client.post(self.url, self.post_data)
        self.assertEqual(200, response.status_code)


class TestGitHubLoginRedirectView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('repo:github_login')

    def test_logout(self):
        user = create_admin_user()
        self.client.force_login(user)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.client.get(self.url)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
