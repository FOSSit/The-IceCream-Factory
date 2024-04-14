# The IceCream Factory Website

## Project Overview

The purpose of this project is to create a comprehensive online presence for The IceCream Factory, a popular ice cream shop. The website serves as a digital platform where customers can explore the menu, learn about the services offered, get in touch with the shop, and stay updated on the latest news and events.

The website has the following functionalities:
- **Menu**: Customers can browse through a wide variety of ice cream flavors available at the shop.
- **Contact**: Customers can find the contact information of the shop and reach out for any queries or feedback.
- **Services**: Information about various services like home delivery, catering, etc., is available.
- **Email Notifications**: Registered customers receive email notifications about discounts, new flavors, and upcoming events.

This project is built using the Django framework and uses an SQLite database for data storage.

## Installation Guide

### System Requirements
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps
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

### Platform-Specific Instructions
- The above instructions are generally applicable to all platforms (Windows/macOS/Linux). If you encounter any issues, please raise an issue in the repository.

## Usage Guide
1. **Apply migrations**
    ```
    python manage.py migrate
    ```

2. **Run the server**
    ```
    python manage.py runserver
    ```

Now, you can access the website at `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions! Please see our Contributing Guidelines for more details.

## License

This project is licensed under the MIT License.
