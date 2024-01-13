from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai


# Create your views here.
def ask_gemini(mealType, foodType, ingredientItems):
        ModifiedInput=f"You are an Intelligent Recipe recommender. I want you to recommend a delicious recipe for {mealType}. Remember that I prefer {foodType} food. Here are the ingredients: {ingredientItems}. Please provide the suitable recipe. Note: Word Limit is 150 words" 
        API_KEY = 'AIzaSyBLAuKEfR5QsUMpn8SANRUMcc8gNQZQstU'
        gemini_api_key = API_KEY
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(ModifiedInput)
        outputMsg=response.text
        return outputMsg

@csrf_exempt
def recipe_app(request):
        if request.method == 'POST':
                meal = request.POST.get('mealtype')
                food = request.POST.get('foodtype')
                items = request.POST.get('ingredients')
                outputResponse = ask_gemini(meal, food, items)
                return JsonResponse({'postMessage': {'meal': meal, 'food': food, 'items': items}, 'response': outputResponse})

        return render(request, 'index.html')
