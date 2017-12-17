from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    #Item.objects.filter(id=2).delete()
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request):
    items =Item.objects.all()
    return render(request, 'list.html',{'items':items})
