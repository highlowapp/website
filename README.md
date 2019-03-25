# Frontend


This is how to work the website test file:

First you will need to install a virtual environment:
  $ sudo apt-get install virtualenv
  
Next use virtualenv to create a virtual environment (you could call it anything you want, I just called it virtualenv):
 $ virtualenv virtualenv
 
Now run the environment(I put virtualenv in ~/Documents) :
  $ source ~/Documents/virtualenv/bin/activate
  
Now that you have that running you should install Flask:
  $ pip install Flask
  
If you are using the Auth class you will need to install the requirements onto the virtualenv:
  $ pip install -r requirements.txt
That worked for me, let me know if you have any problems.
