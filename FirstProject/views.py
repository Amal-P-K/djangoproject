from django.db import connection
from django.shortcuts import render

# View function to list actors
""" def actors_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ACTOR")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]  # Get column names

    # Convert rows to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows] """
   
def actors_list(request):
    # Hardcoded dictionary data
    data = [
        {'id': 1, 'name': 'Robert Downey Jr.', 'age': 58, 'movies': 'Iron Man, Avengers'},
        {'id': 2, 'name': 'Chris Hemsworth', 'age': 40, 'movies': 'Thor, Extraction'},
        {'id': 3, 'name': 'Scarlett Johansson', 'age': 39, 'movies': 'Black Widow, Lucy'},
        {'id': 4, 'name': 'Chris Evans', 'age': 42, 'movies': 'Captain America, Knives Out'},
    ]

    return render(request, 'actors_list.html', {'data': data})
def login(request):
    data = [
        {'id': 1, 'name': 'Robert Downey Jr.'},
        {'id': 2, 'name': 'Chris Hemsworth'},
    ]
    return render(request, 'login.html', {'data': data})
def student(request):
    data="Amal"
    return render(request,'student.html',{'data': data})
def student_list(request):
     data = [
        {"name": "Amal"},
        {"name": "Albin"},
        {"name": "Aswin"}
    ]
     return render(request,'student_list.html',{'data': data})
def student_info(request):
    data = [
        { 'name': 'Amal', 'age': 18, 'grade': 'A'},
        { 'name': 'Aswin', 'age': 20, 'grade': 'B'},
        { 'name': 'Akash', 'age': 19, 'grade': 'C'},
    ]

    return render(request, 'student_info.html', {'data': data})



def home(request):
	print("correct")
	context = {
		'message': 'Hello, Django!',
	}
	return render(request, 'home.html', context)
def students(request):
    return render(request, 'students.html')

def submit(request):
    name = request.POST.get("name")  
    age = request.POST.get("age")  
    print(name) 
    print(age)
    context = {
        'message': 'Logged in!',
        'name': name,
        'age':age,
    }
    return render(request, 'submit.html', context)