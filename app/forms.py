from django import forms
c=[('python','PYTHON'),('java','JAVA',),('django','DJANGO')]
g=[('male',"MALE"), ('female',"FEMALE")]
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #Course=forms.MultipleChoiceField(choices=c)
    Course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)