from allauth.account.forms import LoginForm as allauthLoginForm
from allauth.account.forms import SignupForm as allauthSignupForm

class LoginForm(allauthLoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Password",
            'data-msg':"Your password is invalid. Please try again.",
            'data-error-class':"u-has-error",
            'data-success-class':"u-has-success"
        })
        self.fields['login'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Email",
            'data-msg':"Please enter a valid email address.",
            'data-error-class':"u-has-error",
            'data-success-class':"u-has-success"
        })

class SignupForm(allauthSignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Email",
            'data-msg':"Please enter a valid email address.",
            'data-error-class':"u-has-error",
            'data-success-class':"u-has-success"
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Username",
            'data-msg':"Please enter a username."
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Password",
            'data-msg':"Your password is invalid. Please try again.",
            'data-error-class':"u-has-error",
            'data-success-class':"u-has-success"
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form__input',
            'aria-label':"Confirm Password",
            'data-msg':"Password does not match the confirm password.",
            'data-error-class':"u-has-error",
            'data-success-class':"u-has-success"
        })

