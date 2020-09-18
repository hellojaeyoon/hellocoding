from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    review_l = Review.objects.order_by('-pk')
    paginator = Paginator(review_l, 3)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    context = {
        'reviews': reviews,
        'posts' : posts,
    }
    return render(request, 'community/review_list.html', context)
    # context = {
    #     'reviews': reviews,
    # }
    # return render(request,'community/review_list.html',context)

def form(request):
    if request.method == 'POST':
        mold = ReviewForm(request.POST)
        if mold.is_valid():
            mold.save()
            return redirect('community:review_list')
    
    else:
        mold = ReviewForm()
    context = {
        'mold': mold,
    }
    return render(request, 'community/form.html',context)

def update(request,pk):
    moldform = Review.objects.get(pk=pk)
    if request.method == 'POST':
        mold = ReviewForm(request.POST, instance=moldform)
        if mold.is_valid():
            mold.save()
            return redirect('community:review_list')
    
    else:
        mold = ReviewForm(instance=moldform)
    context = {
        'mold': mold,
    }
    return render(request, 'community/form.html',context)

def detail(request,pk):
    mold = Review.objects.get(pk=pk)
    context = {
        'mold': mold,
    }
    return render(request, 'community/review_detail.html',context)

def delete(request, pk):
    mold = Review.objects.get(pk=pk)
    mold.delete()
    return redirect('community:review_list')