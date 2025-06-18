
# ✅ Django To-Do List App

A beginner-friendly To-Do List web application built with Django. It allows users to create, update, delete, and mark tasks as complete. Ideal for learning Django fundamentals like models, views, templates, and URL routing.

## 📌 Features

- Add new tasks
- Edit and update tasks
- Mark tasks as completed/incomplete
- Delete tasks
- Clean and simple UI using HTML, CSS & JavaScript

## 🛠️ Tech Stack

- **Framework:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (Django default)

## 🖥️ Live Demo

> _Not deployed yet_  

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo-django.git
cd todo-django
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can install Django directly:

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit in your browser:  
👉 http://127.0.0.1:8000/

## 📁 Project Structure

```plaintext
todo_project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── todo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── todo/
│   │       ├── list.html
│   │       └── form.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
```

## 🎯 Future Enhancements

- Add user authentication (Login/Register)
- Add due dates to tasks
- Responsive UI 
- Task filtering and sorting

## 🙋‍♂️ Author

**Viom Shrotriya**  
[GitHub](https://github.com/ghansham01)
