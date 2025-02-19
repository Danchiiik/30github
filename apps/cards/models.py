from django.db import models



GENDER = (
    ('male', 'male'),
    ('female', 'female')
)

DEGREES = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('PhD', 'PhD')
)

STATUS_OF_STUDIES = (
    ('In process', 'In process'),
    ('Finished', 'Finished')
)


class Cards(models.Model):

    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')  # Main thumbnail image

    country = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER, max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    name_father = models.CharField(max_length=30)
    surname_father = models.CharField(max_length=50)
    name_mother = models.CharField(max_length=30)
    surname_mother = models.CharField(max_length=50)
    siblings = models.PositiveIntegerField(default=0)

    degree = models.CharField(choices=DEGREES, max_length=15)
    previous_school = models.CharField(max_length=200)
    status_of_studies = models.CharField(choices=STATUS_OF_STUDIES, max_length=15)
    graduation = models.DateTimeField()
    study_country = models.CharField(max_length=50)
    study_address = models.CharField(max_length=100)
    study_language = models.CharField(max_length=50)
    gpa = models.FloatField()


    wanted_degrees = models.CharField(choices=..., max_length=200)
    wanted_countries = models.CharField(choices=..., max_length=200)
    financial_support = models.BooleanField(default=False)


    essay = models.CharField(max_length=5000, null=True, blank=True)
    diploma = models.FileField()
    documents = models.FileField()


    

    

    

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


# class Events(models.Model):
#     name = models.CharField(max_length=150)
#     image = models.FileField(upload_to='images/')  # Main thumbnail image
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
#     description = models.TextField(null=True, blank=True, max_length=2500)
#     region = models.CharField(max_length=50, choices=REGION)
#     address = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     type_of_event = models.CharField(max_length=50, choices=TYPE_OF_EVENT)
#     type = models.CharField(max_length=50, choices=TYPE)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     video = models.FileField(upload_to='videos/', null=True, blank=True)  # New field for video

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         verbose_name = 'Мероприятие'
#         verbose_name_plural = 'Мероприятия'

