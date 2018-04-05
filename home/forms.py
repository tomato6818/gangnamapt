from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label=''
                                 ,widget=forms.TextInput(attrs={'placeholder': '검색어 입력', 'id': 'keyword'}))
