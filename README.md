## REST Webapp for rockets

Built with Django, and Django's REST Framework module. The database used is SQLite, Python's bundled self-contained, file-based SQL database. Tested locally on MacOS.

0. Install python3 if not already installed.

1. To build the app, clone the repo.
> git clone https://github.com/kevinye2/rocketapp.git 

> cd rocketapp

2. Setup virtual environment
> python3 -m venv env

3. Activate virtual environment
> source env/bin/activate

4. Install all requirements
> pip3 install -r requirements.txt

5. Enter Django website directory.
> cd website

6. Apply initial migrations for data models.
> python3 manage.py migrate

7. Load dummy rocket data.
> python3 manage.py loaddata data.json # loads in data from a directory called fixtures (Django specific)

8. Run django webapp
> python3 manage.py runserver

Once the webapp is up and running, you should be able to test it locally by going to http://127.0.0.1:8000/
When the app is open in the browser, you can view the list of rockets by going to http://127.0.0.1:8000/Rocket/, and you can add to the list of rockets with the UI on the page.
You can also see individual rockets by appending the primary-key to the end of the url, i.e. http://127.0.0.1:8000/Rocket/1. Here, you can modify the rocket's data values with a PUT request.

All data requests can be changed to its json representation, or default api representation. 