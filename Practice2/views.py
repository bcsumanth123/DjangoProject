from django.http import HttpResponse


def home(request):
    return HttpResponse('this is even number')


def even_home(request):
    global i
    for i in range(10):
        if i % 2 == 0:
            print(i)
    return HttpResponse(f'<h1>print even number{i}</h1>')
