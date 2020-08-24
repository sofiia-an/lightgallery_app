from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from gallery.models import gallery, Image
from gallery.forms import ImageForm

def imagedisplay(request):
    resultsdisplay = gallery.objects.all()
    return render(request, 'index.html', {'gallery': resultsdisplay})

def IndexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        picture_display = Image.objects.all()
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'dashboard.html', {'form':form, 'img_obj':img_obj, 'Image':picture_display})
    else:
        form = ImageForm()
    return render(request, 'dashboard.html',{'form':form})



def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        pic_info = Image.objects.all().filter(title=search)
        return render(request,'searchbar.html',{'pic_info':pic_info})