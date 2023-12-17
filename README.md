# temp_deleted_notes_CRUD_operation
 Temporary deleted notes, is a Django-based web application designed for managing notes and implementing CRUD (Create, Read, Update, Delete) functionalities. It provides a RESTful API using Django REST Framework for creating, retrieving, updating, and deleting notes. The application integrates Celery for background task processing and Redis as a message broker.

source venv_name/bin/activate   #create virtual Environment
.\venv_name\Scripts\activate
source venv_name/bin/activate

### install some dependencies
pip install -r requirements.txt
python manage.py runserver

python manage.py startapp app_name
python manage.py makemigrations
python manage.py migrate

####create admin page
python manage.py createsuperuser

python manage.py collectstatic
python manage.py test

####Celery commands
#Start celery worker
celery -A your_project_name worker -l info

# start celery beat
celery -A your_project_name beat -l info

