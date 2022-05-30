from tkinter import EW
from django.shortcuts import get_object_or_404, render, redirect
from .models import Board, Comment
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

# 자게 html
def freeBoard(request):
    posts = Board.objects.filter().order_by('-date')
    paginator = Paginator(posts, 10)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'freeBoard.html', {'posts':posts})


def graduateBoard(request):
    return render(request, 'graduateBoard.html')


def create(request):
    if request.method == 'POST':
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['text']
        post.file = request.FILES.get('file')
        post.user = request.user
        post.date = timezone.now()
        post.save()
        return redirect('freeBoard')
    else:
        return render(request, 'freeBoard.html')


def detail(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    return render(request, 'freeBoardDetail.html', {'post_detail':post_detail})


def createComment(request, post_id):
    post = get_object_or_404(Board, pk = post_id)
    if request.method == 'POST':
        cmt = Comment()
        cmt.comment = request.POST['comment']
        cmt.date = timezone.now()
        cmt.user = request.user
        cmt.post = post
        cmt.save()
    return redirect('detail', post_id=post_id)
    

def update(request, post_id):
    post_detail = get_object_or_404(Board, pk = post_id)
    if request.method == 'POST':
        post_detail.title = request.POST['title']
        post_detail.content = request.POST['content']
        post_detail.file = request.FILES.get('file') or post_detail.file
        post_detail.date = timezone.now()
        post_detail.save()
        return redirect('/freeBoard/'+str(post_id), {'post_detail': post_detail})
    else:
        return render(request, 'freeBoardUpdate.html', {'post_detail': post_detail})
    
    
def delete(request, post_id):
    post = get_object_or_404(Board, pk = post_id)
    post.delete()
    return redirect('freeBoard')


def updateComment(request, post_id, comment_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == 'POST':
        comment.comment = request.POST['title']
        comment.save()
        return redirect(f'/freeBoard/{post_id}')
    else:
        return render(request, 'freeBoardDetailUpdate.html', {'post_detail': post_detail})
    
    
def deleteComment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect(f'/freeBoard/{post_id}')