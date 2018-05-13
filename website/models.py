from django.db import models


# Create your models here.
class About(models.Model):
    first_name = models.CharField('Name', max_length=250)
    last_name = models.CharField('Name', max_length=250, default='')
    mobile = models.CharField('Mobile', max_length=20)
    email = models.EmailField('Email', max_length=250)
    address = models.CharField('Address', max_length=250)
    designation = models.CharField('Designation', max_length=250)
    description = models.TextField('Description')

    def __str__(self):
        return self.first_name


class Social(models.Model):
    facebook = models.CharField('Facebook', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    linkedin = models.CharField('LinkedIn', max_length=100)
    google_plus = models.CharField('GooglePlus', max_length=100)
    github = models.CharField('Github', max_length=100)
    youtube = models.CharField('Youtube', max_length=100)

    def __str__(self):
        return "Social Media"


class Experience(models.Model):
    designation = models.CharField('Designation', max_length=250)
    company = models.CharField('Company', max_length=250)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    description = models.TextField('Description')

    def __str__(self):
        return self.company + ' ' + self.designation


class Education(models.Model):
    school = models.CharField('School', max_length=250)
    degree = models.CharField('Degree', max_length=250)
    obtain_gpa = models.FloatField("Obtain GPA")
    total_gpa = models.FloatField("Total GPA")
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')

    def __str__(self):
        return self.school


class SkillCategory(models.Model):
    title = models.CharField('Title', max_length=250)
    order = models.IntegerField('Order', default=0)

    def __str__(self):
        return self.title


class Skill(models.Model):
    COLOR = {
        ('bg-primary', 'Primary'),
        ('bg-success', 'Success'),
        ('bg-info', 'Info'),
        ('bg-warning', 'Warning'),
        ('bg-danger', 'Danger'),
    }
    title = models.CharField('Title', max_length=250)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    level = models.IntegerField('Level')
    color = models.CharField('Color', max_length=50, choices=COLOR, default='bg-success')
    order = models.IntegerField('Order', default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
