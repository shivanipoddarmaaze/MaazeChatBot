# MaazeChatBot
ChatBot is created using following Technologies:

- [Python](https://www.python.org/downloads/release/python-3100/) 
- [Django](https://www.geeksforgeeks.org/django-tutorial/)
- [Channels](https://channels.readthedocs.io/en/stable/tutorial/part_2.html)
- [Redis](https://redis.io/)

## Installation

ChatBot requires [Python 3.10](https://www.python.org/downloads/release/python-3100/) to run.

Install the dependencies and start the server.

1. Activate [virtual environment](https://docs.python.org/3/tutorial/venv.html)
2. Install requirements.
```sh
pip install -r requirements.txt
```

3. Run commands to create migrations:
```sh
python manage.py makemigration
python manage.py migrate
```
4. Start the server...

```sh
python manage.py runserver
```
5. Server will run on http://127.0.0.1:8000/
