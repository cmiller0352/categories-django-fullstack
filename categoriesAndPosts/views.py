from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post
from .forms import CategoryForm, PostForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categoriesAndPosts/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categoriesAndPosts/category_detail.html', {'category': category})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categoriesAndPosts/category_form.html', {'form': form, 'type_of_request': 'New'})

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categoriesAndPosts/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


def new_post(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk, post.pk)
    else:
        form = PostForm()
    return render(request, 'categoriesAndPosts/new_post.html', {'form': form, 'type_of_request': 'New'})
  

def post_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category = pk)
    data = { 'posts' : posts, 'category' : category}
    return render(request, 'categoriesAndPosts/posts.html', data)


def post_detail(request, pk, fk):
    post = get_object_or_404(Post, pk=pk)
    print({pk})
    return render(request, 'categoriesAndPosts/post_detail.html', {'post': post})
    

def edit_post(request, pk, fk):
    post = get_object_or_404(Post, fk=fk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print({post.fk})
            return redirect('post_detail', fk=post.fk)
    else:
        form = PostForm(instance=post)
    return render(request, 'categoriesAndPosts/post_form.html', {'form': form, 'type_of_request': 'Edit'})
    

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('category_list')
