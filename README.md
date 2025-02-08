# Section 3: Admin Interface and Media File Configuration

This section covers setting up the Django admin interface and configuring media file handling.

## Steps

1.  **Register the `Meme` Model:**

    Open `memes/admin.py` and add:

    ```python
    from django.contrib import admin
    from .models import Meme

    admin.site.register(Meme)
    ```

2.  **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts.

3.  **Configure Media File Settings:**

    Open `meme_gallery/settings.py` and add these settings at the *bottom* of the file:

    ```python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    ```

4.  **Create the `media` Directory:**

    Create a directory named `media` at the *root* level of your project (next to `manage.py` and the `meme_gallery` directory):

    ```bash
    mkdir media
    ```

5.  **Serve Media Files in Development:**
    Add the following to `meme_gallery/urls.py`

    ```python
    from django.conf import settings # Add this at the top if it is not present
    from django.conf.urls.static import static # Add this at the top
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add this line
    ```

6.  **Access the Admin:**

    Run the server (`python manage.py runserver`) and go to `http://127.0.0.1:8000/admin/`. Log in. You should now be able to add memes, and the uploaded images will be stored in the `media/memes/` directory.

## Explanation

*   **Admin Interface:**  A built-in interface for managing your data.
*   **`admin.site.register()`:** Makes your model manageable in the admin.
*   **Superuser:** An administrator account.
*   **`MEDIA_URL`:** The URL prefix for accessing media files in your templates (e.g., `{{ meme.image.url }}`).
*   **`MEDIA_ROOT`:**  The *absolute path* to the directory where media files will be stored on your server's file system.
*   **`static(settings.MEDIA_URL, ...)`:**  This tells Django's development server how to serve media files during development.  This is *not* needed (and shouldn't be used) in a production environment.