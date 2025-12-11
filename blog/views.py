from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .models import Post, Category


def index(request):
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
        & Q(category__is_published=True)
    ).order_by('-pub_date')[:5]

    return render(request, 'blog/index.html', {'post_list': post_list})


def category(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        Q(category=category)
        & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
    ).order_by('-pub_date')

    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        Q(id=id)
        & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
        & Q(category__is_published=True)
    )

    return render(request, 'blog/detail.html', {'post': post})
