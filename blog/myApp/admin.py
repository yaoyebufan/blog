from django.contrib import admin


# Register your models here.
from .models import Article,Message,comment,Log


@admin.register(Article)# admin.site.register(Grades,GradesAdemin)
class ArticleAdemin(admin.ModelAdmin):
   # 列表页属性
    list_display = ['pk','title','date','picture','isDelete','author','tag']
    list_filter = ['title'] #过滤器
    search_fields = ['title']#查询框
    list_per_page = 5#页码
   # 添加，修改页面属性
   # fields = ['gdate','ggirlnum','gboynum','gname']#页面的先后顺序和ieldsets不能同时存在
   #  fieldsets = [
   #     ("num",{"fields":['ggirlnum','gboynum']}),
   #     ("base",{"fields":['gname','gdate']}),
   # ]#分组

@admin.register(Message)# admin.site.register(Grades,GradesAdemin)
class MessageAdemin(admin.ModelAdmin):
   # 列表页属性
    list_display = ['pk','commenter','phone','emil','isDelete','date']
    list_filter = ['commenter'] #过滤器
    search_fields = ['commenter']#查询框
    list_per_page = 5#页码


@admin.register(comment)  # admin.site.register(Grades,GradesAdemin)
class commentAdemin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['pk', 'commenter', 'emil', 'uid', 'date']
    list_filter = ['commenter']  # 过滤器
    search_fields = ['commenter']  # 查询框
    list_per_page = 5  # 页码

@admin.register(Log)  # admin.site.register(Grades,GradesAdemin)
class LogAdemin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['pk', 'commenter','date']
    list_filter = ['commenter']  # 过滤器
    search_fields = ['commenter']  # 查询框
    list_per_page = 5  # 页码