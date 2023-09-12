from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Roti',
        'description': 'Rasa roti manis yang kita kenal dan sayangi, bread.',
        'price' : 2000
    }

    return render(request, "main.html", context)
