# RealmRiff
A creative space where users riff on their favorite genres.

<!-- ------------------------------------ -->
1. Created directory named as Project_name
2. Created a virtual env.
"python -m venv .venv"

3. Activated that virtual env.
".venv\Scripts\activate"

4. Installed django.
"pip install django"

<!-- ------------------------------------ -->
5. Create Project directory
"django-admin startproject project_name"

6. Started apps for diff functioning inside project directory - using following command.
"python mange.py startapp app_name"

7. Updated settings.py file in terms of newApps.
8. Created new templates folder inside project directory(same as app levels), and inside each app and add the directory name in the Templates > DIRS in settings.py file.
9. Created new static folder inside project directory(same as app levels).
10. Let's run the makemigrations command for each app to test what we have done so far.
"python manage.py makemigrations app_name"

11. Let's run the migrate command to apply the migrations to the database.
"python manage.py migrate"

12. Execute the command to run server.
"python manage.py runserver"

<!-- ------------------------------------ -->
13. Design a layout.html file inside project > templates > layout.html
14. Design a index.html file for homepage of the website inside the project > templates > index.html this index file will inherit layout.html file.
15. Create a view.py file inside project and create a view to render this index file.
16. Create a url-pattern for accessing that particular view.

<!-- ----------------------------------- -->
17. Create superuser for this project. 
"python manage.py createsuperuser"

