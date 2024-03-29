# TodoApp - Django

<p style="text-align: justify">Welcome to TodoApp, a meticulously crafted Django-based todo web application that combines robust security features including email verification, OTP authentication, and password hashing, with a clean and efficient codebase. Experience seamless task management in a protected environment, where your data's security is paramount, and your productivity is optimized. TaskGuard: Where organization meets peace of mind.</p>

---
### Installation

Create a virtual environment
```bash
  python -m venv venv
```

Install dependencies
```bash
  pip install -r requirements.txt
```

1. Make Migrations
```bash
  python manage.py makemigrations
```

2. Migrate changes to database
```bash
  python manage.py migrate
```

3. Create a super user
```bash
  python manage.py createsuperuser
```

4. Run Server
```bash
  python manage.py runserver
```

5. Email Configuration in .env file
```bash
  HOST_EMAIL = "YOUR_EMAIL"
  HOST_PASSWORD = "YOUR_PASSWORD"
```