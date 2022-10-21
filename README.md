######

#unzip the file and cd into the Doctor directory
#install virtual environment

virtualenv env
#start the virtual environement
source env/Scripts/activate

#delete my database and perform the migrations
#perfom the migrations
python manage.py makemigrations
python manage.py migrate
#create superuser (if on windows run this command)
winpty python manage.py createsuperuser

#run the server
python manage.py runserver

#navigate to homepage
http://127.0.0.1:8000

#signup a user
#signup a doctor with usernames (john, liz, all and sam)
#login as user and book and appointment, view your bookings,
#login as doctor and view your bookings.
