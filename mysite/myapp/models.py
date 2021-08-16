from django.db import models
import datetime

# Create your models here.


class Task(models.Model):

    # this function here will show us the name of object in the admin panel not object 1 or 2 or..
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    # when we had create the models we have to make migrations but before of that we should go to setting.py to see if have add the myapp in there
    # if we dont add our migrations wont work so we should add our app name to settings.py
    # then we go to consle and type python manage.py makemigrations thrn we type python manage.py migrate
    # after this we can see our models or tables in backend site by having a superuser
    # for creating super user we type python manage.py createsuperuser then we give our username email address and pasword
    # now we run server and we go to localhost:8000/admin page and there we give our user and pasword after that we are loged in
    # but first we should add our models to admin.py by importing our models.py
    # then we register our model by typing admin.site.register(Task"our class name")
