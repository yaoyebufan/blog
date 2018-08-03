from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Article,Message,comment,Log
from django.contrib.auth import logout
from django.shortcuts import redirect
# 引入的返回聚合函数
from django.db.models import Max,Min,F,Q

# Create your views here.
# def article(request):
#     articlelist = Article.article.all()
#     return render(request,'myApp/index.html',{'articlelist':articlelist})#返回给html
# # 分页
# # def stupage(requst,page):
# #     # 0-5   5-10    10-15
# #     # 1     2       3
# #     page = int(page)
# #     studentlist = Article.article.all()[(page-1)*5:page*5]#显示三条匹配的数据
# #     return render(requst, 'myApp/index.html', {'students': studentlist})  # 返回给html，render起渲染作用

from django.core.paginator import Paginator
def articlepage(request):
    alllist = Article.article.all()
    somelist =  Article.article.all()[0:3]#显示前三条最新的数据
    messagelist = Message.message.all()[0:3]#显示前三条最新的留言
    paginator = Paginator(alllist,5)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request,"myApp/index.html",{'articlelist':page,"somelist":somelist,"messagelist":messagelist})

def content(request):
    articlelist = Article.article.all()
    # a = articlelist.filter(id__lte=5)
    return render(request,'myApp/content.html',{'articlelist':articlelist})#返回给html

def tocontent(request,id):
    articlelist = Article.article.filter(pk=id)
    return render(request, "myApp/content.html",{'articlelist':articlelist})

# def list1(request):
#     return render(request,"myApp/list.html")

def message(request):
    return render(request,"myApp/message.html")
from django.utils import timezone #引入timezone模块

def tomessage(request):
    time_now = timezone.now()  # 输出time_now即为当然日期和时间
    commenter1 = request.POST.get("commenter")
    emil1 = request.POST.get("emil")
    phone1 = request.POST.get("phone")
    contend1 = request.POST.get("content")
    create = Message.createmessage(commenter1,phone1,emil1,contend1,time_now,False)
    create.save()
    return render(request, "myApp/message.html")

def tocomment(request):
    time_now = timezone.now()  # 输出time_now即为当然日期和时间
    author = request.POST.get("author")
    emil1 = request.POST.get("email")
    contend1 = request.POST.get("comment")
    id = request.POST.get("id")
    create = comment.createcomment(author,emil1,contend1,time_now,id)
    create.save()
    return HttpResponse("发表成功")
def comment1(request,id):
    duixiang = Article.article.get(pk=id)
    comments = duixiang.comment_set.all()
    # grades = Grades.grade.get(pk=num)#获取班级id的对象
    # students = grades.student_set.all()#根据对象获取匹配的所有学生
    return render(request,'myApp/comments.html',{'comments':comments})#返回给html

def me(request):
    return render(request,'myApp/me.html')

#查看留言
def tomessage1(request,id):
    message = Message.message.filter(pk=id)
    return render(request, "myApp/tomessage.html",{'message':message})

#更多留言
def moremessage(request):
    alllist = Message.message.all()
    paginator = Paginator(alllist, 3)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request, "myApp/moremessage.html", {'articlelist': page})


# 更多文章
def morearticle(request):
    alllist = Article.article.all()
    paginator = Paginator(alllist, 5)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request, "myApp/morearticle.html", {'articlelist': page})

#跳转主页
def f(request):
    return render(request, "myApp/f.html")

#搜索
def so(request):
    title = request.POST.get("s")
    # 区分大小写双_contains可以匹配到包含名字里有“”的所有对象,想要不区分大小写加上i（icontains）即可，sname__isnull是否为空
    alllist = Article.article.filter(title__contains=title)
    paginator = Paginator(alllist, 5)
    page1 = request.GET.get('page', '1')  # 默认跳转到第一页
    page = paginator.page(page1)
    return render(request, "myApp/morearticle.html", {'articlelist': page})


# 时间轴
def time(request):
    alllist = Log.log.all()[0:6]  # 显示前6条最新的日志
    return render(request, "myApp/time.html", {'list': alllist})

