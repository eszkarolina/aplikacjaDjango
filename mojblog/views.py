from django.shortcuts import render
from .models import Post, Comment, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, CategoryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render(request, 'blog/post_detail.html',
         {'post': post,
         'form': form},
         context_instance=RequestContext(request) )

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mojblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mojblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})    


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})    

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('mojblog.views.post_detail', pk=pk)    

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('mojblog.views.post_list')    

# do komentarzy
@login_required
def comment_add(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            comment.publish()
            return redirect('mojblog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Post, pk=pk)
    comment.delete()
    return redirect('mojblog.views.post_detail')


@login_required
def comment_edit(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('mojblog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form})       

  

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        posts = Post.objects.filter(category__name=q)
        return render(request, 'blog/search.html', {'posts':posts })
    else:
        return HttpResponse('Please submit a search term.')
   
