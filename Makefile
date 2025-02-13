r:
	python manage.py makemigrations && python manage.py migrate && python manage.py runserver


c:
	celery -A choose_me worker -l debug