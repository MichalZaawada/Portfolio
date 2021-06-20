from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'base.html')

@csrf_exempt
def nav(request):
    html = render_to_string('partials/_navbar.html')
    return HttpResponse(html)

@csrf_exempt
def change(request):
    html = render_to_string('about_me.html')
    return HttpResponse(html)

@csrf_exempt
def contact(request):
    html = render_to_string('contact.html')
    return HttpResponse(html)

@csrf_exempt
def projects(request):
    html = render_to_string('projects.html')
    return HttpResponse(html)

@csrf_exempt
def index(request):
    html = render_to_string('index.html')
    return HttpResponse(html)

@csrf_exempt
def nav_en(request):
    html = render_to_string('partials/_navbar_en.html')
    return HttpResponse(html)
@csrf_exempt
def change_en(request):
    html = render_to_string('about_me_en.html')
    return HttpResponse(html)

@csrf_exempt
def contact_en(request):
    html = render_to_string('contact_en.html')
    return HttpResponse(html)

@csrf_exempt
def projects_en(request):
    html = render_to_string('projects_en.html')
    return HttpResponse(html)

@csrf_exempt
def index_en(request):
    html = render_to_string('index_en.html')
    return HttpResponse(html)