Getting Started
To get started with the project, follow these steps:

Clone this repository to your local machine.
Navigate to the project directory.
Install the necessary dependencies.
Set up the environment variables for your SMTP server.
Run the development server.
Open your browser and navigate to the local server to view the website.
Features
Menu: Browse through our delicious ice cream flavors and toppings.
Contact: Find our contact information and get in touch with us.
Services: Learn about the services we offer at our store.
Email Notifications: Registered customers will receive email notifications about discounts, new flavors, and events.
Technologies Used
This project utilizes various technologies, including Node.js, Express.js, MongoDB, React.js, Bootstrap, and SMTP for email notifications.
Installation Guide for Ice Cream App using Django
This guide will walk you through the steps to set up and run the Ice Cream app using Django with home.html as the main page.


----INSTLLATION GUIDE--------------------------------------------------------------------------------------------------------------------------------------------


Prerequisites
Before you begin, ensure you have the following installed:

Python (version 3.x)
Django (version 4.2.1)
Git (optional, if you want to clone the repository)
Step 1: Clone the Repository
If you haven't already, clone the repository to your local machine. Open your terminal or command prompt and run the following command:

bash
Copy code
git clone https://github.com/your-username/ice-cream-app.git
Replace your-username with your actual GitHub username.

Step 2: Navigate to the Project Directory
Navigate to the project directory using the cd command:

bash
Copy code
cd ice-cream-app
Step 3: Set Up Python Environment
Create a virtual environment for the project. Run the following commands to create and activate the virtual environment:

bash
Copy code
python3 -m venv env
source env/bin/activate   # For Linux/Mac
env\Scripts\activate      # For Windows
Step 4: Install Django and Dependencies
Install Django and other required packages using pip. Run the following command:

bash
Copy code
pip install django==4.2.1
pip install asgiref==3.7.2 sqlparse==0.4.4 tzdata==2023.3
Step 5: Create a Django Project and App
Create a Django project and an app for the Ice Cream website. Run the following commands:

bash
Copy code
django-admin startproject icecream_project .
python manage.py startapp icecream_app
Step 6: Configure Django Settings
Navigate to the settings.py file in your Django project (icecream_project/settings.py). Update the INSTALLED_APPS list to include your app ('icecream_app',) and set the TEMPLATES configuration to include the templates directory.

python
Copy code
INSTALLED_APPS = [
    ...
    'icecream_app',
]

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
Step 7: Create HTML Templates
Create a templates directory in your app (icecream_app) if it doesn't exist. Inside the templates directory, create a home.html file with your HTML content for the main page.

Step 8: Define URL Routing
Create a urls.py file inside your app (icecream_app/urls.py) if it doesn't exist. Define the URL routing to map the main page to the home.html template.

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
Step 9: Create Views
Define the view function for the main page in the views.py file inside your app (icecream_app/views.py).

python
Copy code
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
Step 10: Run the Development Server
Start the Django development server to run your Ice Cream app. Run the following command:

bash
Copy code
python manage.py runserver
