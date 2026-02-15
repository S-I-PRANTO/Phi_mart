from django.shortcuts import render,redirect


def root(request):
    return redirect('api-root')
# Create your views here.
