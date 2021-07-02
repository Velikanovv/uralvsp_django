from django.db import models
from django.utils import timezone
# Create your models here.

def service_img_path(instance, filename):
    return 'service/%s/img/%s' % (str(instance.pk), filename)

def production_img_path(instance, filename):
    return 'production/%s/img/%s' % (str(instance.pk), filename)

def product_img_path(instance, filename):
    return 'product/%s/img/%s' % (str(instance.pk), filename)

def category_img_path(instance, filename):
    return 'category/%s/img/%s' % (str(instance.pk), filename)

def subcategory_img_path(instance, filename):
    return 'subcategory/%s/img/%s' % (str(instance.pk), filename)

class Production(models.Model):
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=production_img_path, default='default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'

class Service(models.Model):
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=service_img_path, default='default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Category(models.Model):
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=category_img_path, default='default.jpg')
    text = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class SubCategory(models.Model):
    category = models.ForeignKey(Category,verbose_name='Категория', on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)
    text = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=subcategory_img_path, default='default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,verbose_name='ПодКатегория', on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)
    image = models.ImageField(verbose_name='Фото',null=False, blank=False, upload_to=product_img_path, default='default.jpg')
    text = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class SubProduct(models.Model):
    product = models.ForeignKey(Product,verbose_name='Продукт', on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(verbose_name='Название',max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            super(SubProduct, self).save(*args, **kwargs)
            params = ProductParam.objects.filter(product=self.product).all()
            for param in params:
                value = ProductValue.objects.create(product=self.product, productparam=param, subproduct=self, title="")
                value.save()
        else:
            super(SubProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель продукта'
        verbose_name_plural = 'Модели продукта'

class ProductParam(models.Model):
    product = models.ForeignKey(Product,verbose_name='Продукт',  on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(verbose_name='Нзвание', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            super(ProductParam, self).save(*args, **kwargs)
            subproducts = SubProduct.objects.filter(product=self.product).all()
            for sub in subproducts:
                value = ProductValue.objects.create(product=self.product, productparam=self, subproduct=sub, title="")
                value.save()
        else:
            super(ProductParam, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

class ProductValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    subproduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE, null=False, blank=False)
    productparam = models.ForeignKey(ProductParam, on_delete=models.CASCADE, null=False, blank=False, related_name="product_value")
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


