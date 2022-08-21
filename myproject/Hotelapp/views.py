from .models import signup
from . import forms
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
import sqlite3 as sql

def index(request):
      return render(request, 'Layout/firstpage.html')

def validate(request):
    if request.method == 'POST':
        name= request.POST['txt']
        email= request.POST['email']
        pswd= request.POST['pswd']
        c="Hii"+" "+name
        obj=signup()
        obj.name=name
        obj.email=email
        obj.password=pswd
        print(name)
        print(email)
        obj.save()
        send_mail('Testing Mail',c,'gopikumarreddy.38@gmail.com',[email])
        dict = {
         'name': name,
         'email': email,
         'password':pswd,
        }
        return render(request, 'Layout/validate.html',dict)   

def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        pswd= request.POST['pswd']
        print(pswd)
        print(email)
        con = sql.connect("db.sqlite3")
        cur = con.cursor()
        statement = f"SELECT * from Hotelapp_signup WHERE email='{email}' AND Password = '{pswd}';"
        cur.execute(statement)
        y=str(cur.fetchone()[1])
        print(y)
        if y=="":
            print("Login failed")
            return render(request, 'Layout/firstpage.html')
        else:
            print("Welcome"+" "+y)
            dict = { 'name': y}
            return render(request, 'Layout/home.html',dict)   
    return render(request, 'Layout/firstpage.html')

def payment(request):
    if request.method == 'POST':
        print("ravi kumar")
        client = razorpay.Client(auth=("rzp_test_XW7SQh9tEBkXfp","YvYNA8Y5DQ5RwobkCa2NxENL"))
        DATA = {    "amount": 1000,    "currency": "INR",    "receipt": "receipt#1"}
        client.order.create(data=DATA)
        return render(request,'Layout/payment.html')
    





    



    