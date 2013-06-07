# -*- coding: utf-8 -*-
from django.db import models

class CV(models.Model):
	container = models.CharField(max_length=10)
	def __unicode__(self):
		return self.container


class Profile(models.Model):
	title = models.CharField(max_length = 20)
	summary = models.TextField()
	cv = models.ForeignKey(CV)
	def __unicode__(self):
		return self.title	


class Education(models.Model):
	degree = models.CharField(max_length=70)
	institution = models.CharField(max_length=70)
	city = models.CharField(max_length = 20)
	year = models.DateField('Year')
	cv = models.ForeignKey(CV)
	def __unicode__(self):
		return self.degree	

class Experience(models.Model):
	job_title=models.CharField(max_length=70)
	institution = models.CharField(max_length=70)
	start_date = models.DateField('start date')
	end_date = models.DateField('finish date')
	cv = models.ForeignKey(CV)


class Courses(models.Model):
	course_title = models.CharField(max_length=70)
	institution = models.CharField(max_length=70)
	city = models.CharField(max_length = 20)
	date = models.DateField('finish date')
	cv = models.ForeignKey(CV)