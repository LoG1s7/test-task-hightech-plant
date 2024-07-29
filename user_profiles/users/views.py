from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render

from users.models import User


@login_required
def user_list(request):
    try:
        users = User.objects.all()
        return render(request, "users/user_list.html", {"users": users})
    except DatabaseError:
        messages.error(request, "Ошибка загрузки списка пользователей.")
        return render(request, "users/user_list.html", {"users": []})


@login_required
def user_profile(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        return render(request, "users/user_profile.html", {"user": user})
    except User.DoesNotExist:
        messages.error(request, "Пользователь не найден.")
        return redirect("user_list")


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        try:
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            messages.success(request, "Профиль успешно обновлен.")
            return redirect("user_profile", user_id=user.id)
        except DatabaseError:
            messages.error(request, "Ошибка сохранения профиля.")
    return render(request, "users/edit_profile.html", {"user": user})
