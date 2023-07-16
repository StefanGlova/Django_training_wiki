from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def select_entry(request, title):
    to_display = util.get_entry(title=title)
    if to_display is None:
        return render(request, "encyclopedia/error_entry_not_found.html")
    
    return render(request, "encyclopedia/entry.html", {"entry": to_display})

