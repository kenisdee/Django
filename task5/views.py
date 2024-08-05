from django.shortcuts import render
from .forms import UserRegisterForm

# Псевдо-список существующих пользователей
existing_users = ["user1", "user2", "user3"]


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in existing_users:
                info['error'] = "Пользователь уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            elif age < 18:
                info['error'] = "Вы должны быть старше 18."
            else:
                info['success'] = f"Приветствуем, {username}!"
    else:
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age')) if request.POST.get('age').isdigit() else 0

        if username in existing_users:
            info['error'] = "Пользователь уже существует."
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают."
        elif age < 18:
            info['error'] = "Вы должны быть старше 18."
        else:
            info['success'] = f"Приветствуем, {username}!"

    return render(request, 'fifth_task/registration_page.html', info)