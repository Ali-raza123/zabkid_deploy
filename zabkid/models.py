# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False, )

    def __str__(self):
        return self.file.name


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False, )
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact_number = models.CharField(max_length=45)
    cnic = models.CharField(max_length=45)
    status = models.CharField(max_length=45,null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'driver'


class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False, )
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contactno = models.CharField(max_length=45, unique=True)
    cnic = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'parent'


class Childrens(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=True, null=True, )
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    Class = models.CharField(max_length=45)
    pickup_time = models.CharField(max_length=45)
    dropoff_time = models.CharField(max_length=45)
    pickup_location = models.CharField(max_length=45)
    dropoff_location = models.CharField(max_length=45)
    age = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'childrens'


class Online_Ride(models.Model):
    id = models.AutoField(primary_key=True)
    children = models.ForeignKey(Childrens, on_delete=models.CASCADE, null=True, related_name='ride_childrens')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, to_field='id', null=True, related_name='ride_driver')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, to_field='id', null=True, related_name='ride_parent')
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'driver_children'


class Ride_history(models.Model):
    id = models.AutoField(primary_key=True)
    children = models.ForeignKey(Childrens, on_delete=models.CASCADE, null=True, related_name='children')
    parent_id = models.IntegerField()
    pickuplocation = models.CharField(max_length=45)
    dropofflocation = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    time = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ride_history'


class Add_Ride_history(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    children_id = models.IntegerField()
    pickuplocation = models.CharField(max_length=45)
    dropofflocation = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    time = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ride_history'


class Assign_driver(models.Model):
    id = models.AutoField(primary_key=True)
    children = models.ForeignKey(Childrens, on_delete=models.CASCADE, null=True, related_name='childrens')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, to_field='id', null=True, related_name='driver')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, to_field='id', null=True, related_name='parent')

    class Meta:
        managed = False
        db_table = 'driver_children'


class Shifts(models.Model):
    id = models.IntegerField(primary_key=True)
    driver_id = models.IntegerField()
    shifttype_id = models.IntegerField()
    children_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifts'
