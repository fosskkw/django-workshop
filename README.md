# Section 6: User Uploads

This section implements user uploads using forms.

## Steps

1.  **Create `forms.py`:**

    Create `memes/forms.py` and add:

    ```python
    from django import forms
    from .models import Meme

    class MemeForm(forms.ModelForm):
        class Meta:
            model = Meme
            fields = ['title', 'image']
    ```

2.  **Update `views.py`:**

    Replace the content of `memes/views.py` with:

    ```python
    from django.shortcuts import render, redirect
    from .models import Meme
    from .forms import MemeForm

    def meme_list(request):
        if request.method == 'POST':
            form = MemeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('meme_list')
        else:
            form = MemeForm()

        memes = Meme.objects.all()
        return render(request, 'memes/meme_list.html', {'memes': memes, 'form': form})
    ```

3.  **Update `meme_list.html`:**

    Add the form to `memes/templates/memes/meme_list.html`:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meme Gallery</title>
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
            <div>
                <h2>{{ meme.title }}</h2>
                <img src="{{ meme.image.url }}" alt="{{ meme.title }}" style="max-width: 400px;">
                <p>Uploaded at: {{ meme.uploaded_at }}</p>
            </div>
        {% endfor %}
    </body>
    </html>
    ```

4.  Run the server and test the upload functionality.

## Explanation

*   **`forms.py`:**  Defines the `MemeForm` using `forms.ModelForm`.
    *   `Meta`: Specifies the model and fields.
*   **`views.py` (updates):**
    *   `request.method == 'POST'` : Checks for form submission.
    *   `request.FILES`: Contains uploaded file data.
    *   `form.is_valid()`: Validates the form data.
    *   `form.save()`: Saves the data to the database.
    *   `redirect()`: Redirects to the meme list after successful upload.
*   **`meme_list.html` (updates):**
    *   `method="post"`:  Required for form submissions.
    *   `enctype="multipart/form-data"`: *Essential* for file uploads.
    *   `{% csrf_token %}`: CSRF protection (required for POST forms).
    *   `{{ form.as_p }}`: Renders the form fields.