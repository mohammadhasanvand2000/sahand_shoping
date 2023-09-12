from colorfield.fields import ColorField
from django.db import models
from django.db.models import Count, F, Value


class Grouping(models.Model):
    title= models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return '{}'.format (self.title )


class Product (models.Model):
    grouping    = models.ForeignKey(Grouping,on_delete=models.CASCADE,related_name="grouping",verbose_name=("grouping"))
    title       = models.CharField(max_length=200,null=True,blank=True)
    price       = models.IntegerField(default='1000',null=True,blank=True)
    image       = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    slug        = models.SlugField(unique=True, max_length=255,null=True,blank=True) 
    


    def __str__(self):
        return '{},{},{},{},'.format (self.title ,self.price,self.image,self.slug )

class Detail(models.Model):
    #COLOR_CHOISES=[]

    product        = models.OneToOneField(Product,on_delete=models.CASCADE,related_name="productdetail",verbose_name=("product"))
    discribtion    = models.CharField(max_length=1000,null=True,blank=True)
    introduction   = models.CharField(max_length=2000,null=True,blank=True)
    Alloy          = models.CharField(max_length=200,null=True,blank=True)
    
    warranty       = models.IntegerField(null=True,blank=True)
    made_in        = models.CharField(max_length=50,null=True,blank=True)
    dimensions     = models.FloatField(null=True,blank=True)
    in_dimensions  = models.FloatField(null=True,blank=True)
    Weight         = models.IntegerField(null=True,blank=True)


   
        
    
   

    def __str__(self):
        return '{},{},{},{},{}'.format (self.discribtion ,self.introduction,self.warranty,self.made_in,self.dimensions )


class Product_image(models.Model):
    producti      = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="productimage",verbose_name=("producti"),null=True)
    image         = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)


    def __str__(self):
        return '{},'.format (self.image , )

class Product_color(models.Model):
    producti      = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="productcolor",verbose_name=("producti"),null=True)
    color         = ColorField(default='#FF0000',null=True,blank=True)
    title         = models.CharField(max_length=200,null=True,blank=True)

 

class Client_Coments(models.Model):
    product = models.OneToOneField(Product,on_delete=models.SET_NULL,related_name="cproduct",verbose_name=("cproduct"),null=True)
    coment  = models.CharField(max_length=10000,null=True,blank=True)
    img     = models.ImageField(help_text="plase enter images your product ",null=True,blank=True)


    def __str__(self):
        return '{},{}'.format (self.coment ,self.img,)



class Cart (models.Model):
    product      = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="productcart",verbose_name=("product"),null=True)
    buy_from_avalable  = models.IntegerField(null=True,blank=True)
    avalable       = models.IntegerField(null=True,blank=True)

    def is_avalable(self):
        a=self.avalable
        b=self.buy_from_avalable
        if b>0:
            c=b-a
            return c

        elif a<5:
            d=a
            return d
    

    def __str__(self):
        return '{},{}'.format (self.buy_from_avalable ,self.product)



    






    