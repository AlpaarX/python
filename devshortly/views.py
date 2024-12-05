from django.shortcuts import render, HttpResponse, redirect
from .models import URL
from .forms import ShortenForm


def shorten(request):
    if request.method == "POST":
        form = ShortenForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data.get("url")  # Extract the URL from the form
            # Check if the URL already exists in the database
            existing_url = URL.objects.filter(url=url).first()

            if existing_url:
                # If the URL already exists, return it with a message
                return render(
                    request,
                    "shorten.html",
                    {
                        "form": form,
                        "message": f"The URL already exists: {existing_url.slug}",
                        "slug": existing_url.slug,
                    },
                )
            else:
                # Save the new URL if it doesn't exist
                new_url = form.save()
                return render(
                    request,
                    "shorten.html",
                    {
                        "form": form,
                        "slug": new_url.slug,
                        "message": "URL successfully shortened!",
                    },
                )

    # For GET requests, just render an empty form
    form = ShortenForm()
    return render(request, "shorten.html", {"form": form})


def slug_redirect(request, slug):
    try:
        url = URL.objects.filter(slug=slug).first()
        return redirect(url.url)
    except:
        return HttpResponse("URL not found")
