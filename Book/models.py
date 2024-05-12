from django.db import models


#------Jarimalar YHQ START-------------#

class JarimaBook(models.Model):
    url_uz = models.FileField(upload_to='Books')
    url_ru = models.FileField(upload_to='Books')
    # url_krl = models.FileField(upload_to='Books')
#------ Jarimalar YHQ END --------------#

# -------- YHQ Qoidalar START-----------------#
class YHQQoidlarCategoryUz(models.Model):
    categoryUz = models.CharField(max_length=150)
    def __str__(self):
        return self.categoryUz
class YHQQoidlarCategoryRu(models.Model):
    categoryRu = models.CharField(max_length=150)
    def __str__(self):
        return self.categoryRu
class YHQQoidalarBook(models.Model):
    titleUz = models.CharField(max_length=150)
    titleRu = models.CharField(max_length=150)
    url_ru = models.FileField(upload_to='Books/qoidalar')
    categoryRu = models.ForeignKey(YHQQoidlarCategoryRu, on_delete=models.CASCADE)
    url_uz = models.FileField(upload_to='Books/qoidalar')
    categoryUz = models.ForeignKey(YHQQoidlarCategoryUz, on_delete=models.CASCADE)
    def __str__(self):
        return self.titleUz

# -------- YHQ Qoidalar END -----------------#