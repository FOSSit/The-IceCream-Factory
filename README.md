# The-IceCream-Factory

The aim of our project is to create and host a https website for an Ice Cream shop called The IceCream Factory with a menu, contacts and different services available that are available at the store.
All the customers who have registered in the website will receive an email notification about any discounts, new flavours available or any other events they may organise.

Installation Guide:

Web Server: 
Choose a web server like Apache (https://httpd.apache.org/docs/2.4/install.html) or Nginx (https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/). Refer to their official documentation for installation instructions specific to your operating system.
Python (3.x recommended): 
Download and install Python from https://www.python.org/downloads/.
Django Framework: 
Install Django using pip install django.
Git Version Control System (optional, but recommended): 
Install Git from https://git-scm.com/downloads for collaboration and version control.

Project Setup:
Clone the Repository (if using Git):

If you have a GitHub repository for your project, clone it using:
Bash
git clone https://github.com/FOSSit/The-IceCream-Factory.git
Use code with caution.
If not using Git, download the project files manually and extract them.
Create a Virtual Environment (recommended):

Isolate project dependencies using python -m venv venv (replace venv with your desired virtual environment name).
Activate the virtual environment:
For Linux/macOS: source venv/bin/activate
For Windows: venv\Scripts\activate
Install Project Dependencies:

Navigate to your project directory (where manage.py is located).
Install required packages using pip install -r requirements.txt (assuming you have a requirements.txt file specifying dependencies).
Database Configuration:

Choose a Database:

Select a database management system like PostgreSQL (https://www.postgresql.org/) or MySQL (https://www.mysql.com/). Installation instructions vary, so refer to their documentation.
Create a Database:

Follow your chosen database system's instructions to create a database for your project.
Django Database Settings:

Edit your project's settings.py file.
Update the DATABASES dictionary with your database connection details:
Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.<your_database_engine>',  # e.g., 'postgresql_psycopg2'
        'NAME': '<your_database_name>',
        'USER': '<your_database_user>',
        'PASSWORD': '<your_database_password>',
        'HOST': '<your_database_host>',
        'PORT': '<your_database_port>',
    }
}
Use code with caution.
Website Content and Design:

Create App(s):

Organize your website's models (data structure) and views (logic) into Django apps. Use python manage.py startapp <app_name> to create apps.
Develop Models:

In your app(s), define models using Django's ORM (Object-Relational Mapper) to represent data like ice cream flavors, menus, services, and customer information (for email notifications).
Consider using a library like django-allauth (https://docs.allauth.org/) if you want to allow customer registration for managing preferences.
Create Views:

Write Django views (functions or classes) to handle user requests (e.g., displaying menus, sending email notifications).
Design Templates:

Create HTML templates using Django's templating system to define the website's structure and layout. Use {% include %} tags to reuse common components.
Static Files (CSS, JavaScript):

Place static files like CSS and JavaScript in a static directory within your app(s) or project root.
Email Notifications:

Email Backend Configuration:

Install a suitable email backend like django-sendmail-backend (https://pypi.org/project/django_sendmail_backend/) using pip install django-sendmail-backend.
Configure the email backend in settings.py with your email server details (SMTP server, port, credentials).
Implement Email Sending Functionality:

In your views or custom functions, use libraries like django.core.mail or third-party email libraries to send email notifications to customers.