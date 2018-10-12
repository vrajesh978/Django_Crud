# Django_Crud
Django + Postgres + CRUD

# Running the project
`python manage.py runserver`

# After updating or creating any model do not forget to run following step
`python manage.py makemigrations`
`python manage.py migrate`
it will create model in db(here in postgres) for you.

# For MySQL
change example_project/settings.py as per below
line 77-86
` 'ENGINE' : 'django.db.backends.mysql',
  'NAME' : 'YOUR DATABASE NAME', 
  'USER' : 'USERNAME', 
  'PASSWORD' : 'Your Password', 
  'HOST' : 'localhost', 
  'PORT' : '3306', `
