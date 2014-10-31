# Pyladies Web App 101


A starter 'to do' app built using Flask.


## Getting Started
 _Assumes you already have Python, pip, and virtualenv installed. If you don't, please refer to [this guide](https://github.com/florapdx/pyladies_guides/blob/master/mac_installs.md)_


 1. Make a new project directory and virtual environment:

 ```$ mkdir pyladies_webapp && cd pyladies_webapp```

 ```$ mkdir venv && virtualenv venv```

 ```$ source venv/bin/activate```


 2. Clone the repo and install requirements:

 ```$ git clone https://github.com/florapdx/pyladies_webapp101.git```

 ```$ cd pyladies_webapp101```

 ```$ pip install -r requirements/development.txt```


 3. Set up the database:

 ```
 # DB scripts sourced from Miguel Grinberg's awesome [Flask Mega Tutorial](from http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
 $ python db_create.py
 ```

 ```
 # This isn't really necessary yet, but go ahead and run a migration anyway.# You should see some output with a version number and migration name:
 $ python db_migrate.py
 ```

 4. You're now ready to run the app:
 ```
 # This command starts the server and prints a local address where you can find the app in your browser:
 $ python run.py
 ```



