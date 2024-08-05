from django.shortcuts import render

def home_view(request):
    return render(request, 'fourth_task/home.html')

def page1_view(request):
    data = {
        'tours_list': [
            {'name': 'Путевка в Париж', 'price': '1500$'},
            {'name': 'Путевка в Токио', 'price': '2000$'},
            {'name': 'Путевка на Бали', 'price': '1200$'}
        ]
    }
    return render(request, 'fourth_task/page1.html', data)


def page2_view(request):
    data = {
        'selected_tours_list': [],
        'total_price': 0
    }
    return render(request, 'fourth_task/page2.html', data)