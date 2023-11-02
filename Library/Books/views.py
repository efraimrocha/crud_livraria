from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def index(request):
    
    books = Book.objects.all()
    
    context = {
        'books': books
    }
    return render(request,'index.html', context)

def create(request):
    
    if request.method == 'GET':
        form = BookForm()
        
        context = {
            'form': form,
        }
        
        return render(request,'criar.html',context=context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        
        

def refresh(request, user_id):
    
    user = Book.objects.get(pk=user_id)
    
    if request.method == 'POST':
        form = BookForm(data=request.POST,instance=user)
        
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = BookForm(instance=user)
        
        context = {'form': form}
        
        return render(request,'criar.html', context=context)
    
def delete(request, user_id):
    
    user = Book.objects.get(pk=user_id)
    user.delete()
    
    return redirect(index)