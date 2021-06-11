# Python-Flask Webhook Implementation for Virtual Machines

This module contains code which implements an order-status webhook in python for cloud or on prem hosting options. In 
order to edit and deploy your changes you first need to follow these setup steps.

## Setup

1. Create a virtual environment

```
python3 -m venv venv
```

2. Activate the environment

```
. venv/bin/activate
```

3. Install flask

```
pip install Flask
```

Then you can start the server by running:

```
python app.py
```

## Deployment

### Hosted

1. [Deploying Flask on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
2. [Deploying Flask on Google App Engine](https://cloud.google.com/appengine/docs/standard/python3/runtime)
3. [Deploying Flask on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
4. [Deploying on Azure (IIS)](https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python)
5. [Deploying on PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/)

### Self-Hosted

1. [uWSGI](https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/)
2. [gunicorn](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#gunicorn)
