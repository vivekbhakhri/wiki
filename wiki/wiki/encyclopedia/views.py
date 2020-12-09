from django.shortcuts import render
from django.http import HttpResponse

from . import util

from markdown2 import Markdown

markdowner = Markdown()


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    page = util.get_entry(title)
    
    if page is None:
        return HttpResponse("Page Not Found")
    body = markdowner.convert(page)
    return render(request, "encyclopedia/topic.html", {
        "title": title,
        "titleBody": body
    })

