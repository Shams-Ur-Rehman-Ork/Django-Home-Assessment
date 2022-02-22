# Django-Home-Assessment
This is a Django Home Assessment project from Trimulabs.

# Step: 1 (Making Virtual Environment for Django Project) --> for unix based systems
1. Make a directory in your PC and navigate to it using terminal.
2. Execute following command in terminal in the newly made directory. It will create a new folder by name venv. This is your virtual environment folder.
~~~
python3 -m venv venv
~~~
3. Next, execute following command in the same directory to activate virtual environment
~~~
source env/bin/activate 
~~~
4. Once you see venv in bracket(like this --> (venv)) in terminal editor, it means it is activated

# Step: 2 (Installing project dependencies inside virtual environment folder)
1. First take clone from github repo and navigate to main diectory of the project.
2. Execute following command to install all dependencies(Note --> Do it when virtual environment is activated, if not activate it first by following above instructions)
~~~
pip install -r requirements.txt
~~~

# Step: 3 (Postgres Database settings)
1. Make a database named as (django-assessment)
2. Make a user named as (assessment) with password (My_Django_Project)
3. Once database is successfully configured, now we are ready to finalize project settings.
4. Project database credentials are also given in project's setting file.

# Step: 4 (Making migrations)
1. Navigate to main project directory.
2. Open terminal in this directory and execute following command to make tables in database.
~~~
python3 manage.py migrate
~~~
3. Now, run project in local server by executing following command.
~~~
python3 manage.py runserver
~~~

4. Now access endpoints using postman collection provided in the project folder.
