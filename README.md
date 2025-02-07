# Section 1: Project Setup

This section covers setting up your Django project and running the development server.

## Steps

1.  **Create a Virtual Environment:**

    This isolates your project's dependencies. Run the following command:

    ```bash
    python3 -m venv venv
    ```

    Activate the environment:

    ```bash
    # Windows
    venv\Scripts\activate
    # macOS and Linux
    source venv/bin/activate
    ```
    You should see `(venv)` in your terminal prompt.

2.  **Install Django:**

    ```bash
    pip install django
    ```

3.  **Create the Django Project:**

    ```bash
    django-admin startproject meme_gallery
    cd meme_gallery
    ```

4.  **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    Open your browser and go to `http://127.0.0.1:8000/`. You should see the Django welcome page!  Press Ctrl+C to stop the server.

## Explanation

*   **Virtual Environment:**  Keeps project dependencies separate, preventing conflicts.
*   **`django-admin startproject`:** Creates the basic project structure.
*   **`manage.py`:**  A command-line utility for managing your Django project.
*   **`runserver`:**  Starts the built-in development server for testing.