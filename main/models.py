from django.db import models


from django.contrib.auth.models import User

# Create your models here.
class AboutHeader(models.Model):

    name_1 = models.CharField('name 1',max_length=50)
    name_2 = models.CharField('name 2',max_length=50)
    name_3 = models.CharField('name 3',max_length=50)
    name_4 = models.CharField('name 4',max_length=50)


    def __str__(self) -> str:
        return self.name_1


class AboutSection(models.Model):

    about_image = models.ImageField('about image',upload_to='images')
    text_1 = models.CharField('text 1',max_length=40)
    text_2 = models.CharField('text 2',max_length=40)
    text_3 = models.TextField('text 3')

    def __str__(self) -> str:
        return self.text_1
    

class OurTeam(models.Model):

    member_image = models.ImageField('member image',upload_to='images')
    line_1 = models.CharField('line 1',max_length=40)
    line_2 = models.CharField('line 2',max_length=40)
    line_3 = models.TextField('line_3')

    def __str__(self) -> str:
        return self.line_1
    


class AboutIconca(models.Model):

    btn_name = models.CharField('button name',max_length=30)
    icon_text_1 = models.CharField('icon text 1',max_length=50)
    icon_text_2 = models.TextField('icon text 2')

    def __str__(self) -> str:
        return self.icon_text_1
    
class AboutPartners(models.Model):

    partner_image = models.ImageField('partner image',upload_to='images')
   


class Products(models.Model):

    prod_name = models.CharField('product name',max_length=30)
    prod_teg = models.CharField('product teg',max_length=30)

    def __str__(self) -> str:
        return self.prod_name
    

class JarangProd(models.Model):

    jarang_name = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField('price')
    line_1 = models.CharField('line 1',max_length=50)
    line_3 = models.TextField('line 3',max_length=50)
    image = models.ImageField('image')
    review = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.line_1
    

class Like(models.Model):

    name = models.ForeignKey(User,on_delete=models.CASCADE)
    grade = models.IntegerField()    

    def __str__(self) -> str:
        return self.name.__str__()
    
    
class ContactHeader(models.Model):

    contact_image = models.ImageField('images',upload_to='images')
    contact_1 = models.CharField('contact 1',max_length=100)
    contact_2 = models.CharField('contact 2',max_length=100)

    def __str__(self) -> str:
        return self.contact_1


class Contact(models.Model):

    name = models.CharField('name',max_length=50)
    email = models.EmailField('email')
    subject = models.CharField('subject',max_length=40)
    message = models.TextField('message')

    def __str__(self) -> str:
        return self.name
    
class ContactInfo(models.Model):

    maps = models.URLField('map image')
    info_1 = models.CharField('info 1',max_length=30)
    info_2  =models.TextField('info 2')

    def __str__(self) -> str:
        return self.info_1
    
    class Meta:

        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfos'

class ContactAside(models.Model):

    contact_1 = models.CharField('contact 1',max_length=50)
    contact_2 = models.TextField('contact 2')
    contact_3 = models.TextField('contact 3')

    def __str__(self) -> str:
        return self.contact_1


class ContactTitles(models.Model):

    title_1 = models.CharField('title 1',max_length=60)
    title_2 = models.CharField('title 2',max_length=60)
    title_3 = models.CharField('title 3',max_length=60)
    btn_name = models.CharField('btn name',max_length=60)

    

    def __str__(self) -> str:
        return self.title_1


class ProductTitle(models.Model):

    prod_title_1 = models.CharField('title 1',max_length=100)
    prod_title_2 = models.CharField('title 2',max_length=100)


    def __str__(self) -> str:
        return self.prod_title_1
    
class IndexHeader(models.Model):

    index_image = models.ImageField('index image',upload_to='images')
    index_info_1  =models.CharField('index info 1',max_length=50)
    index_info_2  =models.CharField('index info 2',max_length=50)

    def __str__(self) -> str:
        return self.index_info_1



class HomeNews(models.Model):

    home_title = models.CharField('home title',max_length=100)
    home_1 = models.CharField('home 1',max_length=100)
    home_2 = models.CharField('home 2',max_length=100)
    home_3 = models.CharField('home 3',max_length=100)
    home_4 = models.CharField('home 4',max_length=100)
    home_5 = models.CharField('home 5',max_length=100)
    home_6 = models.CharField('home 6',max_length=100)
    home_7 = models.CharField('home 7',max_length=100)
    home_8 = models.CharField('home 8',max_length=100)
    home_image = models.ImageField('home image',max_length=100)
    home_footer_1 = models.CharField('home footer',max_length=100)
    home_footer_2 = models.CharField('home footer_2',max_length=100)
    home_footer_3 = models.CharField('home footer_3',max_length=100)

    def __str__(self) -> str:
        return self.home_title

