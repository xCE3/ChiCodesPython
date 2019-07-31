from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def validateUser(self, post_data):

		is_valid = True
		errors = []

		if len(post_data.get('name')) and len(post_data.get('alias')) < 3:
			is_valid = False
			errors.append('name fields must be more than 3 characters')
		#if email is valid
		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
			is_valid = False
			errors.append('must enter a valid email')
		#if birthdate is not null
		if len(post_data.get('birthdate')) == 0:
			is_valid = False
			errors.append('enter your birthday')
		#if password >= 8 characters, matches password confirmation
		if len(post_data.get('password')) < 8:
			is_valid = False
			errors.append('password must be at least 8 characters')
		if post_data.get('password_confirmation') != post_data.get('password'):
			is_valid = False
			errors.append('password and password confirmation must match')

		return (is_valid, errors)


class User(models.Model):
	name = models.CharField(max_length = 45)
	alias = models.CharField(max_length = 45)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	birthdate = models.DateField()
	likes = models.ManyToManyField("Quote", related_name="likes", default=None)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return "name:{}, alias:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.alias, self.email, self.password, self.created_at, self.updated_at)

class QuoteManager(models.Manager):
	def validateQuote(self, post_data):

		is_valid = True
		errors = []

		if len(post_data.get('content')) < 12:
			is_valid = False
			errors.append('Message must be more than 10 characters')
		return (is_valid, errors)

class Quote(models.Model):
	content = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'authored_quotes')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = QuoteManager()

	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)





