from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone
from django.http import HttpResponseRedirect


def home(request):
    products=Product.objects
    return render(request, 'products/home.html',{'products': products})

@login_required(login_url='/accounts/login')
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            product.url=request.POST['url']
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/products/'+ str(product.id))
 

        else:
            return render(request, 'products/create', {'error':'All fileds are required'}) 
    else:
        return render(request, 'products/create.html')
@login_required(login_url='/accounts/login')
def detail(request, product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html',{'product':product})

@login_required(login_url='/accounts/login')
def upvote(request, product_id):
    if request.method=='POST':
        product=get_object_or_404(Product, pk=product_id)
        product.votes_total+=1
        product.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def profile(request):
    current_user=request.user
    user_id=str(current_user.id)
    user_name=str(current_user.username)
    print(user_name)
    products=Product.objects.filter(hunter__id=user_id)

    return render(request, 'products/profile.html',{'products':products,'name':user_name})


# Create your views here.
