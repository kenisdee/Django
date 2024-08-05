from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/home.html')

def page1_view(request):
    tours = [
        {'name': 'Путевка в Париж', 'price': '1500$'},
        {'name': 'Путевка в Токио', 'price': '2000$'},
        {'name': 'Путевка на Бали', 'price': '1200$'}
    ]
    context = {'tours': tours}
    return render(request, 'third_task/page1.html', context)

def page2_view(request):
    selected_tours = []
    total_price = sum(int(tour['price'].replace('$', '')) for tour in selected_tours)
    context = {'selected_tours': selected_tours, 'total_price': total_price}
    return render(request, 'third_task/page2.html', context)