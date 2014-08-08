SockJS-Cyclone deployment on Heroku Quickstart
==============================================

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click on the button above for one-click heroku deploy, or just follow the detailed instructions below.

Install `mkvirtualenvwrapper`, `git` and the `heroku toolbelt` using your distribution package manager.

Clone this repository:
```
git clone https://github.com/flaviogrossi/sockjs-cyclone_heroku_quickstart.git`
```

Create your python virtualenv for local use:
```
mkvirtualenv sockjs_heroku_app
```

Install the required dependencies in your virtualenv:
```
pip install -r requirements.txt
```

Login with your Heroku account:
```
heroku login
```

Test your app locally:
```
foreman start
```

Create your Heroku app:
```
heroku create
```

Push your code to Heroku:
```
git push heroku master
```

Optionally, enable experimental [Heroku support for websockets](https://blog.heroku.com/archives/2013/10/8/websockets-public-beta):
```
heroku labs:enable websockets
```

Enjoy your newly deployed SockJs-Cyclone Heroku app!
