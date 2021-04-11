from django.db import models


class User(models.Model):
    id = models.IntegerField('primary key', db_column='id', null=False, primary_key=True)
    civility = models.CharField('civility', db_column='civilite', max_length=10)
    firstName = models.CharField('first name', db_column='first_name', max_length=20)
    lastName = models.CharField('last name', db_column='last_name', max_length=20)
    sexe = models.CharField('sexe', db_column='sexe', max_length=10)
    birthday = models.DateField('birthday', db_column='birthday')
    mail = models.TextField('mail', db_column='mail', max_length=50)
    password = models.CharField('password', db_column='password', max_length=20)
    city = models.CharField('city', db_column='city', max_length=20)
    country = models.CharField('country', db_column='country', max_length=20)

    class Meta:
        db_table = "p_user"

    def __str__(self):
        return self.firstName + ' ' + self.lastName
