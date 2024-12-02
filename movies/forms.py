from django import forms

class MoviewReviewForm(forms.Form):
    rating = forms.IntegerField(label="Calificación", min_value=1, max_value=100, required=True)
    review = forms.CharField(label="Reseña", min_length=20 ,required=True)