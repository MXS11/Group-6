After setting up everything in the My_project, you will need to set up OAuth application via https://console.developers.google.com/
Getting started
* GO to the Dashboard, create a NEW PROJECT
* Name your new project.User will be able to see the name of this project when we redirect them to Google login page.
* Afer you click "CREATE" to proceed.

APIs Credentials
*Back to “Dashboard”, go to “Credentials” on left panel.
*Create credentials. On the dropdown, choose “OAuth Client ID” option.

OAuth consent screen
*Make sure you fill out the “OAuth Consent Screen” form.
*You’ll only need to provide “Application name”, “Email” and click “SAVE”.

Create OAuth client ID
*Now, you can create your OAuth Client ID by filling out these details;
*Authorized Javascript origins (http://127.0.0.1:8000)
*Authorized redirect URL (http://127.0.0.1:8000/accounts/google/login/callback/)

Obtain OAuth client
*Once you click “CREATE”, you will be able to obtain your “client ID” and “client Secret”.
*You’ll need this information to proceed the next steps

We’ll need to configure Django admin. To access the admin panel, you’ll need to create a superuser to login. Type this command on terminal:
(my_project) python manage.py createsuperuser
	You’re required to provide “username”, “email” and “password” in the terminal. Once you’re done, proceed to start the server:
(my_project) python manage.py runserver
Go to (http://127.0.0.1:8000/admin) to access your admin page. Make sure you provide the credentials to login.

For refrence: https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5

Add a site
*On the SITES section, click “sites” and fill out the details and click “Save”:
Domain name: 127.0.0.1:8000
Display name: 127.0.0.1:8000
*Add social applications
Back to admin homepage, under “SOCIAL ACCOUNTS” section, click “Social applications” to fill out these settings:
Provider: Google
Name: Google API
Client id: (refer step 7, your OAuth details)
Secret key: (refer step 7, your OAuth details)