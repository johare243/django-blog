from django import forms
from django.contrib.auth.models import User
from pages.models import Category, Post, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        #Provide association btw ModelForm and model
        fields = ('name',)

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the post")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the post.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Post
        #we can show what not to include
        exclude = ('category', )
        #the below is the same as above
        #fields = ('title', 'url', 'views', 'category')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        #if url is not empty and doesn't start with 'http://'
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
