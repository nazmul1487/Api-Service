from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20)


job_type =(
    ("Backend","Backend"),
    ("Mobile","Mobile"),
)


class UserInfo(forms.Form):

    name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
                'class': 'form-control'}), required=True)

    email = forms.CharField(max_length=256, widget=forms.EmailInput(attrs={
        'class': 'form-control'}), required=True)

    phone = forms.CharField(max_length=14, widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=True)

    full_address = forms.CharField(max_length=512, widget=forms.Textarea(attrs={
        'class': 'form-control'}), required=True)

    name_of_university = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=True)

    graduation_year = forms.CharField(label='Graduation Year', widget=forms.TextInput(attrs={'min':'2015','max': '2020','type': 'number'}))

    cgpa = forms.DecimalField(label='Cgpa', max_value=4, min_value=2, decimal_places=2 )

    experience_in_months = forms.CharField( widget=forms.NumberInput(attrs={
        'class': 'form-control', 'min':0 ,'max': 100,}), required=True)

    current_work_place_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=True)

    applying_in = forms.ChoiceField(choices=job_type, required=True)

    expected_salary = forms.CharField(label='Cgpa', widget=forms.TextInput(attrs={'min':'15000','max': '60000','type': 'number'}))

    field_buzz_reference = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=True)

    github_project_url = forms.CharField(max_length=512, widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=True)

    file = forms.FileField(widget=forms.FileInput(attrs={'accept': 'application/pdf', }))