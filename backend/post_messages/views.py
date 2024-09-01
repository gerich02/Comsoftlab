from django.shortcuts import render
from django.http import JsonResponse
from .models import Login


def index(request):
    return render(request, "index.html")


def add_login(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        login_instance, created = Login.objects.update_or_create(
            login=login,
            defaults={"password": password},
        )

        if created:
            return JsonResponse(
                {
                    "status": "created",
                    "message": "New login created successfully"
                }
            )
        else:
            return JsonResponse(
                {
                    "status": "updated",
                    "message": "Existing login updated successfully"
                }
            )

    return JsonResponse(
        {
            "status": "error",
            "message": "Invalid request method"
        }
    )


def get_logins(request):
    logins = Login.objects.all().values("id", "login")
    return JsonResponse({"logins": list(logins)})


def messages_page(request):
    return render(request, "messages.html")
