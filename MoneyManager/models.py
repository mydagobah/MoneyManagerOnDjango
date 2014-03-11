from django.db import models
from django import forms
import datetime

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
	return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name     = models.CharField(max_length=255)

    def __unicode__(self):
	return self.name

class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
	return self.name

class Creditcard(models.Model):
    name  = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner)

    def __unicode__(self):
	return self.name

class Income(models.Model):
    amount  = models.DecimalField(max_digits=15, decimal_places=2)
    owner   = models.ForeignKey(Owner)
    comment = models.CharField(max_length=2000, null=True, blank=True)

class Spense(models.Model):
    amount      = models.DecimalField(max_digits=15, decimal_places=2)
    issue_date  = models.DateField('date issued')
    added_date  = models.DateTimeField('date added')
    category    = models.ForeignKey(Category)
    owner       = models.ForeignKey(Owner)
    subCategory = models.ForeignKey(SubCategory, null=True, blank=True)
    creditcard  = models.ForeignKey(Creditcard, null=True, blank=True)
    comment     = models.CharField(max_length=2000, null=True, blank=True)

class SpenseForm(forms.ModelForm):
    class Meta:
	model = Spense
	fields  = ['amount', 'issue_date', 'category', 'owner', 'creditcard', 'comment']
	exclude = ['added_date', 'subCategory']
        labels = {
	     'amount':     'Total ($)',
	     'issue_date': 'Date purchased',
	     'creditcard': 'Card used (Optional)',
	     'comment':    'Comment (Optional)',
	}
        help_texts = {
	}
	error_messages = {
	}
	widgets = {
	    'comment': forms.Textarea(attrs={'cols':23,'rows':2})
	}
    # add validation for amount
    def clean_amount(self):
	data = self.cleaned_data['amount']
        if data <= 0:
	    raise forms.ValidationError('Spending must be positive')
        return data # always return data
