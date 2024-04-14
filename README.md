# The IceCream Factory Website

Welcome to The IceCream Factory's website project! This project aims to create a secure HTTPS website for The IceCream Factory, showcasing their menu, contact information, and various services available at their store. Additionally, registered customers will receive email notifications about discounts, new flavors, and upcoming events organized by the shop.

## Aim
The Aim of our project is to create host a https website for a Ice Cream shop called The IceCream Factory with there menu, contact and different services available at there store.
To all the resisted customers at there website they must receive an email notification about any discounts, new flavour available or any other events they might organise.

## Features

- HTTPS secure website
- Menu display
- Contact information
- Registration for customers
- Email notifications for registered customers
- Discount alerts
- New flavor notifications
- Event announcements

## Installation Guide

### Prerequisites

- Python installed on your system. You can download and install it from the [Python website](https://www.python.org/).
- Access to an SMTP server for sending emails.

### Setup Instructions

1. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv myenv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        myenv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source myenv/bin/activate
        ```

2. **Install Django and other dependencies:**

    ```bash
    pip install Django==4.2.1 asgiref==3.7.2 sqlparse==0.4.4 tzdata==2023.3
    ```

3. **Start a new Django project:**

    ```bash
    django-admin startproject icecreamfactory
    ```

4. **Navigate into the project directory:**

    ```bash
    cd icecreamfactory
    ```

5. **Create a new Django app for the website:**

    ```bash
    python manage.py startapp website
    ```

6. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

10. **Access the website:**

    Open your web browser and go to `http://localhost:8000`.

### Usage

- Visit the website to explore the menu, contact information, and other services.
- Register as a customer to receive email notifications about discounts, new flavors, and events.
- Admins can manage discounts, flavors, and events through the Django admin panel (`http://localhost:8000/admin`).

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.
