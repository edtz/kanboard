Kanboard/ITMO-THESIS
========

### Description
Kanban board as a service. Allows to created projects and fill them with user stories, which could be assigned to developers and sprints. Each story tracks its own status. Functional, but lacks front page. Completed in May '16.

### Prerequisites
- Python 3.x
- Django
- MDL

### How to use
Run migrations:

    ./manage.py makemigrations
    ./manage.py migrate

And then run however you like, for example using django's dev server:

    ./manage.py runserver
