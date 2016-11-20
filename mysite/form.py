from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SignupForm, self).__init__(*args, **kwargs)
    nickName = forms.CharField(
        label="Nickname", max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '닉네임'
        }))
    username = forms.RegexField(label="Username", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters,    digits and " "@/./+/-/_ only.",
                                error_messages={
                                    'invalid': "This value may contain only letters,  numbers and "  "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '아이디'
                                }))

    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '비밀번호',
                                    'height': 3,
                                }))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '비밀번호 재확인'
                                }),
                                help_text="Enter the same password as above, forverification.")
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '이메일'
        })
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "nickName")




class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        # Set the label to omit ':'
        kwargs.setdefault('label_suffix', '')
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
    nickName = forms.CharField(
        label="Nickname", max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '닉네임',
            'required': 'True',

        }))
    username = forms.RegexField(label="Username", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters,    digits and " "@/./+/-/_ only.",
                                error_messages={
                                    'invalid': "This value may contain only letters,  numbers and "  "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '아이디',
                                    'required': 'True',
                                }))

    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '비밀번호',
                                    'height': 3,
                                    'required': 'True',
                                }))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '비밀번호 재확인'
                                    ,'required': 'True',
                                }),
                                help_text="Enter the same password as above, forverification.")
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '이메일',
            'required': 'True',
        })
    )
