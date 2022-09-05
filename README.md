## REST Webapp for space systems

Built with Django, and Django's REST Framework module. The database used is SQLite, Python's bundled self-contained, file-based SQL database. Tested locally on MacOS.

0. Install python3 if not already installed.
1. To build the app, clone the repo.
> git clone
> cd Webapp

2. Setup virtual environment
> python3 -m venv env

3. Activate virtual environment
> source env/bin/activate
> 
> # Install all requirements
> pip3 install -r requirements.txt


Apply migrations for data models.
> python manage.py migrate

Load dummy rocket data.
> python manage.py loaddata data.json # loads in data from a directory called fixtures (Django specific)


4. Run django webapp
> python manage.py runserver