Installation
==================================================

1. Make sure you have virtualenv installed

 `pip install virtualenv` https://virtualenv.pypa.io/en/stable/installation/

2. Install all requirements

 `pip install -r requirements.txt`

3. Create GitHub app and get tokens

 https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/

4. Add environment 3 variables

 `SECRET_KEY; SOCIAL_AUTH_GITHUB_KEY; SOCIAL_AUTH_GITHUB_SECRET; ALLOWED_HOST`

 `for dev environment use ALLOWED_HOST=localhost`

5. Create super user

 `python src/manage.py createsuperuser`

6. Run the server

 `python src/manage.py runserver`
