from django import forms

class MovieReviewForm(forms.Form):
    rating = forms.IntegerField(label="Calificación", min_value=1, max_value=100, required=True)
    review = forms.CharField(label="Reseña", min_length=20 ,required=True, 
    widget=forms.Textarea(attrs={"class": "px-3 py-3.5 text-left text-sm font-semibold text-gray-900"})
    )
    
    rating.widget.attrs.update({"class": "py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900"})