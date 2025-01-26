"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.db import connection
from django.shortcuts import render, redirect

# Inline view function for actors_list
def actors_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ACTOR")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]  # Get column names

    # Convert rows to a list of dictionaries
    data = [dict(zip(columns, row)) for row in rows]

    return render(request, 'actors_list.html', {'data': data})

# Inline view function for home (redirecting to /actors/)
def home(request):
    return redirect('actors_list')  # Redirect to actors list page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', actors_list, name='actors_list'),
    path('', home, name='home'),  # Route for root, redirects to actors list
]