# demo-graphene
Demo Graphene + Django

## Installation

```
pip install -U pip wheel
pip install -r requirements.txt
```

## Init database

`cd server`, then:

```
python manage.py migrate
python manage.py loaddata fixture.json
```
