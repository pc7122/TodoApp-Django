# TodoApp - Django

<p align="justify">Welcome to TodoApp, a meticulously crafted Django-based todo web application that combines robust security features including email verification, OTP authentication, and password hashing, with a clean and efficient codebase. Experience seamless task management in a protected environment, where your data's security is paramount, and your productivity is optimized. TaskGuard: Where organization meets peace of mind.</p>

---
### Installation

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

5. Email Configuration in settings.py
```bash
  EMAIL_HOST_USER = 'YOUR_EMAIL'
  EMAIL_HOST_PASSWORD = 'YOUR_PASSWORD'
```