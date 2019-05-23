Architecture
==================================================

DataRobotTest project - simple self-replicated project where user can easily copy current project into his/her GitHub repo just with 1 click.

This project is divided into two django apps, core project, static and templates

1. `data_test` - is a core project package and includes settings file, urls file with all project's urls and wsgi file for running the project

2. `github` - package to work with GitHub. It includes api module which can check and create repo in user's GitHub account

3. `repo` - package which includes logic of main page (show copy repo form and handle the process of creation and copying)

4. `static` - folder to store all project assets

5. `templates` - folder with all project templates
