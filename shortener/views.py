from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Url
from django.core.exceptions import ValidationError
import uuid


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        shortened_url = Url(link=url, uuid=uid)
        try:
            shortened_url.clean_fields()
        except ValidationError as e:
            return HttpResponseNotFound(e)
        shortened_url.save()
        return HttpResponse(uid)
    return redirect('/')


def go(request, pk):
    try:
        new_url = Url.objects.get(uuid=pk)
    except Url.DoesNotExist:
        return redirect('/')
    return redirect(new_url.link)
