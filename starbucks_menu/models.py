from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'main_categories'

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete = models.CASCADE)
    name     = models.CharField(max_length = 45)

    class Meta:
        db_table = 'sub_categories'

class Product(models.Model):
    main_category       = models.ForeignKey(MainCategory, on_delete = models.CASCADE)    
    sub_category        = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    big_image_url       = models.URLField(max_length = 500, null=True)
    name                = models.CharField(max_length = 45, null=True)
    english_name        = models.CharField(max_length = 300, null=True)
    main_comment        = models.CharField(max_length = 550, null=True)
    calories            = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    fat                 = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    protein             = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    salt                = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    sugar               = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    caffein             = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    small_image_url     = models.URLField(max_length = 500, null=True)
    sub_comment         = models.CharField(max_length = 500, null=True)
    product_allergy     = models.ManyToManyField('Allergy', through='ProductAllergy', null=True)
    product_allergy2    = models.ManyToManyField('Allergy2', null=True)

    class Meta:
        db_table = 'products'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

class Allergy2(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies2'

class ProductAllergy(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete = models.CASCADE)

    class Meta:
        db_table = 'product_allergies'
