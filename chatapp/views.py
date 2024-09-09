from django.shortcuts import render
from openai import OpenAI
from django.conf import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def chat_gpt(request):
    content = ""
    user_prompt = ""

    if request.method == "POST":
        user_prompt = request.POST.get("prompt", "")
        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                model="gpt-4o",
            )
            content = response.choices[0].message.content.strip()


            if not content:
                print("No response content.")
        except Exception as e:
            print(f'something went wrong ', e)

    return render(request, "home.html", context={
        'page': 'Chat GPT',
        'response': content,
        'user_prompt': user_prompt
    })
