This Todo App is made using python , django , mongodb.
It will add your task and shows it to you on the screen and task will be deleted by just clicking delete button
With connection to mongodb it will save your tasks into database having tasks , date and id fields.

Procfile is needed if you are deploying your application to heroku server and for that you need to install django-heroku and gunicorn libraries using pip. To deploy into heroku live server check this out: https://medium.com/@qazi/how-to-deploy-a-django-app-to-heroku-in-2018-the-easy-way-48a528d97f9c 


Localhosting:
In master branch databse will be hosted on locally

ServerHosting:
In server_db branch database will be hosted on MongoDB Atlas server

you can find the difference in 
'todo/views.py':
  here difference is in connect()

'settings.py':
  here difference is in DATABASE = [] 
   
Image of it:
![](images/todo.png)
