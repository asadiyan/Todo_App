from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

# importing generic views

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.
# we have 2 kinds of views one is function based view the other one is class based view or generic views
# generic views has 4 kinds listView, detailView, updateView and deleteView
# if we want to create one of them we should import it first


class TaskListView(ListView):
    # we choose our class name but class should inherit from ListView class
    model = Task
    template_name = "myapp/index.html"
    context_object_name = "task_list"
    # after these all instructions we should have path in urls.py like function based views
    # so we go to urls.py and we create a path


class TaskDetailView(DetailView):
    model = Task
    template_name = "myapp/detail.html"
    context_object_name = "task"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "myapp/update.html"
    context_object_name = "task"
    fields = ("name", "priority", "date")

    # this function makes that after we update or edited the task goes back to that task detail page
    # we pass a url as cbvdetail but we need a id of that task to show that task detail page
    # we pass a primary key like pk to it and pk is self.object.id
    # self means this task
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "myapp/delete.html"
    # success_url is the url after deleting task page will go there
    # reverse_lazy is module we imported it at top
    success_url = reverse_lazy("cbvindex")


def add(request):
    if request.method == "POST":
        # we check if submit buttom is activing post method then:
        # we get the name and priority from form in add.html and save
        # it in variable
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")
        date = request.POST.get("date", "")
        # these name and priority inside "" are the same names in input field at add.html

        # so we create an object out of the data we have
        # the reason for creating an object is to save the object inside data base
        # the object should be the type of task which we create it in models.py
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect("/")

    # for the first view we create we pass a html file to render function
    # we go inside our myapp folder we create templates folder
    # and we create myapp folder inside templates folder then we put our
    # add.html file inside myapp folder for other veiws we just create html file near this file

    return render(request, "myapp/add.html")


# this view is function based view.
def index(request):

    # we create a object of all tasks we have saved in data base
    task_list = Task.objects.all()
    # we create a context of that then we can pass it to html file we have index.html
    context = {
        "task_list": task_list,
    }

    if request.method == "POST":
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")
        date = request.POST.get("date", "")
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect("/")

    return render(request, "myapp/index.html", context)


def delete(request, taskid):

    task = Task.objects.get(id=taskid)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    return render(request, "myapp/delete.html", {"task": task})


def edit(request, taskid):
    task = Task.objects.get(id=taskid)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "myapp/edit.html", {"form": form, "task": task})
