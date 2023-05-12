FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/JuhoYoun/My-Home.git

WORKDIR /home/My-Home/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure--5ej32jnwnzn%jv$gb)z@=e1c@(lvtha!1&o9o9%2z4p4_n16s" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pinterest.wsgi", "--bind", "0.0.0.0:8000"]
