# Section 7: Basic Styling and Frontend Timezone Conversion

This section adds basic CSS for styling and implements frontend timezone conversion using JavaScript.

## Steps

1.  **Create `style.css`:**

    Create a file `static/css/style.css` and add the following styles:

    ```css
    body {
        font-family: sans-serif;
        margin: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1 {
        color: navy;
    }

    .meme {
        border: 1px solid #ddd;
        padding: 10px;
        margin-bottom: 10px;
        width: fit-content;
    }

    .meme img {
        display: block;  
        margin: 0 auto; 
    }

    form {
        width: fit-content;
    }
    ```

2.  **Link to the CSS in `meme_list.html`:**

    Add the following within the `<head>` section of `memes/templates/memes/meme_list.html`:

    ```html
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    ```
    Add `{% load static %}` at the top of the file.

    ```html
    {% load static %}
    <!DOCTYPE html>
    ...
    ```

3.  **Add Frontend Timezone Conversion:**

    Modify `memes/templates/memes/meme_list.html` to include JavaScript for converting UTC datetimes:

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meme Gallery</title>
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        <h1>Meme Gallery</h1>

        <h2>Upload a Meme</h2>
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Upload</button>
        </form>

        {% for meme in memes %}
        <div class="meme">
            <h2>{{ meme.title }}</h2>
            <img src="{{ meme.image.url }}" alt="{{ meme.title }}" style="max-width: 400px;">
            <p>Uploaded at: <span class="datetime" data-utc="{{ meme.uploaded_at|date:'c' }}"></span></p>
        </div>
        {% endfor %}

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const datetimeSpans = document.querySelectorAll('.datetime');

                datetimeSpans.forEach(span => {
                    const utcString = span.dataset.utc;
                    const date = new Date(utcString);
                    const formattedDate = date.toLocaleString();
                    span.textContent = formattedDate;
                });
            });
        </script>
    </body>
    </html>
    ```

5.  Run the server and see the updated styling and localized timestamps.

## Explanation

*   **`static/css/style.css`:** Contains the CSS rules.
*   **`<link rel="stylesheet" ...>`:** Links the HTML to the CSS file.
*   **Frontend Timezone Conversion:**
    *   We use a `<span>` element with the class `datetime` and a `data-utc` attribute to store the UTC datetime string (formatted using `|date:'c'`).
    *   JavaScript code selects all elements with the class `datetime`.
    *   For each element, it gets the UTC string, creates a `Date` object, formats it using `toLocaleString()`, and sets the `<span>`'s text content to the formatted date.
    *   The `Date` object automatically handles the conversion to the browser's local timezone.