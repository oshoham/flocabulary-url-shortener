# flocabulary-url-shortener
A URL shortener implemented in Django, using PostgreSQL as the database and React on the front end.

## Ideas For Improvement
1. Check for URL validity before shortening, and display an error if the provided URL is invalid.
2. Display a visual indicator to the user when they click "Copy" to indicate that they have copied the shortened URL.

## Running Locally
Make sure you have installed:

  1. [Node and NPM](https://nodejs.org/en/)
  2. [Python](install.python-guide.org)
  3. [The Heroku Toolbelt](toolbelt.heroku.com)
  4. [Postgres](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql)

Create a Postgres user called `urlshortener` with password `password` that has permission to create databases, and a Postgres database called `urlshortener`. This is the hard part.

Optionally, install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and create/activate a virtual environment once you've cloned the git repo.

```
$ git clone https://github.com/oshoham/flocabulary-url-shortener.git
$ npm install
$ pip install -r requirements.txt
$ heroku local:run python manage.py migrate
$ python manage.py collectstatic
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Tests

To run the test suite, run

```
$ python manage.py test
```
