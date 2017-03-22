django-bootstrap3-datetimepicker
================================

This package uses Bootstrap v3 datetimepicker widget version 2 provided by the following project:
 https://github.com/Eonasdan/bootstrap-datetimepicker

The correct formatting options for dates can be found here:
 http://momentjs.com/docs/

It works only with Bootstrap3. If you are using Bootstrap2 in your
Django project, check out this:
https://github.com/zokis/django-bootstrap-datetimepicker

Install
-------

-  Run ``pip install bootstrap3-datetime``
-  Add ``'bootstrap3_datetime'`` to your ``INSTALLED_APPS``

Example
-------

forms.py


::

    from bootstrap3_datetime.widgets import DateTimePicker
    from django import forms

    class ToDoForm(forms.Form):
        todo = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"}))
        date = forms.DateField(
            widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                           "pickTime": False}))
        reminder = forms.DateTimeField(
            required=False,
            widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                           "pickSeconds": False}))
