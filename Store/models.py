from django.db import models
from django_jalali.db import models as jalali_models

ORDER_STATUS_CHOICES = (
    # Awaiting confirmation
    ('aw','در انتظار تایید'),
    # Processing
    ('p','درحال پردازش'),
    # Ready to send
    ('r','اماده ارسال از انبار'),
    # Delivery
    ('d','تحویل پست داده شده'),
    ('do','تحویل مشتری داده شد'),)
class Category(models.Model):
    name = models.CharField(max_length=250, help_text='نام',default='متفرقه',null=True)
    slug = models.SlugField(max_length=250, unique=True, help_text='اسلاگ')
    image = models.ImageField(upload_to='Product/category', null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250,help_text='نام' ,null=True)
    slug = models.SlugField(max_length=250,unique=True,help_text='اسلاگ',allow_unicode=True)
    image = models.ImageField(upload_to='Product/Brand', null=True)
class Product(models.Model):
    title = models.CharField(max_length=100, null=True,help_text='نام')
    description = models.TextField(null=True,help_text='توضیحات')
    price = models.IntegerField(null=True,help_text='قیمت')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='cat',help_text='دسته بندی',blank=True)
    image_1 = models.ImageField(upload_to='Product', null=True,help_text='تصویر 1')
    image_2 = models.ImageField(upload_to='Product', null=True,help_text='تصویر 2')
    image_3 = models.ImageField(upload_to='Product', null=True,help_text='تصویر 3')
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, related_name='brand',help_text='برند',blank=True)
    slug = models.SlugField(max_length=50, null=True,help_text='اسلاگ',allow_unicode=True)
    quantity = models.IntegerField(help_text='تعداد در انبار', null=True)

    def __str__(self):
        return self.title
    

class Order(models.Model):
    user = models.ForeignKey('Account.User', on_delete=models.CASCADE,related_name='order')
    address = models.CharField(max_length=500,null=True)
    products = models.ManyToManyField(Product, related_name='products')
    status = models.CharField(max_length=2,choices=ORDER_STATUS_CHOICES)
    total_price = models.IntegerField(null=True,blank=True)
    created_at = jalali_models.models.DateTimeField(auto_now_add=True,null=True)





class Comment(models.Model):
    confirmed = models.BooleanField(default=False,)
    author = models.ForeignKey('Account.User',on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length=500)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comment')

