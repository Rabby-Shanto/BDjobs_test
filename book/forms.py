from django import forms
from .models import Book


class DateInput(forms.DateInput):
    input_type = 'date'


class bookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=DateInput)
    genre = forms.ChoiceField(choices=Book.book_type, widget=forms.RadioSelect)
    class Meta:

        model = Book
        fields = ['title','publisher_name','publisher_age','page_no','publication_date','genre']

    def __init__(self,*args, **kwargs):
        super(bookForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'