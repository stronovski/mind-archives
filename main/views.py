from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'The Mind Archive',
        'name': 'Andi Salsabila Ardian',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)