from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		label="", 
		widget=forms.TextInput(attrs={
			'class':'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40', 
			'placeholder':'Email Address'
		})
	)
	first_name = forms.CharField(
		label="", 
		max_length=100, 
		widget=forms.TextInput(attrs={
			'class':'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40', 
			'placeholder':'First Name'
		})
	)
	last_name = forms.CharField(
		label="", 
		max_length=100, 
		widget=forms.TextInput(attrs={
			'class':'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40', 
			'placeholder':'Last Name'
		})
	)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({
			'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40',
			'placeholder': 'Username'
		})
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="text-xs text-gray-500">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

		self.fields['password1'].widget.attrs.update({
			'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40',
			'placeholder': 'Password'
		})
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = (
			'<ul class="text-xs text-gray-500">'
			'<li>Your password can\'t be too similar to your other personal information.</li>'
			'<li>Your password must contain at least 8 characters.</li>'
			'<li>Your password can\'t be a commonly used password.</li>'
			'<li>Your password can\'t be entirely numeric.</li>'
			'</ul>'
		)

		self.fields['password2'].widget.attrs.update({
			'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 focus:outline-none focus:ring focus:ring-opacity-40',
			'placeholder': 'Confirm Password'
		})
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="text-xs text-gray-500">Enter the same password as before, for verification.</span>'