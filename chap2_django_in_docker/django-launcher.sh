
#!/bin/sh

python3 manage.py collectstatic --noinput

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000

#daphine b 0.0.0.0 -p 8000 hello_world.asgi:application