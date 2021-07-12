from django.shortcuts import  render
from datetime import datetime
from home.models import Contact,Summarize,Generation,Sentiment,Question
from django.contrib import messages
from transformers import pipeline,DistilBertTokenizer, DistilBertForQuestionAnswering
import json
import torch
# Create your views here.
def index(request):
    
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def summarizer(request):
    if request.method == "POST":
        articles = request.POST.get('message')
        num_words = int(request.POST.get('num'))
        summarizer = pipeline('summarization')
        summary = summarizer(articles, min_length=num_words)
        s1 = json.dumps(summary[0])
        d2 = json.loads(s1)
        result_summary = d2['summary_text']
        result_summary = '. '.join(list(map(lambda x: x.strip().capitalize(), result_summary.split('.'))))
        context = {'result_summary': result_summary}
        summarize = Summarize(original_text=articles,desc_summary=result_summary,date_time=datetime.today())
        summarize.save()
        return render(request,'summarizer.html', context)
    else:
        return render(request,'summarizer.html')

def generation(request):
    if request.method == "POST":
        message = request.POST.get('message')
        
        text_generator = pipeline('text-generation')
        generator = text_generator(message, max_length=100)
        s1 = json.dumps(generator[0])
        d2 = json.loads(s1)
        generated_text = d2['generated_text']
        generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
        context = {'generated_text': generated_text}
        generation = Generation(incomp_text=message,gen_text=generated_text,date_time=datetime.today())
        generation.save()
        return render(request,'generation.html', context)
    else:
        return render(request,'generation.html')

def sentiment(request):
    if request.method == "POST":
        message = request.POST.get('message')
        
        classifier = pipeline('sentiment-analysis')
        sentiment = classifier(message)
        s1 = json.dumps(sentiment[0])
        d2 = json.loads(s1)
        sentiment_label = d2['label']
        context = {'sentiment': sentiment_label}
        sentiment = Sentiment(doc_text=message,sentiment=sentiment_label,date_time=datetime.today())
        sentiment.save()
        return render(request,'sentiment.html', context)
    else:
        return render(request,'sentiment.html')

def question(request):
    if request.method == "POST":
        content = request.POST.get('message')
        question = request.POST.get('name')
        
        question_answering = pipeline("question-answering")
        result = question_answering(question=question, context=content)
        s1 = json.dumps(result)
        d2 = json.loads(s1)
        generated_text = d2['answer']
        generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
        context = {'answer': generated_text}
        questions = Question(con_text=content,question=question,answer=generated_text,date_time=datetime.today())
        questions.save()
        return render(request,'question.html', context)
    else:
        return render(request,'question.html')
  

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
    
        contact = Contact(name=name, email=email,desc=message,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent")
    return render(request,'contact.html')

# Create your views here.
