from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'main_categories'
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete = models.CASCADE)
    name     = models.CharField(max_length = 45)

    class Meta:
        db_table = 'sub_categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    main_category   = models.ForeignKey(MainCategory, on_delete = models.CASCADE)    
    sub_category    = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    name            = models.CharField(max_length = 45, null = True)
    english_name    = models.CharField(max_length = 300, null = True)
    big_image_url   = models.URLField(max_length = 500, null = True)
    small_image_url = models.URLField(max_length = 500, null = True)
    main_comment    = models.CharField(max_length = 550, null = True)
    sub_comment     = models.CharField(max_length = 500, null = True)
    nutrition       = models.OneToOneField('Nutrition', on_delete = models.CASCADE, null = True)
    allergy         = models.ManyToManyField('Allergy', through = 'ProductAllergy', null = True)
    size            = models.ManyToManyField('Size', through = 'ProductSize', null = True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    calories    = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)
    fat         = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)
    protein     = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)
    salt        = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)
    sugar       = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)
    caffein     = models.DecimalField(max_digits = 4, decimal_places = 1, null = True)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

    def __str__(self):
        return self.name

class ProductAllergy(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_allergies'

class Size(models.Model):
    name = models.CharField(max_length = 100, null = True)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    size    = models.ForeignKey(Size, on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_sizes'
