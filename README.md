# student-exam-tracker

````markdown
# Flask Student Exam Tracker

A simple Flask web application to track exam papers with file uploads, status tracking, and user authentication.

---

## Features

- User registration, login, and logout
- Secure password hashing
- Dashboard for adding, editing, and viewing exams
- Upload application and fee files per exam
- Mark exams as completed with a checkbox
- Responsive design using Bootstrap 5
- Flash messages for user feedback

---

## Technology Stack

- Python 3.10+
- Flask
- Flask-WTF (Forms & CSRF protection)
- Flask-SQLAlchemy (ORM with SQLite)
- Bootstrap 5 (Frontend CSS framework)
- Werkzeug (Password hashing)
- Gunicorn (Production WSGI server)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/exam-tracker.git
   cd exam-tracker
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables (optional but recommended):

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   export SECRET_KEY="your_secret_key_here"
   ```

5. Initialize the database:

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. Run the app:

   ```bash
   flask run
   ```

---

## Usage

* Register a new user on `/register`
* Login on `/login`
* Access your exam dashboard on `/dashboard`
* Add, edit, mark completion, and upload exam documents
* Logout when finished

---

## File Uploads

Uploaded files are saved in the `/static/uploads/` directory. Make sure this folder exists and is writable.

---

## Deployment

For deploying the app, consider using:

* [Render.com](https://render.com)
* [PythonAnywhere](https://www.pythonanywhere.com)
* [Replit](https://replit.com)

Make sure to:

* Use a production-ready WSGI server like `gunicorn`
* Set environment variables for `SECRET_KEY` and database URI
* Secure your upload folder properly

---

## Folder Structure

```
├── app.py
├── models.py
├── forms.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
├── static/
│   ├── uploads/
│   └── style.css
└── README.md
```

---

## License

MIT License © Swaraj Dhage

---

## Contact

For any questions or feedback, reach out at dhageswaraj1000@gmail.com
---

```

If you want me to help generate your **`requirements.txt`** or other project files, just ask!
```
