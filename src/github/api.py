import json
import os
import requests
from django.conf import settings


class GitHubAPI:
    URL = 'https://api.github.com/'
    headers = None

    def __init__(self, user):
        social_auth = user.social_auth.get(provider='github')
        self.token = social_auth.extra_data['access_token']
        self.username = user.username
        self.headers = {
            'Authorization': 'token {0}'.format(self.token)
        }

    def repo_exists(self, name):
        url = '{0}repos/{1}/{2}'.format(self.URL, self.username, name)
        r = requests.get(url, headers=self.headers)
        return r.status_code == 200

    def create_repo(self, data):
        url = '{0}user/repos'.format(self.URL)
        r = requests.post(url, json.dumps(data), headers=self.headers)
        return r.json()

    def git_push(self, repo_url):
        os.system('cd {0} && git push https://{1}:{2}@{3} --all'.format(
            os.path.dirname(settings.BASE_DIR), self.username, self.token, repo_url)
        )
