from django.shortcuts import render


def create_page(request):
    return render(request, 'create.html')


def list_page(request):
    return render(request, 'list.html')
