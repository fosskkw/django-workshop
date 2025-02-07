# Section 2: Create App and Model

This section covers creating a Django app and defining the `Meme` model.

## Steps

1.  **Create the `memes` App:**

    ```bash
    python manage.py startapp memes
    ```

2.  **Register the App:**

    Open `meme_gallery/settings.py` and add `'memes'` to the `INSTALLED_APPS` list:

    ```python
    INSTALLED_APPS = [
        # ... other apps ...
        'memes',  # Add this line
    ]
    ```

3.  **Define the `Meme` Model:**

    Open `memes/models.py` and add the following code:

    ```python
    from django.db import models

    class Meme(models.Model):
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to='memes/')
        uploaded_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title
    ```

4.  **Install Pillow** (for image processing):

    ```bash
    pip install Pillow
    ```

5.  **Create Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Explanation

*   **App:**  A module within a project, organizing code for a specific feature.
*   **Model:**  Defines the data structure (database table).
    *   `CharField`: For text.
    *   `ImageField`: For image files (`upload_to` specifies where to store them).
    *   `DateTimeField`: For date and time (`auto_now_add=True` sets the timestamp automatically).
    *   `__str__`:  Provides a human-readable representation of the object.
*   **Migrations:**  Django's way of managing changes to the database schema.
    *   `makemigrations`: Creates migration files.
    *   `migrate`: Applies migrations to the database.