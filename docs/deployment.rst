Deployment
==================================================

simple deployment on https://www.pythonanywhere.com

1. Make sure you are already registered on this resource

2. Create an app

 `go to Web tab and click Add a new web app`

 `choose manual configuration`

3. Create virtualenv

 `go to Consoles tab and and click Bash`

 `mkvirtualenv --python=/usr/bin/python3.5 <env_name>`

4. clone the project from your repo

 `git clone https://github.com/<username>/<repo_name>.git`

5. Install requirements

 `pip install -r DataRobotTest/requirements.txt`

6. Configure project

 1. `go back to the Web tab > in the Virtualenv section add path to a virtualenv`

 2. `/home/<your_user_name>/.virtualenvs/<env_name>`

 3. `go to the Code section and click on WSGI configuration file`

 4. `remove everything and past data from pythonanywhere_wsgi.sample file but change username to yours`

 5. `go to the Static files section and add static url` (URL=/static/; Directory=/home/<username>/DataRobotTest/src/static_cdn/)

7. Setup DataBase

 1. `go to the Databases tab`

 2. `set password for DB`

 3. `add new DB in Create a database`

 4. `copy DB name (it should look like something like this username$dbname)`

 5. `copy Database host address`

 6. `copy Username`

8. Create .env file in the console

 1. `cp DataRobotTest/.env.sample DataRobotTest/.env`

 2. change vars in .env file (make sure DB_NAME will set correctly)

9. Set those variables in the console (https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/)

 1. `set -a; source ~/DataRobotTest/.env; set +a`

10. django project setup

 1. `python src/manage.py migrate`

 2. `python src/manage.py collectstatic`

 3. `python src/manage.py createsuperuser`

11. Go to the Web tab and reload server (now everything should work)

12. Enjoy!
