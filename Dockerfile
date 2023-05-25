FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/JuhoYoun/My-Home.git

WORKDIR /home/My-Home/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000"]














