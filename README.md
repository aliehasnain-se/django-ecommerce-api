# 🛒 Django E-commerce REST API

A scalable, production-ready E-commerce backend built with Django and Django REST Framework — featuring PostgreSQL database, JWT authentication, and secure environment-based configuration.

---

## 🚀 Features

- 🔐 Custom User Authentication (Djoser + JWT)
- 📦 Product & Collection Management
- 🖼️ Product Image Upload (with file size validation)
- 🛒 Cart & Cart Items API (UUID-based carts)
- 📋 Order & Order Items API (atomic transactions)
- ⭐ Product Reviews
- 👥 Role-based Permissions (Admin & Users)
- 🔍 Filtering, Search & Pagination
- 🐘 PostgreSQL Database
- 🔒 Environment Variables via `.env` (secrets hidden)
- 👤 Customer Membership System (Bronze / Silver / Gold)

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | Django & Django REST Framework |
| Authentication | JWT (Djoser) |
| Database | PostgreSQL |
| Filtering | django-filter |
| Configuration | python-dotenv / django-environ |
| Version Control | Git & GitHub |

---

## 📦 API Endpoints

### 🔑 Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/users/` | Register new user |
| POST | `/auth/jwt/create/` | Login & get JWT token |
| GET | `/auth/users/me/` | Get current user info |

### 🗂️ Collections
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/store/collections/` | List or create collections |
| GET, PUT, PATCH, DELETE | `/store/collections/<id>/` | Retrieve, update or delete a collection |

### 📦 Products
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/store/products/` | List or create products (filter, search, order) |
| GET, PUT, PATCH, DELETE | `/store/products/<id>/` | Retrieve, update or delete a product |

### 🖼️ Product Images
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/store/products/<id>/images/` | List or upload product images |
| GET, DELETE | `/store/products/<id>/images/<id>/` | Retrieve or delete a product image |

### ⭐ Reviews
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/store/products/<id>/reviews/` | List or create reviews for a product |
| GET, PUT, PATCH, DELETE | `/store/products/<id>/reviews/<id>/` | Retrieve, update or delete a review |

### 🛒 Carts
| Method | Endpoint | Description |
|---|---|---|
| POST | `/store/carts/` | Create a new cart |
| GET, DELETE | `/store/carts/<uuid>/` | Retrieve or delete a cart |
| GET, POST | `/store/carts/<uuid>/items/` | List or add items to cart |
| GET, PATCH, DELETE | `/store/carts/<uuid>/items/<id>/` | Retrieve, update or remove cart item |

### 👤 Customers
| Method | Endpoint | Description |
|---|---|---|
| POST | `/store/customers/` | Create customer profile |
| GET, PUT, PATCH | `/store/customers/me/` | View or update your own profile |
| GET, PUT, PATCH | `/store/customers/<id>/` | Admin: manage any customer |

### 📋 Orders
| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/store/orders/` | List your orders or place a new order |

---

## ⚙️ Environment Setup

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

> ⚠️ Never commit your `.env` file. Make sure `.env` is listed in `.gitignore`.

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone <repo-url>
cd project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your .env file (see above)

# 5. Apply migrations
python manage.py migrate

# 6. (Optional) Create a superuser
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

---

## 🗄️ Database Configuration

Make sure PostgreSQL is installed and a database is created:

```sql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
```

`settings.py` database config:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

---
