from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .forms import bookForm
from django.db.models import Q
# Create your views here.



class home(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'lists'
    paginate_by = 2


class create(CreateView):
    model = Book
    template_name = 'create.html'
    context_object_name = 'book'
    form_class = bookForm
    success_url = '/'

class detail(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

class update(UpdateView):
    model = Book
    form_class = bookForm
    template_name = 'update.html'
    success_url = '/'

class delete(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = '/'

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            books = Book.objects.filter(Q(title__icontains=keyword) | Q(publisher_name__icontains=keyword))
            books_count = books.count()
            
            context = {
                'lists' : books,
                'books_count' : books_count,
                'keyword' : keyword
                
            }
    return render(request,'list.html',context)
