from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACCOUNT_TYPE = (('1','Superadmin'),('2','teacher'),('3','Student'))

class UserAccount(models.Model):
	User=models.OneToOneField(User,on_delete=models.CASCADE)
	account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
	def __str__(self):
		return self.User.username



class forget_otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)
    expire  = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    secret_key = models.CharField(max_length=50,default="")
    attempt = models.IntegerField(default=0)    
    is_used = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
		