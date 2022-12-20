from django.http import HttpResponse


def confirmar(request):
    return HttpResponse("confirmado")