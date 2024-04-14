# The-IceCream-Factory

PROJECT OVERVIEW:

Introduction:
Welcome to the development of the IceCream Factory's website project! Our objective is to create a secure HTTPS (Hypertext Transfer Protocol Secure) platform for an ice cream shop called the IceCream Factory with their home page displaying various details of the business. Through this website, the customers can seamlessly navigate through and decide on the ice-cream they want using the menu, access their contact details for queries and uncover the vast array of services provided at their store. All the interested customers can sign up for the email notifications and will be informed about any discounts, new available flavour or other events organised by the shop. 

Key Features of the Website:
1. Menu- Browse through the diverse selection of ice-creams to select the one which tickles your taste buds the most!
2. Contact Details- The shop's contact information including their address, phone number and email address is available on the website in case of queries.
3. Offered Services- The various services provided by the shop including event catering and custom flavour orders are also available, and shop to be contacted for further information using the given contact information. 
4. Email Notification- Registered customers will recieve email notifications for discounts, new flavours and organised events. 
	a. Discounts- Seasonal discounts, exclusive offers and limited time discounts will be notified to the customers. 
	b. New Flavours- New flavours added to the menu will be informed to the customers.
	c. Organised Events- Upcoming shop organised events such as ice-cream tasting and giveaway days will also be notified to the registered customers.

Technologies Used:
1. Django Framework- For a strong, dependable and scalable backend, Django web framework has been used for development. 
2. SQLite Database Management System: SQLite secure database has been used to securely store the data, ensuring user privacy while allowing for efficient retrieval and manipulation of customer details. flavours and order details.

INSTALLATION GUIDE:

System Requirements:
1. Python:
    a. Modern Operating System such as Windows/macOS/Linux
    b. Stable python released version
    c. Adequate disc space for python installation and usage 

2. Django:
    a. Compatibility with your python version
    b. Sufficient memeory and CPU resources for handling web requests

3. SQLite:
    a. storage for database storage

Dependancy Installation Steps (for each OS):
1. Python (version 3.x):
    a. WINDOWS-
        i. Download the latest version of Python for Windows from the official Python website
        ii. Run the installer and follow the installation wizard
        iii. Make sure to check the option to add Python to PATH during installation
        iv. Use pip commands in terminal to install required libraries and dependancies 

    b. macOS-
        i. Install a the required python version using Homebrew or the official installer from the Python website
        ii. In terminal, use pip commands to install required libraries and dependancies

    c. Linux-
        i. Python is usually pre-installed on most Linux distributions and if not, you can install it using the package manager
        ii. Use the command "sudo apt-get install python3" in terminal to install python
        iii. Use "pip install package_name" command in terminal to installed required libraries and dependancies
    
2. Django (version compatible with python 3.x):
    a. WINDOWS-
        i. Open terminal and to execute command "pip install django" to install django
    
    b. macOS-
        i. Open terminal and to execute command "pip install django" to install django

    c. Linux-
        i. Open terminal and to execute command "pip install django" to install django

3. SQLite:
    a. WINDOWS-
        i. Go to the SQLite download page and download the precompiled binaries for Windows.
        ii. Extract the contents of the downloaded ZIP file to a folder on your computer
        iii. If you want to run SQLite from any directory in Command Prompt, you can add the SQLite binary folder to your system PATH

    b. macOS-
        i. Homebrew Installation:
            1. Open terminal and install Homebrew using " /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" "
            2. Install SQLite using "brew install sqlite"
        ii. MacPorts Installation:
            1. Open terminal and install MacPorts
            2. Install SQLite using "sudo port install sqlite3"
    
    c. Linux-
        i. Update the package index "sudo apt-get update" on terminal
        ii. Install SQLite using "sudo apt-get install sqlite3"
    
Commands:
1. Cloning Repository:
    a. Use command "git clone <repository_url>" if you just want to copy into current directory. 
    b. Use command "git clone <repository_url> <directory_name>" to copy to a specific directory. 

2. Creating Virtual Environment:
    a. WINDOWS-
        i. Use "python -m venv myenv" command in terminal to create virtual environment.
        ii. Use "myenv\Scripts\activate" command in terminal to activate virtual environment. 

    b. macOS-
        i. Use "python3 -m venv myenv" command in terminal to create virtual environment. 
        ii. Use "source myenv/bin/activate" command in terminal to activate vitual environment.  

    c. Linux-
        i. Same steps as maxOS.

USAGE GUIDE: 
1. Navigate to your Django directory and activate the virtual environment. 
2. Run command "python manage.py runserver" in terminal from inside Django directory. 
3. This starts the development server using Django.
4. Once the server is running, open a web browser and navigate to the address provided in the terminal (default = http://127.0.0.1:8000/).
5. Interact with the website as required. 
6. To stop the development server, go back to the terminal or command prompt where it's running and press Ctrl + C. You'll be prompted to confirm that you want to shut down the server. Press y and Enter to confirm.