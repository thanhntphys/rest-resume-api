from django.db import models

# Create your models here.

GENDER_CHOICES = [
    (0, 'male'),
    (1, 'female'),
    (2, 'other'),
]


class Employee(models.Model):
    name = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    year_of_birth = models.DateField()
    email = models.EmailField(max_length=50, blank=True, unique=True)
    professional_overview = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)


class WorkHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    from_month_year = models.DateTimeField()
    to_month_year = models.DateTimeField()
    index = models.SmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    skill = models.CharField()
    index = models.SmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)


class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shool_name = models.CharField(max_length=100)
    major = models.CharField(max_length=50)
    from_year = models.DateField()
    to_year = models.DateField()
    index = models.SmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)


class Certificates(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    from_year = models.DateField()
    to_year = models.DateField()
    index = models.SmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)


class Projects(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField()
    technologies = models.TextField()
    team_size = models.SmallIntegerField()
    from_month_year = models.DateTimeField()
    to_month_year = models.DateTimeField()
    index = models.SmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)

