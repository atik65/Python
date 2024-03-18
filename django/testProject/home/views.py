from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.models import Contact


# home view
def home(request):
    context = {"name": "John", "age": 30, "scores": [10, 20, 30, 40, 50]}
    return render(request, "home.html", context)


# about view
def about(request):
    return render(request, "about.html")


# service view
def service(request):
    return render(request, "service.html")


# contact view
def contact(request):

    # process post request
    if request.method == "POST":
        form_data = request.POST

        if form_data:
            name = form_data.get("name")
            phone = form_data.get("phone")
            description = form_data.get("description")

            if name and phone and description:
                # Save the contact to the database
                contact = Contact.objects.create(
                    name=name, phone=phone, description=description
                )

                contact.save()
                return redirect("/contact")

    # logics for get request
    all_contacts = Contact.objects.all()
    context = {"contacts": all_contacts}

    return render(request, "contact.html", context)
