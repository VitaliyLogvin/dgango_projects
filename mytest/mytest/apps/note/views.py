from models import Note
from annoying.decorators import render_to


@render_to("note.html")
def note_page(request):
    notes = Note.objects.all()
    page_name = "Note"
    return {"notes": notes, "page_title": page_name}
