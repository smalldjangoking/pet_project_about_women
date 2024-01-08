from django import forms

from women.models import Category, Women


class Addpostform(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выбрать Категорию', label='Категория')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'img_file', 'is_published', 'cat', 'tag']

        widgets = {
            'title': forms.TextInput(attrs={'cols': 25, 'rows': 1}),
            'slug': forms.TextInput(attrs={'cols': 15, 'rows': 1}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

        labels = {
            'slug': 'URL',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 35 or len(title) < 10:
            raise forms.ValidationError('Допустимая длина заголовка [10 до 35 символов!]')
        return title
