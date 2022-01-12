
from django.db import models
from django.db.models.expressions import F
from years.models import levelschool, yearsschool
from PIL import Image
from django.urls import reverse
# Create your models here.



class ALLStudent(models.Model):
    levellist = (
            ('ปวช.3','ปวช.3'),
            
            ('ปวส.2','ปวส.2'))
    schoolyaerlist= (('พ.ศ.2564','พ.ศ.2564'),
                 ('พ.ศ.2565','พ.ศ.2565'),
                 ('พ.ศ.2566','พ.ศ.2566'),
                 ('พ.ศ.2567','พ.ศ.2567'),
                 ('พ.ศ.2568','พ.ศ.2568'))
               
   
    schoolyaer = models.CharField(max_length=100, choices=schoolyaerlist,default='พ.ศ.2564') 
    level = models.CharField(max_length=100, choices=levellist,default='ปวช.3') 
    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200)    
    student_tel = models.CharField(max_length=10,blank=True,null=True)
    parent_name = models.CharField(max_length=200,blank=True,null=True)
    parent_tel = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(max_length=200,blank=True,null=True)
    photo = models.ImageField(upload_to="studentphoto",blank=True,null=True)
    
    def __str__(self) :
        return '{}-{}'.format(self.student_id,self.student_name)
    
from django.contrib.auth.models import User
    
class Profile(models.Model):
    usertypelist = (('teacher','teacher'),
                    ('student','student'))
    levellist = (
            ('ปวช.3','ปวช.3'),
            
            ('ปวส.2','ปวส.2'))
    schoolyaerlist= (('พ.ศ.2564','พ.ศ.2564'),
                 ('พ.ศ.2565','พ.ศ.2565'),
                 ('พ.ศ.2566','พ.ศ.2566'),
                 ('พ.ศ.2567','พ.ศ.2567'),
                 ('พ.ศ.2568','พ.ศ.2568'))
    
    schoolyaer = models.CharField(max_length=100, choices=schoolyaerlist,default='พ.ศ.2564') 
    level = models.CharField(max_length=100, choices=levellist,default='ปวช.3') 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photoprofile = models.ImageField(default='defalt.jpg',upload_to='photo_profile',blank=True,null=True)
    usertype = models.CharField(max_length=100,choices=usertypelist,null=True,blank=True,default='student')
  
                
    def __str__(self) :
        return F'{self.user.username}Profile'




class levell(models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(unique=True,null=True)
   
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('pro_cate', args=[self.slug,])
     
    
class yearr(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(levell,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return  '{}-{}'.format(self.name,self.category)


class proshow(models.Model):
    

    
    file_name = models.CharField(max_length=255)
    categoryyear = models.ForeignKey(yearr, on_delete=models.CASCADE, default='' , null=True)
    categorylevel = models.ForeignKey(levell, on_delete=models.CASCADE, default='' , null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True , null=True)
    my_file= models.FileField(upload_to='documentproject')
    ognfirst = models.CharField(max_length=255,blank=True,null=True)
    ognsecond= models.CharField(max_length=255,blank=True,null=True)
    ognthird=models.CharField(max_length=255,blank=True,null=True )
    teacherpro=models.CharField(max_length=255,blank=True,null=True )
    consultpro=models.CharField(max_length=255,blank=True,null=True )
    photo = models.ImageField (upload_to='Photoproject',height_field=None, width_field=None,blank=True,null=True)
    views=models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    userupload = models.CharField(max_length=255,blank=True,null=True )
    Abstract= models.FileField(upload_to='Abstractproject',blank=True,null=True)
    
   
            
            
    def __str__(self) :
        return '{}-{}'.format(self.file_name,self.categoryyear)




            
   

class ALLteacher(models.Model):
    levellist = (
            ('ปวช.1','ปวช.1'),
            ('ปวช.2','ปวช.2'),
            ('ปวช.3','ปวช.3'),
            ('ปวส.1','ปวส.1'),
            ('ปวส.2','ปวส.2'))
    positionlist= (('หัวหน้าแผนก','หัวหน้าแผนก'),
                 ('ครูประจำแผนก','ครูประจำแผนก'),
               
                 )
               
   
    position = models.CharField(max_length=100, choices=positionlist) 
    level = models.CharField(max_length=100, choices=levellist) 
    class_Number = models.CharField(max_length=200,blank=True,null=True)
    teacher_name = models.CharField(max_length=200)
    teacher_tel = models.CharField(max_length=10,blank=True,null=True)
    photo = models.ImageField(upload_to="teacherphoto",blank=True,null=True)
    
    def __str__(self) :
        return '{}-{}'.format(self.level,self.teacher_name)
    
    
    
class Comment(models.Model):
    project = models.ForeignKey(proshow, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.project.file_name, self.commenter_name)