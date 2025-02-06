from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # user
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/<int:pk>/", views.profilePage, name="profile"),
    path("accounts/", views.allProfiles, name="accounts"),
    # post
    path("createpost/", views.create_post_page, name="createpost"),
    path("deletepost/<int:pk>/", views.delete_post, name="deletepost"),
    # reel
    path("reels/", views.ReelPage, name="reels"),
    path("createreel/", views.Create_ReelPage, name="createreel"),
    path("deletereel/<int:pk>/", views.delete_ReelPage, name="deletereel"),
    #comment
    path("commentsforpost/<int:pk>/", views.comment_for_post, name="commentsforpost"),
    path("commentsforreel/<int:pk>/", views.comment_for_reel, name="commentsforreel"),
    path("deletecommentforpost/<int:pk>/", views.delete_comment_for_post, name="deletecommentforpost"),
    path("deletecommentforreel/<int:pk>/", views.delete_comment_for_reel, name="deletecommentforreel"),
    
    
    path("follow_unfollow/<int:pk>/", views.follow_unfollow, name="follow_unfollow"),
]
