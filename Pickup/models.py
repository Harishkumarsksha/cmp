from django.db import models
from django.contrib.auth.models import User
from CustomerData.models import CSR


class PickUp(models.Model):
    FUEL_CHOSE = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('3', '3'), ('4', '4'),
    )

    odoMetervalue = models.DecimalField(
        max_digits=5, decimal_places=0, null=True, blank=True)
    fuelLevel = models.CharField(
        max_length=7, default=('1', '1'), choices=FUEL_CHOSE, null=True, blank=True)
    cdPlayer = models.BooleanField(default=False)
    cigrateCharger = models.BooleanField(default=False)
    toolKit = models.BooleanField(default=False)
    serviceBook = models.BooleanField(default=False)
    clock = models.BooleanField(default=False)
    perfume = models.BooleanField(default=False)
    jack = models.BooleanField(default=False)
    spareWheel = models.BooleanField(default=False)
    mats = models.BooleanField(default=False)
    dickyMat = models.BooleanField(default=False)
    bodyCover = models.BooleanField(default=False)
    antenna = models.BooleanField(default=False)
    remote = models.BooleanField(default=False)
    image1 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image4 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image5 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    customerRemarks = models.TextField(null=True, blank=False)
    # customerSignature = models.JSignatureField()

    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING, null=True, blank=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.customerRemarks
