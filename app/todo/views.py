from django.urls import reverse_lazy
from todo.models import ToDo
from django.views import generic
from todo.forms import ToDoForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'

class ToDoLoginView(LoginView):
    template_name = 'todo_login.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'todo_register.html', {'form': form})





def regist(request):
    count = User.objects.count()
    return render(request, 'registration/reg.html', {'count': count})


class IndexView(generic.TemplateView):
    template_name = 'index.html'




class TodoListView(LoginRequiredMixin, generic.ListView):

    queryset = ToDo.objects.all()
    template_name = 'todo_list.html'

    def get_queryset(self):
        super().get_queryset()
        admin_uid = self.request.user
        if not admin_uid.is_superuser:
            return ToDo.objects.filter(user=admin_uid)
        return ToDo.objects.all()



class TodoActiveListView(generic.ListView):
    # queryset = ToDo.objects.all().filter(status='Active')
    template_name = 'todo_list.html'

    def get_queryset(self):
        admin_uid = self.request.user
        if admin_uid.is_superuser:
            return ToDo.objects.filter(status='Active')
        return ToDo.objects.filter(user=admin_uid, status='Active')

class TodoCompletedListView(generic.ListView):
    # queryset = ToDo.objects.all().filter(status='Completed')
    template_name = 'todo_list.html'

    def get_queryset(self):
        admin_uid = self.request.user
        if admin_uid.is_superuser:
            return ToDo.objects.filter(status='Completed')
        return ToDo.objects.filter(user=admin_uid, status='Completed')

class TodoCreateView(generic.CreateView):
    queryset = ToDo.objects.all()
    template_name = 'todo_create.html'
    form_class = ToDoForm
    success_url = reverse_lazy('todo:todo_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(generic.UpdateView):
    queryset = ToDo.objects.all()
    template_name = 'todo_update.html'
    form_class = ToDoForm
    success_url = reverse_lazy('todo:todo_list')

class ToDoDeleteView(generic.DeleteView):
    queryset = ToDo.objects.all()
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo:todo_list')

    # def test_func(self):
    #     return self.request.user.is_superuser

class ToDoDetailView(generic.DetailView):
    queryset = ToDo.objects.all()
    template_name = 'todo_details.html'
