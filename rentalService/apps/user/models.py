from django.db import models
import datetime
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser,
	PermissionsMixin)


class RealUserManager(BaseUserManager):
	def create_user(self, userId, password=None):
		if not userId:
			raise ValueError('Users must have an email address')

		user = self.model(
			userId=userId,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, userId, password):
		u = self.create_user(userId=userId,
							 password=password,
							 )
		u.is_admin = True
		u.save(using=self._db)
		return u


class RealUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		verbose_name='email',
		max_length=255,
		#unique=True,
	)
	username = None
	id = models.AutoField(primary_key=True)
	userId = models.CharField(max_length=255,unique=True)
	name = models.CharField(max_length=30, blank=True)
	postCode = models.CharField(max_length=8)
	address = models.CharField(max_length=256)
	phone = models.CharField(max_length=11)
	grade = models.IntegerField(null=True)
	accountInfo = models.CharField(max_length=128, blank=True)
	userInfo = models.CharField(max_length=128, blank=True)

	createTime = models.DateTimeField(default=datetime.datetime.now())
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = RealUserManager()

	USERNAME_FIELD = 'userId'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		# The user is identified by their email address
		return self.userId

	def get_short_name(self):
		# The user is identified by their email address
		return self.userId

	def __str__(self):
		return self.userId

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin