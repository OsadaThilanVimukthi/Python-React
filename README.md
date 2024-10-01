# Python-React+Flask

Im Osada thilan vimukthi now im larning flask i have much experience on djnago

Step

Create Virtual env
 using python *n venv venv(Name if u like)
 install flask packages using pip, pip in package manager of python

 pip install flask_socketio


 deployment

 u need to create wsgi.py file and
 and install pip install gunicron eventlet

 create requirements.txt pip freeze > requirements.txt
 gunicorn --worker-class eventlet -w 1 wsgi:app