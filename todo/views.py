from django.shortcuts import render
from .models import Todo
from pymongo import MongoClient
from datetime import datetime
from django.http import HttpResponseRedirect

def connect():
    conn = MongoClient('localhost' , 27017)
    db = conn.database_name
    print("DB name: " , db)
    collection = db.collection_name
    print("Collection name: " , collection)
    return collection


def add_data(request):
    # print("adding data")
    collection = connect()
    task_text = request.POST.get('enter')
    data_length = collection.find().count()
    # print(data_length)
    data = {
        'id' : data_length + 1,
        'text' : task_text,
        'added_date' : datetime.now().strftime("%B %d %Y , %H:%M:%S"),
    }
    
    data_to_db = collection.insert_one(data)
    print("Data inserted:")
    return data , collection


def home(request):
    collection = connect()
    all_tasks = collection.find().sort("added_date")
    if request.POST:
        print("KEY found", request.POST)
        collection.delete_one({'id' : int(request.POST['delete'])})
    return render(request , 'todo/main.html' , {'todo_tasks' : all_tasks})


def todo_tasks(request):
    add_data(request)
    return HttpResponseRedirect("/")
