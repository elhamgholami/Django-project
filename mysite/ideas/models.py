from django.db import models

class Tweet(models.Model):
    category = (
        ('Science','Science'),
        ('Technology','Technology'),
        ('Engineering',' Engineering'),
        ('Mathematics','Mathematics')
    )
    content= models.TextField(max_length=500 , null=True , blank= True)
    category_choice = models.CharField(max_length=30,blank= True , null= True , choices = category)
    yourname = models.CharField(max_length=30, null = True , blank= True)
    yourage= models.CharField(max_length=3,null=True , blank=True)
    title=models.CharField(max_length=200,blank=True , null=True)
    
    def __str__(self) -> str:
        return self.content
    
