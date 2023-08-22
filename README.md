# [plant_app](git@github.com:ivanmarinoff/My-Plant.git)


This is a `Plant App` course project built with  **Django**.
> Example project by [SoftUni](http://www.softuni.bg").

<br>

## This is a App `Home page`

![home_page](https://github.com/ivanmarinoff/My-Plant/assets/107050101/d0c85bae-096c-4882-8cb2-d0b797e28a73)

<br />

## This is a `Profile details` page
![profile_details](https://github.com/ivanmarinoff/My-Plant/assets/107050101/43094ed9-eec1-4110-be4f-5f383bf131c2)

<br />

## This is a `Create Plant` view
![Create_plant](https://github.com/ivanmarinoff/My-Plant/assets/107050101/17b0ec44-984b-448d-bfc4-4916286c8edb)

<br />

## This is a `Catalogue` page

![catalogue](https://github.com/ivanmarinoff/My-Plant/assets/107050101/0b356ac7-5a9d-435a-90cd-e5dfab714768)

<br />

## This is a `Django Admin` page
![admin](https://github.com/ivanmarinoff/My-Plant/assets/107050101/5f93707a-fe48-4e84-a5df-0bac2c2ac0a2)


<br />

- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Create user` page
  - `Create plant` page
  - `Catalogue` page 
  

## How to use it
<br />

> **Install the package** via `PIP` 

```bash
$ Use the pip install -r requirements.txt command 
// OR
$ pip install git@github.com:ivanmarinoff/My-Plant.git
```

<br />

> Use command `venv\Scripts\activate` in to terminal to create `venv` file of your Django project directory!

<br />

> **Start the app**
> To set up SQLite database run the `db.sqlite3` file


```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />
