# Fat Bear Week API

#### Project aim: a totally unofficial but well-intentioned API to serve data about Katmai National Park's fat bears.

[What is Fat Bear Week?](https://explore.org/fat-bear-week)

This is one of those "can't sleep at 4am" projects, so it may or may not actually go anywhere. 

This project runs Python > 3.8 with Django and Postgres. 

## DB Setup
If you just want to look at the schema, check out the `schema.sql` file in `/database`.

You'll need Postgres if you don't already have it 
```commandline
brew install postgres
```

Create a database called `fat_bear_week` and run the following:
```commandline
python manage.py migrate
python manage.py import_bears
```

If any changes are made to the models, a migration will need to be created:
```commandline
python manage.py makemigrations
python manage.py migrate -- this step will run the new migrations against the db
```

## Run
Make sure you've got a venv up with the requirements installed.
```commandline
pip install -r requirements.txt
```
Make sure you've got your DB connection info in `settings.py/DATABASES`

From there it's just standard Django fare
```commandline
python manage.py runserver  
```

## Endpoints
Current endpoints:
- `/api/bears GET` - all info held about every bear on our books
- `/api/champions GET` - all bears that have won a final round, date of final and basic bear ID
- `/api/finalists GET` - all bears that have competed in a final round, date of final and basic bear ID

Proposed endpoints:
#### GET
- `/bears/{uuid}`
  - all the ID information held about a specific bear
- `/matchups/{year}`
  - a simple bear vs. bear list of matchups and dates for the given year
- `/rivals` 
  - every bear and their no. 1 rival (the bear that has beat them in a 1-1 the most times)
- `/overview/{year: optional}`
  - admin stuff, e.g. no. rounds, participants, start-end dates, winner, no. votes cast

#### POST (stretch goal as these will need to be locked down)
- `/results/{bracket_uuid}`
  - write a result record for a given bracket uuid. 
- `/bears`
  - create/update a bear
