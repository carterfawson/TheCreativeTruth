from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

def home(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        '../../TheCreativeTruth/templates/index.html',
        context
    )

def about(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        '../../TheCreativeTruth/templates/about.html',
        context
    )

def post(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        '../../TheCreativeTruth/templates/blog/post.html',
        context
    )

# Create your views here.
