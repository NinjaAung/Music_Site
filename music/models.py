from django.db import models
# Create your models here.

# python manage.py createsuperuser

class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(null=True)

    # allows us to see the objects as a string
    def __str__(self):
        return self.name 

class Song(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    # allows us to see the objects as a string
    def __str__(self):
        return self.name 


class Creator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField(Creator, through=("Subscription"))

    def __str__(self):
        return self.name

class Subscription(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    day_joined = models.DateField(null=True)

    def __str__(self):
        return self.creator




# In class 

# class Event(models.Model):
#     name = models.CharField(max_length=50)
#     date = models.DateTimeField()
#     attendee = models.ManyToManyField(Attendee, through='ticket')
    
#     def __str__(self):
#         return self.name 

# class Attendee(model.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
   

#     def __str__(self):
#         return self.name 

# class Ticket(models.Model):
#     price = models.DecimalField(decimal_places=2, max_digits=6)
#     event = models.ForeignKey(Event, on_delete=models.cascade)
#     attendee = models.ForeignKey(Event, on_delete=models.cascade)

#     def __str__(self):
#         return self.event.name + "for" + self.attendee.name

