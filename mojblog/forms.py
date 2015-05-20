from django import forms

from .models import Post, Comment, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # category=forms.ModelChoiceField(Category.objects.all())
        fields = ('title', 'category', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		# exclude = ('Post', )
		fields = ('text', )

class CategoryForm(forms.ModelForm):
	class Meta:
		fields = ('category', )
	