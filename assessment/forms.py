from django import forms 
from competence.models import Assessment
from django.contrib.admin.widgets import AdminSplitDateTime


 
class AssessmentForm(forms.ModelForm):
    # start_date=forms.DateTimeField(widget=AdminSplitDateTime())
    # end_date=forms.DateTimeField(widget=AdminSplitDateTime())
    # start_date=forms.DateTimeField(widget=forms.SelectDateWidget())
    # end_date=forms.DateTimeField(widget=forms.SelectDateWidget())
     
    class Meta:
        model=Assessment
        fields=('assessed','bundle','start_date', 'end_date','published')
        widgets={
            # 'assessed':forms.
            'start_date':forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),
            'end_date':forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),
        }