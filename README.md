tellascope
=============

## Requirements

- `virtualenv` and `virtualenvwrapper`

## Getting started
Please note – this guide assumes you are using OS X. If you aren't, you hopefully know the equivalent commands to make these things happen. If you don't, find someone to help you!

First, clone this project.

```bash
git clone git@github.com:nuvention-web/dac.git
cd dac
```

Then, create the virtual environment for your project.

```bash
mkvirtualenv tellascope
add2virtualenv .
```

Add this to your `~/.virtualenvs/tellascope/bin/postactivate` file:
```bash
export DJANGO_SETTINGS_MODULE=tellascope.config.settings.development
```

And install the requirements:

```bash
pip install Django==1.7
pip install -r requirements.txt
```

Note: Django is not in the requirements because django-faker requires it to be installed before it can be installed.

Now create the database (this assumes you have postgres installed) and run Postgres:

```bash
createdb tellascope
pgup
```

```
export DJANGO_SETTINGS_MODULE=tellascope.config.settings.development
```

You should be able to run your first `migrate` now:

```bash
django-admin makemigrations
django-admin migrate
```

You will also need to install Grunt and other Node dependencies to compile the Sass (this assumes you already have `node` and `grunt-cli` installed).

```bash
npm install
grunt dev
```

Do some things for Django static files:
```
sudo mkdir -p /var/www/tellascope/static/ && sudo chmod -R 777 /var/www/tellascope/static/
django-admin collectstatic
```

Then, you should be able to run the server:

```bash
django-admin runserver
```


