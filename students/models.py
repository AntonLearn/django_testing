from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

    def clean(self):
        enrolled_students_count = self.students.count()
        if enrolled_students_count >= settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError(f"Максимальное число студентов на курсе: {settings.MAX_STUDENTS_PER_COURSE}")
