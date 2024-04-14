 The project aims to create a secure HTTPS website for The IceCream Factory, showcasing their menu, contact information, and various services available at their store. Additionally, registered customers will receive email notifications about discounts, new flavors, and upcoming events organized by the shop.

## FEATURES


- Discount alerts
- New flavor notifications
- Event announcements

## INSTALLATION GUIDE


1. **Create a virtual environment :**

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

7. **Access the website:**

    Open your web browser and go to `http://localhost:8000`.


CD 


 