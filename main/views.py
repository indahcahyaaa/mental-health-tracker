from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245453',
        'name': 'Indah Cahya Puspitahati',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)