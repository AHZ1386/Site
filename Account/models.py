from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


PROVINEC_CHOISES = (
    ("آذربایجان شرقی", "East Azarbaijan"),
    ("آذربایجان غربی", "West Azarbaijan"),
    ("اردبیل", "Ardabil"),
    ("اصفهان", "Isfahan"),
    ("البرز", "Alborz"),
    ("ایلام", "Ilam"),
    ("بوشهر", "Bushehr"),
    ("تهران", "Tehran"),
    ("چهارمحال و بختیاری", "Chaharmahal and Bakhtiari"),
    ("خراسان جنوبی", "South Khorasan"),
    ("خراسان رضوی", "Razavi Khorasan"),
    ("خراسان شمالی", "North Khorasan"),
    ("خوزستان", "Khuzestan"),
    ("زنجان", "Zanjan"),
    ("سمنان", "Semnan"),
    ("سیستان و بلوچستان", "Sistan and Baluchestan"),
    ("فارس", "Fars"),
    ("قزوین", "Qazvin"),
    ("قم", "Qom"),
    ("کردستان", "Kurdistan"),
    ("کرمان", "Kerman"),
    ("کرمانشاه", "Kermanshah"),
    ("کهگیلویه و بویراحمد", "Kohgiluyeh and Boyer-Ahmad"),
    ("گلستان", "Golestan"),
    ("گیلان", "Gilan"),
    ("لرستان", "Lorestan"),
    ("مازندران", "Mazandaran"),
    ("مرکزی", "Markazi"),
    ("هرمزگان", "Hormozgan"),
    ("همدان", "Hamadan"),
    ("یزد", "Yazd")
)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(unique=True,max_length=12)
    registered = models.BooleanField(default=False)
    shopping_cart = models.ManyToManyField('Store.Product', related_name='item', blank=True, null=True)
    main_address = models.ForeignKey('Account.UserAddress', on_delete=models.CASCADE,related_name='main_address',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.phone_number)


    objects = CustomUserManager()
    def check_address(self):
        if self.addresses.all():
            return True
        else:
            return False
    # چک کرد پر بودن شماره تلفن کاربر
    def check_phone_number(self):
        if self.phone_number:
            return True
        else:
            return False
    # چک کردن پر بودن لیست خرید کاربر
    def check_shopping_cart(self):
        if self.shopping_cart:
            return True
        else:
            return False

    def check_registered(self):
        if self.registered:
            return True
        else:
            False

class Otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.PositiveSmallIntegerField(null=True)
    expiration_date = models.DateTimeField(null=True)
    def __str__(self):
        return f'User: : "{self.user.phone_number}" Otp_code: {self.otp}'

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses',null=True)
    post_code = models.IntegerField(null=True)
    address = models.CharField(max_length=250,null=True)
    provinec = models.CharField(max_length=20,choices=PROVINEC_CHOISES,null=True)
    house_number = models.IntegerField(null=True)
    home_unit = models.PositiveIntegerField(null=True)