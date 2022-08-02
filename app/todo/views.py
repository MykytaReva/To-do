from django.urls import reverse_lazy
from todo.models import ToDo
from django.views import generic
from todo.forms import ToDoForm



class IndexView(generic.TemplateView):
    template_name = 'index.html'


class TodoListView(generic.ListView):
    queryset = ToDo.objects.all()
    template_name = 'todo_list.html'

class TodoActiveListView(generic.ListView):
    queryset = ToDo.objects.all().filter(status='Active')
    template_name = 'todo_list.html'

class TodoCompletedListView(generic.ListView):
    queryset = ToDo.objects.all().filter(status='Completed')
    template_name = 'todo_list.html'


class TodoCreateView(generic.CreateView):
    queryset = ToDo.objects.all()
    template_name = 'todo_create.html'
    form_class = ToDoForm
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(generic.UpdateView):
    queryset = ToDo.objects.all()
    template_name = 'todo_update.html'
    form_class = ToDoForm
    success_url = reverse_lazy('todo_list')

class ToDoDeleteView(generic.DeleteView):
    queryset = ToDo.objects.all()
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')

class ToDoDetailView(generic.DetailView):
    queryset = ToDo.objects.all()
    template_name = 'todo_details.html'
