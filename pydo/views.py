from django.shortcuts import render
import wikipedia
import wolframalpha


# Create your views here.
def home(request):
    query = request.GET.get('q')
    if query:
        print(query)
        while True:
            try:
                # wolframalpha
                app_id ="7KAKPE-A6T6EEQR3L"
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                answer = next(res.results).text
                print(answer)
                if answer:
                    print(answer)
                    return render(request, 'index.html', {'answer': answer})
                else:
                    print("Not Found!")
                    answer = query+" Not Found!"
                    return render(request, 'index.html', {'answer': answer})
            except:
                # wikipedia
                wikipedia.set_lang("bn")
                answer = wikipedia.summary(query)
                if answer:
                    print(answer)
                    return render(request, 'index.html', {'answer': answer})
                else:
                    print("Not Found!")
                    answer = query+" Not Found!"
                    return render(request, 'index.html', {'answer': answer})
    else:
        return render(request, 'index.html')
