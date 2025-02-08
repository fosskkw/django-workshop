# Section 4: Basic View and Template

This section covers creating a view to display memes and a template to render them.

## Steps

1.  **Create the `meme_list` View:**

    Open `memes/views.py` and add:

    ```python
    from django.shortcuts import render
    from .models import Meme

    def meme_list(request):
        memes = Meme.objects.all()
        return render(request, 'memes/meme_list.html', {'memes': memes})
    ```

2.  **Create the Template Directory:**

    Create the following directory structure:

    ```
    memes/
        templates/
            memes/
                meme_list.html
    ```

3.  **Create the `meme_list.html` Template:**

    Open `memes/templates/memes/meme_list.html` and add:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meme Gallery</title>
    </head>
    <body>
        <h1>Meme Gallery</h1>

        {% for meme in memes %}
            <div>
                <h2>{{ meme.title }}</h2>
                <img src="{{ meme.image.url }}" alt="{{ meme.title }}" style="max-width: 400px;">
                <p>Uploaded at: {{ meme.uploaded_at }}</p>
            </div>
        {% endfor %}
    </body>
    </html>
    ```

4.  **Create the App's `urls.py`:**

    Create a file `memes/urls.py` and add:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.meme_list, name='meme_list'),
    ]
    ```

5.  **Include the App's URLs in the Project's `urls.py`:**

    Open `meme_gallery/urls.py` and modify it:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('memes.urls')),
    ]
    ```

6. Run the server and visit `http://127.0.0.1:8000/`

## Explanation

*   **View:**  A function that handles a request and returns a response.
    *   `render()`: Combines a template with data to produce HTML.
    *   `Meme.objects.all()`: Retrieves all `Meme` objects from the database.
*   **Template:**  An HTML file with placeholders for dynamic content.
    *   `{% for ... %}` ... `{% endfor %}`:  Template loop.
    *   `{{ ... }}`:  Displays data from the view.
*   **URL Configuration:** Maps URLs to views.
    *   `urls.py` (app): Defines URL patterns for the app.
    *   `urls.py` (project): Includes app URLs.
    *   `include()`: Includes URL patterns from another file.