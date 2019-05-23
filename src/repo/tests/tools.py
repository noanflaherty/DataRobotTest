from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from social_django.models import UserSocialAuth


def create_user_base(**kwargs):
    fields = {
        'username': get_random_string(),
        'email': '{0}@test.com'.format(get_random_string(5)),
        'is_staff': False,
        'is_superuser': False,
    }
    fields.update(kwargs)
    user = User(**fields)
    user.save()
    return user


def create_admin_user():
    return create_user_base(is_staff=True, is_superuser=True)


def create_regular_user():
    return create_user_base()


def create_user_social_auth(user, **kwargs):
    fields = {
        'user': user,
        'provider': 'github',
        'uid': '1045555',
        'extra_data': {
            'auth_time': 1558545074,
            'id': 1045555,
            'expires': None,
            'login': 'testUser',
            'access_token': '8q6e36515ee784fec53e',
            'token_type': 'bearer'
        }
    }
    fields.update(kwargs)
    user_social_auth = UserSocialAuth(**fields)
    user_social_auth.save()
    return user_social_auth
