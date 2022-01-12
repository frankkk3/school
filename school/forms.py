from django import forms
from django.db.models import fields

from django import forms

from school.models import Comment, proshow









class MyfileUploadForm(forms.Form):
    levellist = [
    ("ปวช.3", "ปวช.3"),
    ("ปวส.2", "ปวส.2"),
    
]
    levelf = forms.ChoiceField (
        required=False,
        widget=forms.Select,
        choices=levellist,)
    ylist = [
    ("พ.ศ.2564", "พ.ศ.2564"),
    ("พ.ศ.2565", "พ.ศ.2565"),
    ("พ.ศ.2566", "พ.ศ.2566"),
    ("พ.ศ.2567", "พ.ศ.2567"),
    ("พ.ศ.2568", "พ.ศ.2568"),
    
]
    year = forms.ChoiceField (
        required=False,
        widget=forms.Select,
        choices= ylist,)
    file_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'})) 
    files = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    organizefirst = forms.CharField(widget= forms.TextInput  (attrs={'class':'form-control' })) 
    organizesecond = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'})) 
    organizethird = forms.CharField(widget= forms.TextInput (attrs={'class':'form-control'})) 
    photo = forms.ImageField(widget=forms.FileInput  (attrs={'class':'form-control'}))
    


class ProjectForm(forms.ModelForm):
    class Meta:
        model = proshow
        fields = ['file_name', 'my_file', 'category', 'categoryyear', 'ognfirst','ognsecond','ognthird','photo','teacherpro','consultpro','Abstract']
        widgets = {
            'file_name': forms.TextInput(attrs={'class': 'form-control'}),
            'my_file': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'categoryyear': forms.Select(attrs={'class': 'form-control'}),
            'ognfirst': forms.TextInput(attrs={'class': 'form-control'}),
            'ognsecond': forms.TextInput(attrs={'class': 'form-control'}),
            'ognthird': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput (attrs={'class': 'form-control'}),
            'teacherpro': forms.TextInput(attrs={'class': 'form-control'}),
            'consultpro': forms.TextInput(attrs={'class': 'form-control'}),
            'Abstract': forms.FileInput(attrs={'class': 'form-control'}),

           
        }
        labels = {
            'file_name' : 'กรอกชื่อไฟล์',
            'my_file' : 'อัปโหลดไฟล์   **รวมไฟล์ทั้งหมดเป็น zip/rar เพื่อupload**',
            'category' : 'แผนก',
            'categoryyear' : 'ปีการศึกษา-ระดับชั้น',
            
            'ognfirst' : 'ผู้จัดทำลำดับที่ 1',
            'ognsecond' : 'ผู้จัดทำลำดับที่ 2',
            'ognthird' : 'ผู้จัดทำลำดับที่ 3    **หากไม่มีใส่เครื่องหมาย - **',
            'photo' : 'รูปภาพรวมผู้จัดทำ  **upload เป็นไฟล์ Jpg/Png**',
            'teacherpro' : 'ครูผู้สอน',
            'consultpro' : 'ครูที่ปรึกษา',
            'Abstract' : 'บทคัดย่อ   **upload เป็นไฟล์ pdf**'
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'comment_body' : 'แสดงความคิดเห็น'}