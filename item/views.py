from django.shortcuts import render, redirect, get_object_or_404
from .models import Mate, Maker
from .forms import ItemForm

def list_item(request):
    qs = Mate.objects.all()
    return render(request, 'item/list_item.html', {
        'item_list': qs,
    })

def create_item(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('list_item')
    else:
        form = ItemForm(instance=item)

    return render(request, 'item/create_item.html', {
        'form': form,
    })

def detail_item(request, pk):
    item = get_object_or_404(Mate, pk=pk)
    return render(request,'item/detail_item.html', {
        'item': item,
    })

def delete_item(request, pk):
    item = Mate.objects.get(id=pk)

    if request.method == 'GET':
        return redirect('detail_item', item.id)

    elif request.method == 'POST':
        item.delete()
        return redirect('list_item')

def update_item(request, pk):
    item = Mate.objects.get(id=pk)

    if request.method == 'GET':
        return render(request, 'item/update_item.html', {'item': item})
    elif request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        price = request.POST['price']
        leftover = request.POST['leftover']

        item.name = name
        item.desc = desc
        item.price = price
        item.leftover = leftover

        item.save()
        return redirect('detail_item', item.id, )

def list_maker(request):
    qs = Maker.objects.all()
    return render(request, 'item/list_maker.html', {
        'maker_list': qs,
    })

def detail_maker(request, pk):
    maker = get_object_or_404(Maker, pk=pk)
    return render(request,'item/detail_maker.html', {
        'maker': maker,
    })

def create_maker(request):
    if request.method == 'GET':
        return render(request, 'item/create_maker.html')

    elif request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        maker = Maker.objects.create(name=name, phone=phone, address=address)
        return redirect('detail_maker', maker.id)

def update_maker(request, pk):
    maker = Maker.objects.get(id=pk)

    if request.method == 'GET':
        return render(request, 'item/update_maker.html', {'maker': maker})
    elif request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        maker.name = name
        maker.phone = phone
        maker.address = address

        maker.save()
        return redirect('detail_maker', maker.id)

def delete_maker(request, pk):
    maker = Maker.objects.get(id=pk)

    if request.method == 'GET':
        return redirect('detail_maker', maker.id)

    elif request.method == 'POST':
        maker.delete()
        return redirect('list_maker')