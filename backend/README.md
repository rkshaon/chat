# Chat
Realtime chatting application.

## Declaration
Python version
```
Python 3.10.12
```
Django version
```
Django == 5.0.6
```
Channels version
```
channels == 4.1.0
```
Daphne is required.
Daphne version
```
daphne == 4.1.2
```
Redis on local machne is required.

## Setup
Clone the project on project directory.
```
git clone git@github.com:rkshaon/chat.git
```

Create virtual environment and activate

[Here steps are in details.](https://github.com/rkshaon/software-engineering-preparation/tree/master/Languages/Python/environment)

After activating virtual environment install dependecies
```
pip install -r requirements.txt
```

Migrate
```
python manage.py makemigrations
python manage.py migrate
```

Create superuser
```
python manage.py createsuperuser
```

Run the project
```
python manage.py runserver
```

## Usage
Open `http://127.0.0.1:8000/chat/` in two individual browser, or in two tabs of a browser.

Enter into the same room. And start chatting.