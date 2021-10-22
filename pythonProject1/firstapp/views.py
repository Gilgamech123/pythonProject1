from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.http import HttpResponseRedirect
class PageHome(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context=context)
class PageIndex(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)
# Create your views here.
class PageRegistration(View):
    def get(self, request):
        context = {}
        return render(request, 'registration.html', context=context)
class PageLogin(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)
class PageDogovor(View):
    def get(self, request):
        context = {}
        return render(request, 'dogovor.html', context=context)