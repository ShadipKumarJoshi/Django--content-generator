from openai import OpenAI
from django.shortcuts import render
from django.conf import settings

# openai.api_key = settings.OPENAI_API_KEY

def generate_content(request):
    if request.method == 'POST':
        content_type = request.POST.get('content_type')
        prompt = request.POST.get('prompt')
        
        if content_type == 'product':
            system_message = "You are a professional product copywriter."
        else:
            system_message = "You are a skilled blog post writer."
            
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        
        generated_content = response.choices[0].message['content']
        return render(request, 'generator/result.html', {'content': generated_content})
    
    return render(request, 'generator/generate.html')