from django.shortcuts import render, redirect, get_object_or_404
from.models import Hc
from django.utils import timezone
# Create your views here.
def home(request):
    hc = Hc.objects.all()
    return render(request, 'home.html', {'hc':hc})

def detail(request, id):
    hc = get_object_or_404(Hc, pk=id)
    return render(request, 'detail.html', {'hc':hc})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_hc = Hc()
    new_hc.name = request.POST['name']
    new_hc.age = request.POST['age']
    new_hc.pub_date = timezone.now()
    new_hc.email = request.POST['email']
    new_hc.introduce = request.POST['introduce'] 
    new_hc.like = request.POST['like']
    new_hc.image = request.FILES['image']
    new_hc.save()
    return redirect('detail', str(new_hc.id))

def edit(request, id):
    edit_hc = Hc.objects.get(pk=id)
    return render(request, 'edit.html', {'hc':edit_hc})

def update(request, id):
    update_hc = Hc.objects.get(pk=id)
    update_hc.name = request.POST['name']
    update_hc.age = request.POST['age']
    update_hc.pub_date = timezone.now()
    update_hc.email = request.POST['email']
    update_hc.introduce = request.POST['introduce'] 
    update_hc.like = request.POST['like']
    update_hc.image = request.FILES['image']
    update_hc.save()
    return redirect('detail', str(update_hc.id))

def delete(request, id):
    delete_hc = Hc.objects.get(pk=id)
    delete_hc.delete()
    return redirect('home')

def ee(request):
    return render(request, 'ee.html')