from django.urls import path

from . import views

urlpatterns = [
    path("home",views.Home.as_view(),name='home'),
    path("authenticate",views.Authenticate.as_view(),name="authen"),
    path("notes",views.List.as_view(),name="notes.list"),
    path("detail/<int:pk>",views.Detail.as_view(),name="notes.detail"),
    path('create',views.CreateNode.as_view(),name='notes.create'),
    path("detail/<int:pk>/update",views.UpdateNode.as_view(),name="notes.update"),
    path("detail/<int:pk>/delete",views.DeleteNode.as_view(),name="notes.delete"),
    path("login_user",views.LoginInterfaceView.as_view(),name='login'),
    path("logout_user",views.LogoutInterfaceView.as_view(),name='logout'),
    path("signup_user",views.SignUpView.as_view(),name='signup'),
]