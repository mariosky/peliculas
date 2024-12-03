from django import forms

class MovieReviewForm(forms.Form):
    rating = forms.IntegerField(label="Calificación", min_value=1, max_value=100, required=True)
    title = forms.CharField(label="Titulo", required=True)
    review = forms.CharField(label="Reseña", min_length=20 ,required=True, 
                             widget =  forms.Textarea(attrs={"class": "block w-full rounded-md bg-white px-3" 
                                  "py-1.5 text-base text-gray-900 outline outline-1"
                                  "-outline-offset-1 outline-gray-300 placeholder:text-gray-400" 
                                  "focus:outline focus:outline-2 focus:-outline-offset-2" 
                                  "focus:outline-indigo-600 sm:text-sm/6"}) ) 
    
    
    title.widget.attrs.update({"class": "block w-full rounded-md bg-white px-3" 
                                  "py-1.5 text-base text-gray-900 outline outline-1"
                                  "-outline-offset-1 outline-gray-300 placeholder:text-gray-400" 
                                  "focus:outline focus:outline-2 focus:-outline-offset-2" 
                                  "focus:outline-indigo-600 sm:text-sm/6"})
    rating.widget.attrs.update({"class": "rounded-md bg-white py-1.5 pl-3 pr-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"})