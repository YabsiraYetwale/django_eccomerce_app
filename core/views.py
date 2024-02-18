from django.shortcuts import render, redirect
from item.models import CatagoryModel,ItemModel
from django.contrib.auth.views import LogoutView,LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy

def index(request):
    items=ItemModel.objects.filter(isSold=False)
    catagories=CatagoryModel.objects.all()

    return render(request,'core/index.html',{
        'items':items,
        'catagories':catagories,
    })
def signUp(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request,'core/signUp.html',{
        'form':form
    })

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('core:index')
class CustomLogoutView(LogoutView):
   next_page = '/'