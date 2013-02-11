from django import forms
from django.utils import html

class SubmitButtonWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return '<input type="Scrape EPEX SPOT" name="%s" value="%s">' % (html.escape(name), html.escape(value))

class ScrapeButton(forms.Form):
    submit = forms.CharField(max_length=100)
    def __init__(self, scraper):
        forms.Form.__init__(self)
        #self.fields['spot_day'].scraper = [(c.id, c.hour, c.weighted_avg) for c in scraper.
            
class SubmitButtonField(forms.Field):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        kwargs["widget"] = SubmitButtonWidget

        super(SubmitButtonField, self).__init__(*args, **kwargs)
        
    def clean(self, value):
        return value
