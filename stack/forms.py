from django import forms

# creating a form
class InputForm(forms.Form):

	question = forms.CharField(max_length = 200,
					help_text = "Enter the question you want to search"
					)
