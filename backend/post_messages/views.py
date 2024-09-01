from django.shortcuts import render
from django.http import JsonResponse
from .models import Login


def index(request):
    return render(request, "index.html")


def add_login(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        if not login:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Login is required"
                }
            )

        login_instance, created = Login.objects.update_or_create(
            login=login,
            defaults={"password": password},
        )

        return JsonResponse({
            "status": "created" if created else "updated",
            "message": "Login added successfully",
            "login_id": login_instance.id
        })

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
