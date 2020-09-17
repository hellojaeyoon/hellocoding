from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     REGION_A = 'seoul'
#     REGION_B = 'daejeon'
#     REGION_C = 'gumi'
#     REGION_D = 'gwangju'
#     REGIONS = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '구미'),
#         (REGION_D, '광주'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'