from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import ItemModel,CatagoryModel
from .forms import ItemForm

def items(request):
    query = request.GET.get('query', '')
    catagory_id = request.GET.get('catagory', 0)
    catagories = CatagoryModel.objects.all()
    items = ItemModel.objects.filter(isSold=False)

    if catagory_id:
        items = items.filter(catagory_id=catagory_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'catagories': catagories,
        'catagory_id': int(catagory_id)
    })

@login_required
def createItem(request):
    if request.method=='POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.creator=request.user
            item.save()
            return redirect('/')
    else:
        form=ItemForm()
    return render(request,'item/create_item.html',{'form':form})

def detail(request,pk):
    item=get_object_or_404(ItemModel,pk=pk)
    related_items=ItemModel.objects.filter(catagory=item.catagory,isSold=False).exclude(pk=pk)
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })
@login_required
def editItem(request,pk):
    item=get_object_or_404(ItemModel,pk=pk,creator=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:item', pk=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request,'item/create_item.html',{
        'form':form,
    })
@login_required
def deleteItem(request,pk):
    item=get_object_or_404(ItemModel,pk=pk,creator=request.user)
    item.delete()
    return redirect('/')