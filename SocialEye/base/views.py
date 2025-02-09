from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import CreateNewUser, CreatePost
from .models import Post, Reel, Comment_For_Post, Comment_For_Reel, Follow
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created")
    comments = Comment_For_Post.objects.all().order_by("-created")
    context = {"posts": posts, "comments": comments}
    return render(request, "home.html", context)


# register
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")  

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print(request, "Invalid username or password")

    return render(request, "login.html")


def register(request):
    form = CreateNewUser()
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


@login_required()
def logoutPage(request):
    logout(request)
    return redirect("home")


# profile
@login_required(login_url="login")
def profilePage(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(user=user).order_by("-created")
    reels = Reel.objects.filter(user=user).order_by("-created")
    context = {"user": user, "posts": posts, "reels": reels}
    return render(request, "profile.html", context)


@login_required(login_url="login")
def allProfiles(request):
    all_users = User.objects.all()
    context = {"users": all_users}
    return render(request, "Accounts_page.html", context)


# post
@login_required(login_url="login")
def posts_page(request):
    posts = Post.objects.all().order_by("-created")
    context = {"posts": posts}
    return render(request, "posts.html", context)


@login_required(login_url="login")
def create_post_page(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        photo = request.FILES.get("photo")
        description = request.POST.get("description")
        post = Post(user=user, title=title, photo=photo, description=description)
        post.save()
        return redirect("home")
    return render(request, "createpost.html")


@login_required(login_url="login")
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("home")


# reel


@login_required(login_url="login")
def ReelPage(request):
    reels = Reel.objects.all().order_by("-created")
    comments = Comment_For_Reel.objects.all().order_by("-created")

    context = {"reels": reels, "comments": comments}

    return render(request, "reel_page.html", context)


@login_required(login_url="login")
def Create_ReelPage(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        reel_file = request.FILES.get("reel_file")
        print(reel_file)
        description = request.POST.get("description")
        reel_instance = Reel(
            user=user, title=title, reel=reel_file, description=description
        )
        reel_instance.save()
        return redirect("reels")
    return render(request, "create_reel_page.html")


@login_required(login_url="login")
def delete_ReelPage(request, pk):
    reel = Reel.objects.get(id=pk)
    reel.delete()
    return redirect("reels")


# comment
@login_required(login_url="login")
def comment_for_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment_For_Post.objects.filter(post=post).order_by("-created")

    if request.method == "POST":
        comment = request.POST.get("comment").strip()
        if comment:
            create_comment = Comment_For_Post(
                user=request.user, post=post, comment=comment
            )
            create_comment.save()

    for_c = "post"
    context = {"comments": comments, "for_c": for_c}

    return render(request, "comments_for.html", context)


@login_required(login_url="login")
def comment_for_reel(request, pk):
    reel = get_object_or_404(Reel, id=pk)
    comments = Comment_For_Reel.objects.filter(reel=reel).order_by("-created")

    if request.method == "POST":
        comment = request.POST.get("comment").strip()
        if comment:
            create_comment = Comment_For_Reel(
                user=request.user, reel=reel, comment=comment
            )
            create_comment.save()

    for_c = "reel"
    context = {"comments": comments, "for_c": for_c}

    return render(request, "comments_for.html", context)


@login_required(login_url="login")
def delete_comment_for_post(request, pk):
    comment = get_object_or_404(Comment_For_Post, id=pk)
    comment.delete()
    return redirect(request.META.get("HTTP_REFERER", "home"))


@login_required(login_url="login")
def delete_comment_for_reel(request, pk):
    comment = get_object_or_404(Comment_For_Reel, id=pk)
    comment.delete()
    return redirect(request.META.get("HTTP_REFERER", "home"))


@login_required(login_url="login")
def follow_unfollow(request, pk):
    following_user = get_object_or_404(User, id=pk)
    follow_obj, created = Follow.objects.get_or_create(
        follower=request.user, following=following_user
    )

    if not created:
        follow_obj.delete()
        return JsonResponse({"message": "Unfollowed", "status": "unfollow"})

    return JsonResponse({"message": "followed", "status": "follow"})
