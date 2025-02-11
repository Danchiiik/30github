from django.db import models




class Cards(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')  # Main thumbnail image
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')


    def __str__(self) -> str:
        return self.name


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

