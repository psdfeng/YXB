from django.db import models

# Create your models here.

class Drug(models.Model):
    '''
        药品类，属性：code HIS代码，name：通用名称，form：规格，company:厂家，img：图片,thumb:缩略图,instructions:说明书
    '''
    code=models.CharField(max_length=200)    #
    name=models.CharField(max_length=200)
    form=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    img=models.ImageField(upload_to='img')
    thumb=models.FilePathField(path='img/thumb')
    instructions=models.CharField(max_length=5000)

