from django.shortcuts import render
from .forms import register_form
# Create your views here.
def test(request):
    return render(request,'base/child1.html')
def register_view(request):
    form=register_form
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            instance=form.save()
            form=register_form
    return render(request,'base/register.html',{'form':form})
def contact(re):
   return render(re,'base/contact.html')