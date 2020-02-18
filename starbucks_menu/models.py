from django.db import models

class MainCategory(models.Model):
    main_category = models.CharField(max_length = 45)

    class Meta:
        db_table = 'maincategories' # main_categories

class SubCategory(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete = models.CASCADE)
    sub_category     = models.CharField(max_length = 45)

    class Meta:
        db_table = 'subcategories'

class Product(models.Model):
    main_category_id     = models.ForeignKey(MainCategory, on_delete = models.CASCADE)    
    sub_category_id      = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    big_image_url        = models.URLField(max_length = 500)
    product_name         = models.CharField(max_length = 45)
    product_name_english = models.CharField(max_length = 300)
    main_comment         = models.CharField(max_length = 550)
    calories             = models.DecimalField(max_digits = 4, decimal_places = 1)
    fat                  = models.DecimalField(max_digits = 4, decimal_places = 1)
    protein              = models.DecimalField(max_digits = 4, decimal_places = 1)
    salt                 = models.DecimalField(max_digits = 4, decimal_places = 1)
    sugar                = models.DecimalField(max_digits = 4, decimal_places = 1)
    caffein              = models.DecimalField(max_digits = 4, decimal_places = 1)
    allegen_information  = models.CharField(max_length = 100)
    small_image_url      = models.URLField(max_length = 500)
    sub_comment          = models.CharField(max_length = 500)

    class Meta:
        db_table = 'products'
