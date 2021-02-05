+### Installation
Requirements before installation 
python 3.7.1
pip3
virtualenv ==16.7.9
virtual-clone ==0.5.3
mysqlclient
(Creating virtualenv is not mandatory)
Please refer to https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/
To install the list on requirement.txt, run
```sh
$ pip3 install -r requirements.txt
```
### Settings
In settings.py, modify the values of NAME, USER, PASSWORD, HOST and PORT based on your enviroment setups
```sh
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'Heatmap_data',
    'USER': 'root',
    'PASSWORD': 'admin',
    'HOST': 'localhost',
    'PORT': '3306',
    'OPTIONS': {
    'read_default_file': '/etc/mysql/my.cnf',
     },
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Development and Test
Create database Heatmap_data and import .sql file from Database folder.
Run setup to create the virtual env.
cd Heatmap
Activate the virtual env
Go to Heatmap folder that includes manage.py file,  and run:

```sh
$ python manage.py runserver
```
or
```sh
$ python3 manage.py runserver
```
### Username and Password

user = admin, password = facialstats123




