from django.db import models

# Create your models here.
# 文章
class Article(models.Model):
    # 自定义objects 让他变为article，也可以写个类进行筛选
    article = models.Manager()
    # 文章标题
    title = models.CharField(max_length=100,null=True)
    # 文章发表时间
    date = models.DateTimeField(null=True)
    # 文章内容
    content = models.TextField(null=True)
    # 附带图片
    picture = models.ImageField(null=True,upload_to='static/picture',blank=True)
    # 是否为假删除
    isDelete = models.BooleanField(default=False)
    # 文章作者
    author = models.CharField(max_length=20,null=True)
    # 最后一次修改的时间
    lastime = models.DateTimeField(auto_now=True,null=True)
    # 第一次创建的时间
    creatime = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        db_table = 'article'#设置表名，默认小写
        ordering = ['-id']
    def __str__(self):
        return "%s" % (self.title)

# 留言
import time
class Message(models.Model):
    @classmethod
    def createmessage(cls, commenter1, phone1, emil1, contend1, date1, isD=False):
        message = cls(commenter=commenter1, phone=phone1, emil=emil1, content=contend1, date=date1,isDelete=isD)
        return message
    # 电话号码
    phone = models.CharField(max_length=11,null=True)
    # 留言者
    commenter = models.CharField(max_length=20,null=True)
    # 留言邮箱
    emil = models.EmailField(null=True)
    # 是否为假删除
    isDelete = models.BooleanField(default=False)
    # 留言内容
    content = models.TextField(null=True)
    # 留言时间
    date = models.DateTimeField(null=True)
    class Meta:
        db_table = 'message'#设置表名，默认小写
        ordering = ['-id']

class comment(models.Model):
    @classmethod
    def createcomment(cls, commenter1, emil1, content1, date1, id1):
        message = cls(commenter=commenter1, emil=emil1, content=content1, date=date1, uid_id=id1)
        return message

    # 评论者
    commenter = models.CharField(max_length=20, null=True)
    # 邮箱
    emil = models.EmailField(null=True)
    # 内容
    content = models.TextField(null=True)
    # 时间
    date = models.DateTimeField(null=True)
    # 外键
    uid = models.ForeignKey(Article, on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        db_table = 'comment'  # 设置表名，默认小写
        ordering = ['-id']
