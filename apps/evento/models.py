from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

# Create your models here.

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Categoria, self).save(*args, **kwargs)

    def _unicode_(self):
        return self.name

class Evento(TimeStampModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False)
    sumary = models.TextField(max_length=255)
    content = models.TextField()
    categoria = models.ForeignKey(Categoria)
    place = models.CharField(max_length=50)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    image = models.ImageField(upload_to='evento')
    is_free = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    views = models.PositiveIntegerField(default=0)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Evento, self).save(*args, **kwargs)

    def _unicode_(self):
        return self.name

class Asistente(TimeStampModel):

    assistant = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ManyToManyField(Evento)

    attended = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)


    def _unicode_(self):
        return "%s %s" % (self.assistant.username, self.assistant.event.name)

class Comentario(TimeStampModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ForeignKey(Evento)

    content = models.TextField()


    def _unicode_(self):
        return "%s %s" % (self.user.username, self.assistant.event.name)
