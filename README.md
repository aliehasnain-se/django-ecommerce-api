# Django E-commerce REST API

A scalable E-commerce backend built with Django and Django REST Framework.

## 🚀 Features
- Custom User Authentication (Djoser + JWT)
- Product & Collection Management
- Cart & Cart Items API
- Order & Order Items API
- Product Reviews
- Product Images Upload
- Role-based Permissions (Admin & Users)
- Filtering, Search, Pagination

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite (PostgreSQL ready)
- Git & GitHub

## 📦 API Endpoints
- /store/products/
- /store/collections/
- /store/carts/
- /store/orders/
- /auth/users/
- /auth/jwt/create/

## ▶ How to Run
```bash
git clone <repo-url>
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver