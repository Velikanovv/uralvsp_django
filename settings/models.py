from django.db import models
from pytils.translit import slugify
# Create your models here.


def sms_file_path(instance, filename):
    return 'social_media_settings/%s/img/%s' % (str(instance.pk), filename)

class SocialMediaSetting(models.Model):
    file = models.FileField(verbose_name='Файл',blank=False, null=False, help_text="Format: .svg | FlatIcon",upload_to=sms_file_path)
    url = models.URLField(verbose_name='Ссылка',blank=True, null=True, help_text="URL")

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

class MenuSetting(models.Model):
    number_url = models.CharField(verbose_name='1 Ссылка на номер',blank=True, null=True, help_text="1 Номер Телефона(Ссылка)", max_length=100)
    s_number_url = models.CharField(verbose_name='2 Ссылка на номер',blank=True, null=True, help_text="2 Номер Телефона(Ссылка)", max_length=100)
    number = models.CharField(verbose_name='1 Номер Телефона',blank=True, null=True, help_text="1 Номер Телефона", max_length=100)
    s_number = models.CharField(verbose_name='2 Номер Телефона',blank=True, null=True, help_text="2 Номер Телефона", max_length=100)

    address = models.CharField(verbose_name='Адрес',blank=True, null=True, help_text="Адрес", max_length=100)

    def __str__(self):
        return str('Настройка меню (Не надо создавать несколько)')

    class Meta:
        verbose_name = 'Настройка меню'
        verbose_name_plural = 'Настройка меню'

class FooterContacts(models.Model):
    name = models.CharField(verbose_name='Название',blank=True, null=True, help_text="Название", max_length=100)
    text = models.CharField(verbose_name='Текст',blank=True, null=True, help_text="Текст", max_length=500)

    def __str__(self):
        return self.name + ': ' + self.text

    class Meta:
        verbose_name = 'Футер - Контакт'
        verbose_name_plural = 'Футер - Контакты'

class SecondBlockAbouts(models.Model):
    name = models.CharField(verbose_name='Заголовок',blank=True, null=True, help_text="Заголвок", max_length=100)
    text = models.CharField(verbose_name='Текст',blank=True, null=True, help_text="Продолжение", max_length=100)

    def __str__(self):
        return self.name + ' ' + self.text

    class Meta:
        verbose_name = '2 Блок - Достижение'
        verbose_name_plural = '2 Блок - Достижения'

class BlocksSettings(models.Model):
    first_block_title = models.CharField(verbose_name='Заголовок 1-го блока',blank=True, null=True, help_text="Заголвок 1 блока", max_length=100)
    first_block_text= models.CharField(verbose_name='Текст 1 блока',blank=True, null=True, help_text="Текст 1 блока", max_length=100)
    second_block_text = models.TextField(verbose_name='Текст второго блока',blank=True, null=True, help_text="Текст 2 блока")

    def __str__(self):
        return 'Настройка блоков'

    class Meta:
        verbose_name = 'Настройка блоков'
        verbose_name_plural = 'Настройка блоков'

class PSSettings(models.Model):
    production_text= models.TextField(verbose_name='Производство',blank=True, null=True, help_text="Текст - Производство")
    service_text = models.TextField(verbose_name='Услуги',blank=True, null=True, help_text="Текст - Услуги")

    def __str__(self):
        return 'Производство и Сервис'

    class Meta:
        verbose_name = 'Производство и Сервис'
        verbose_name_plural = 'Производство и Сервис'



def menuurl_img_path(instance, filename):
    return 'menuurl/%s/img/%s' % (str(instance.pk), filename)

class MenuUrl(models.Model):
    title = models.CharField(verbose_name='Заголовок',blank=True, null=True, help_text="Название", max_length=100)
    url = models.CharField(verbose_name='Ссылка',blank=True, null=True, help_text="Ссылка", max_length=500)
    add_to_catalog = models.BooleanField(verbose_name='Добавлять в каталог',default=False)
    image = models.ImageField(verbose_name='Фото',null=True, blank=False, upload_to=menuurl_img_path)

    def __str__(self):
        return self.title + ': ' + self.url

    class Meta:
        verbose_name = 'Сторонние ссылки'
        verbose_name_plural = 'Сторонние ссылки'

class Politics(models.Model):
    text = models.TextField(verbose_name='Текст',help_text="Политика конфидециальности")

    def __str__(self):
        return 'Политика конфидециальности'

    class Meta:
        verbose_name = 'Политика конфидециальности'
        verbose_name_plural = 'Политика конфидециальности'

class Contacts(models.Model):
    text = models.TextField(verbose_name='Текст',help_text="Информация")

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class MessageSettings(models.Model):
    feedback_done_message = models.CharField(verbose_name='Обратная связь',blank=True, null=True, help_text="Сообщение | Обратная связь", max_length=100)
    application_done_message = models.CharField(verbose_name='Заявка',blank=True, null=True, help_text="Сообщение | Заявка", max_length=100)

    def __str__(self):
        return 'Настройка сообщений заявок'

    class Meta:
        verbose_name = 'Настройка сообщений заявок'
        verbose_name_plural = 'Настройка сообщений заявок'

class Page(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    slug = models.CharField(verbose_name='Ссылка', max_length=100, unique=True, blank=True)
    show_in_menu = models.BooleanField(verbose_name='Показывать в меню',default=False)
    text = models.TextField(verbose_name='Текст', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = self.name
        self.slug = slugify(self.slug)
        super(Page, self).save(*args, **kwargs)

