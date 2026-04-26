from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Post


def index(request):
    template = 'blog/index.html'
    post_list = (
        Post.objects.select_related('location', 'category', 'author')
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )[:5]
    )
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('location', 'category', 'author'),
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, p_category):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=p_category,
        is_published=True)
    post_list = (
        Post.objects.select_related('location', 'category', 'author')
        .filter(
            is_published=True,
            category__slug=p_category,
            pub_date__lte=timezone.now()
        )[:10]
    )
    context = {
        "post_list": post_list,
        "category": category
    }
    return render(request, template, context)
