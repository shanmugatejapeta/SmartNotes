from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
# from django.http import HttpResponse,Http404

# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime

from .models import Notes
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm

from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name='home/signup.html'
    success_url='notes'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args,*kwargs)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'



class Home(TemplateView):
    template_name="home/welcome.html"
    extra_context ={"tday":datetime.today()}

class Authenticate(LoginRequiredMixin,TemplateView):
    template_name='home/authenticate.html'
    login_url='/admin'

class List(LoginRequiredMixin,ListView):
    template_name="note1.html"
    context_object_name="notes"
    model=Notes
    login_url='/admin'

    def get_queryset(self) -> QuerySet[Any]:
        return self.request.user.notes.all()

class Detail(LoginRequiredMixin,DetailView):
    template_name="home/note.html"
    model=Notes
    context_object_name="note"
    login_url='/admin'

class CreateNode(LoginRequiredMixin,CreateView):
    model=Notes
    form_class=NotesForm   # fields=["title",'para']
    success_url='notes'
    # template_name='form_notes.html' ----->defautl is home/notes_form.html. We can change if we need.
    login_url='/admin'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UpdateNode(LoginRequiredMixin,UpdateView):
    model=Notes
    form_class=NotesForm
    success_url='../../notes'
    template_name='home/notes_update.html'
    login_url='/admin'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteNode(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url='../../notes'
    template_name='home/notes_delete.html'
    context_object_name='note'
    login_url='/admin'













# # Create your views here.
# def home(request):
#     return render(request,"home/welcome.html",{"tday":datetime.today()})

# @login_required(login_url="/admin")
# def authenticate(request):
#     return HttpResponse("You are in resticted Area!!!")

# def detail(request):
#     try:
#         note=Notes.objects.all()
#     except Notes.DoesNotExist:
#         raise Http404("Data Not Found")
#     return render(request,"note1.html",{"note":note})

