<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Welcome to Django</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This is a project to study Django framework based on the book "Django 5 by example"
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Before start, verify if you have all the rquirement below:

- You have installed the Python version `3.12` or newer.
```
python -v
```
- You have created a virtual environment.
     - Linux e macOS:
    ```
    python -m venv my_env # create isolated environment
    source my_env/bin/activate # activate the environment
    ```
    - Windows:
    ```
    py -m venv my_env # create isolated environment
    .\my_env\Scripts\activate # activate the environment
    ```
- You have installed the Django version `5.1.4`.

    ```
    pip install django~=5.1.4
    django --version
    ```

### Installing

After clone this repository, go to the the directory and open shell in this location

Change to the directory named 'welcome-to-django-project':

```
cd welcome-to-django-project
```

Apply database migrations with the command:

```
python manage.py migrate
```

Run development server:

```
python manage.py runserver
```

## 🚀 Running the application <a name = "deployment"></a>

Open the terminal and inside the welcome-to-django-project run development server:

```
python manage.py runserver
```
The terminal will show the localhost url (ps.: http://127.0.0.1:8000/).

As for now, we have 2 endpoint:
- http://127.0.0.1:8000/blog
- http://127.0.0.1:8000/foodlog (in development)

## 🔧 Running the tests <a name = "tests"></a>

TBD: ~~Explain how to run the automated tests for this system.~~

### Break down into end to end tests

TBD: ~~Explain what these tests test and why~~

```
Give an example
```

### And coding style tests

TBD: ~~Explain what these tests test and why~~

```
Give an example
```

## 🎈 Useful Commands <a name="useful"></a>

Create an inital project file structure (Don't need for this project because it's already created).
```
django-admin startproject mysite
```

Applying inital database migrations
```
python manage.py migrate
```

Create and applying migrations after altered a model
```
python manage.py makemigrations
```

Create an application
```
python manage.py startapp blog
```

Running the development server
```
python manage.py runserver
```

Open a Python shell
```
python manage.py shell
```

## 🚀 Deployment <a name = "deployment"></a>

TBD: ~~Add additional notes about how to deploy this on a live system.~~

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Prgramming Language
- [Django](https://www.djangoproject.com/) - Web Framework
- [PostgreSQL](https://www.postgresql.org/) - Database

## ✍️ Authors <a name = "authors"></a>

- [@fmassaretto](https://github.com/fmassaretto) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Django by 5 example book
