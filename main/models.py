from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="categories/", verbose_name="Изображение", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Pet(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="pets"
    )
    breed = models.CharField(
        max_length=100, verbose_name="Порода", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="pets/", verbose_name="Изображение", blank=True, null=True
    )

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(
        max_length=100, verbose_name="Фамилия", blank=True, null=True
    )
    age = models.IntegerField(verbose_name="Возраст")
    profession = models.CharField(max_length=100, verbose_name="Профессия")
    image = models.ImageField(
        upload_to="staff/", verbose_name="Изображение", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    animal = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name="Питомец")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f'{self.name} - {self.animal}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
