from django.shortcuts import render
from django.http import HttpResponse

from . import util

from markdown2 import Markdown

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request):
    return HttpResponse("I'm working")

def entry(request, title):
    page = util.get_entry(title)
    
    if page is None:
        return HttpResponse("Page Not Found")
    body = markdowner.convert(page)
    return render(request, "encyclopedia/topic.html", {
        "title": title,
        "titleBody": body
    })

