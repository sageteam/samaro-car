from django.db import models

class CourseField(models.Model):
    title = models.CharField(max_length = 32)
    course = models.ForeignKey('Course', related_name='field', on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length = 32)
    course = models.ForeignKey('CourseTendency', related_name='course', on_delete=models.CASCADE)


class CourseTendency(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField()
