from django.shortcuts import render
from django.http import HttpResponse


def leo(request):
    return HttpResponse("Знак зодиака Лев")


def scorpio(request):
    return HttpResponse("Знак зодиака Скорпион")
