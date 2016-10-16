from django import forms


class verbSaveForm(forms.Form):
    #변수는 폼에서 id로 지정이 된다.
    verblist = forms.CharField(
        widget=forms.CharField()
    )