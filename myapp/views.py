from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    items = Item.objects.all()

    #search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        items = items.filter(name__icontains=item_name)




    #pages
    paginator = Paginator(items,6)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request,'myapp/index.html',{'items':items})

def detail(request,id):
    item = Item.objects.get(id=id)

    return render(request,'myapp/detail.html',{'item':item})