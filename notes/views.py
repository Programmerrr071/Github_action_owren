from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/list.html', {'notes': Note.objects.all(), 'form': form})


def note_toggle(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.done = not note.done
        note.save()
    return redirect('note_list')


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
    return redirect('note_list')
