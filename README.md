# URL Shortener Project

This is a simple Django-based URL shortener application that allows users to shorten long URLs and get a shorter link for easier sharing.

## Features

- Shorten URLs
- Redirect to original URLs using the shortened slug

## Prerequisites

- Python 3.x
- Django 3.x or later
- SQLite (default database)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AlpaarX/shortly-django.git
   ```
2. Navigate to the project directory:

   ```bash
   cd your-project-name
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## URL Shortening Flow

The user submits a URL via the form.
If the URL already exists, the existing shortened slug is shown.
If the URL is new, it is stored in the database, and a new shortened URL is generated.
