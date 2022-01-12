from django.conf.urls import url
from django.core import paginator
from school.models import *
from years.models import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from datetime import datetime
from school.forms import CommentForm, MyfileUploadForm, ProjectForm
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage,InvalidPage


def home(request):
    
    return render(request, 'home.html')
# Create your views here.
def a(request):
    
    return render(request, 'school/a.html')

def about(request):
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]
    return render(request, 'school/about.html',{'pop':popu ,'guide':guide})


def contact(request):
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]
    return render(request, 'school/contact.html',{'pop':popu ,'guide':guide})



def register(request):
    
    if request.method == 'POST':
        
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email

        newuser.set_password(password)
        newuser.save()
        # from django.shortcuts import redirect
        return redirect('login')

    return render(request, 'school/register.html')


@login_required
def searchstudent(request):
    ###models.objects.all()ดึงข้อมุลทั้งหมดมาจากฐานข้อมูล###
    ###models.objects.get(ตัวแปร:ข้อค้นหา)ดึงข้อมุลมาจากฐานข้อมูลแค่ตัวเดียว###
    ###models.objects.fillter(ตัวแปร:ข้อค้นหา)ดึงข้อมุลมาจากฐานข้อมูลหลายค่า###
    #search = ALLStudent.objects.get(student_id=)#
    if request.method == 'POST':
        data = request.POST.copy()
        searchid = data.get('search')
        print(searchid, type(searchid))
        try:
            result = ALLStudent.objects.get(student_id=searchid)
            print('RESULT:', result)
            context = {'result': result, 'check': 'found'}
        except:
            context = {'result': 'ไม่มีข้อมูลในระบบ', 'check': 'notfound'}
        return render(request, 'school/search.html', context)
    return render(request, 'school/search.html')





@login_required
def EditProfile(request):

    username = request.user.username
    current = User.objects.get(username=username)

    if request.method == 'POST' and request.FILES['photo_profile']:
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        #password = data.get('password')

        myprofile = User.objects.get(username=username)
        ###file system####
        try:
            setprofile = Profile.objects.get(user=myprofile)
        except:
            setprofile = Profile()
            setprofile.user = myprofile
        file_image = request.FILES['photo_profile']
        file_image_name = request.FILES['photo_profile'].name
        fs = FileSystemStorage()
        filename = fs.save(file_image_name, file_image)
        upload_file_url = fs.url(filename)
        setprofile.photoprofile = upload_file_url[6:]
        setprofile.save()
        #######
        myprofile.username = email
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.email = email
        # myprofile.set_password(password)
        myprofile.save()
        # from django.shortcuts import redirect
        return redirect('editprofile')

    context = {'data': current}
    return render(request, 'school/editprofile.html', context)



   
@login_required  
def upload (request):
   
    if request.method == 'POST':
        c_form = MyfileUploadForm(request.POST,request.FILES)
        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']    
            files = c_form.cleaned_data['files']
            ogfirst= c_form.cleaned_data['organizefirst']
            ogsecond= c_form.cleaned_data['organizesecond']
            ogthird= c_form.cleaned_data['organizethird']
            photoup=c_form.cleaned_data['photo']
            levelv =c_form.cleaned_data['levelf']
            yearv=c_form.cleaned_data['year']

            proshow(file_name=name,my_file=files,ognfirst=ogfirst,ognsecond=ogsecond,ognthird=ogthird ,photo=photoup
                        ,level=levelv,years=yearv).save()
            return HttpResponse("File Upload")
        else:
            return HttpResponse("error")
    else:

    
        context = {
            'form' : MyfileUploadForm()

         }
        return render(request,'school/upload.html',context)






 



        
        
       
def index (request):
    
    catenum = yearr.objects.all()
    category = request.GET.get('category')
    if category == None:
        upfile=proshow.objects.all().order_by('-pk').filter(is_published=True)
    else :
        upfile=proshow.objects.filter(category__name=category)
    
    
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]
    page_num = request.GET.get("page")
    paginator=Paginator(upfile,4)
    
    
    try:
        upfile = paginator.page(page_num)
    except PageNotAnInteger:
        upfile = paginator.page(1)
    except EmptyPage:
        upfile = paginator.page(paginator.num_pages)
        
    
    
    categories = levell.objects.all()
    context={'up' : upfile,'pop':popu,'guide':guide ,'category':categories,'c':catenum}
    
    return render (request,'school/index.html',context )



      
def userup (request):
    upfile=proshow.objects.all().order_by('-pk').filter(is_published=True)
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]

    context={'up' : upfile,'pop':popu,'guide':guide ,}
    
    return render (request,'school/userpro.html',context )



    





def coma (request):
    category = levell.objects.all()
   
    categoryID = request.GET.get('cate')
    if categoryID:
        project = proshow.objects.filter(categoryyear = categoryID)
    else:
        project = proshow.objects.all()
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]    
   
    context={
        'cate':category,
        'pro' : project,
        'pop':popu,
        'guide':guide
    }
   
    
    return render (request,'school/coma.html',context)


def comb (request,category_slug=None):
    category = None
    categories=Category.objects.all()
    show=proshow.objects.filter(categoryyear=1)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug )
        show=show.filter(category=category)
    context={'categories':categories,
                            'cc':show,
                            'category':category}    
        
    return render (request,'school/comb.html',context)



def blogdetail(request,id):
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]
    singlepro=proshow.objects.get(id=id)
    num_comments = Comment.objects.all().count()   
    singlepro.views = singlepro.views+1
    singlepro.save()
    
    return render(request,"school/prodetail.html",{"pro":singlepro,'pop':popu,'guide':guide,'num_comments':num_comments})



def allteacher(request):
    teacher=ALLteacher.objects.all()
    popu=proshow.objects.all().order_by('-views')[:3]
    guide=proshow.objects.all().order_by('views')[:3]
    return render(request,"school/allteacher.html",{"teacher":teacher,'pop':popu,'guide':guide})



@login_required(login_url='Index')
def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        U_form = ProjectForm(request.POST, request.FILES)
     
        if U_form.is_valid():
            userup=request.user.first_name
            
            name = U_form.cleaned_data['file_name']
            cate = U_form.cleaned_data['category']
            cateyear = U_form.cleaned_data['categoryyear']    
            files = U_form.cleaned_data['my_file']
            ogfirst= U_form.cleaned_data['ognfirst']
            ogsecond= U_form.cleaned_data['ognsecond']
            ogthird= U_form.cleaned_data['ognthird']
            photoup=U_form.cleaned_data['photo']
            teacher =U_form.cleaned_data['teacherpro']
            consult=U_form.cleaned_data['consultpro']
            Abstractt=U_form.cleaned_data['Abstract']
            v = proshow(userupload=userup,file_name=name,category=cate,categoryyear=cateyear,my_file=files,ognfirst=ogfirst,ognsecond=ogsecond
           ,ognthird=ogthird,photo=photoup,teacherpro=teacher,consultpro=consult,Abstract=Abstractt)
            v.save()
            
        
            return redirect('Index')
    else:
        form = ProjectForm()

    context = {
        "form":form
    }

    return render(request, "school/addProject.html", context)


@login_required(login_url='Index')
def updateProject(request,id):
    project = proshow.objects.get(id=id)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('Index')

    context = {
        "form":form
    }

    return render(request, "school/updateProduct.html", context)


@login_required(login_url='Index')
def deleteProject(request, id):
    project = proshow.objects.get(id=id)
    project.delete()
    return redirect('Index')



@login_required
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            project = proshow.objects.filter(file_name__icontains=query) 
            return render(request, 'school/searchbar.html', {'project':project})
        else:
            print("No information to show")
            return render(request, 'school/searchbar.html', {})






def add_comment(request, id):
    pro = proshow.objects.get(id=id)

    form = CommentForm(instance=pro)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=pro)
        if form.is_valid():
            name = request.user.first_name
            body = form.cleaned_data['comment_body']
            c = Comment(project=pro, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('Index')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    

    
    form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'school/add_comment.html', context)


def delete_comment(request, id):
    comment = Comment.objects.filter(project=id).last()
    project_id = comment.project.id
    comment.delete()
    return redirect(reverse('blogdetail', args=[project_id]))