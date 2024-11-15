from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        import google.generativeai as genai

        API_KEY= "AIzaSyD2C7OANbPonIaqiDPTFVsS8MWQbpQbPqE"
        genai.configure(api_key=API_KEY)

        prompt = """traduis "je suis en DEV IA" en anglais"""


        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        #hearders = {
        #   "Content-Type": "application/json",
        #   "Authorization": f"Bearer {api_key}"
        #}
        #parameters= {
        #    "model": model,
        #    "prompt": prompt,
        #   "max_tokens": 100
        #}
        #response = requests.post(f"https://api.openai.com/v1/completions", headers=hearders, json=parameters).json()
        print(response.text)



        return Response(data={"result": response.text}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)


class AllTranslation(APIView):
    def get(self, request):
        data= Translation.objects.all()
        serliaze_data = TranslationSerializer(data,many=True)

        return Response(data=serliaze_data.data, status=None)


class FrenchITTranslationViewSet(APIView):
    def get(self, request):
        data= { 'request' : 'voici la trad '}

        return Response(data=data, status=None)

 


def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})