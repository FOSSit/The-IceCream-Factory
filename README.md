# The IceCream Factory Website

This project is a Django-based web application for The IceCream Factory, an ice cream shop. The website features the shop's menu, contact information, and various services. Registered customers will receive email notifications about discounts, new flavors, and upcoming events.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**
    ```
    git clone https://github.com/yourusername/theicecreamfactory.git
    ```

2. **Set up a virtual environment** (Optional but recommended)
    ```
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```
    python manage.py migrate
    ```

5. **Run the server**
    ```
    python manage.py runserver
    ```

Now, you can access the website at `http://127.0.0.1:8000/`.

## Features

- **Menu**: Browse our wide selection of ice cream flavors.
- **Contact Us**: Get in touch with us for any queries or feedback.
- **Services**: Learn about our special services like home delivery and catering.
- **User Registration**: Register to receive email notifications about our latest offers and events.

## Contributing

We welcome contributions! Please see our Contributing Guidelines for more details.

## License

This project is licensed under the MIT License.
