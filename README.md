# PhiMart – E-commerce REST API (Django Rest Framework)

PhiMart is a full-featured E-commerce backend built using **Django Rest Framework (DRF)**.  
It provides RESTful APIs for managing products, categories, carts, and orders with secure **JWT authentication** and interactive **Swagger API documentation**.

This project is designed as a scalable backend for modern e-commerce applications.

---

## Features

- User authentication & authorization (JWT) using **Djoser**
- Product management (CRUD)
- Category management
- Shopping cart system
- Order management
- Secure endpoints with permissions
- Interactive API documentation (Swagger & Redoc)
- Clean and modular project structure

---

## Tech Stack

- Python
- Django
- Django Rest Framework (DRF)
- Djoser (JWT Authentication)
- drf-yasg (Swagger Documentation)
- SQLite / PostgreSQL (Database)

---

## API Modules

| Module     | Description |
|------------|------------|
| Products   | Manage product listings |
| Categories | Product categorization |
| Carts      | User shopping carts |
| Orders     | Order placement & tracking |
| Auth       | JWT-based authentication |

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/phimart.git
cd phimart

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```


```
pip install -r requirements.txt
```

```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
API Documentation
Swagger UI:
```
http://127.0.0.1:8000/swagger/
```
Redoc:
```
http://127.0.0.1:8000/redoc/
```
Authentication
This project uses JWT Authentication via Djoser.

Login
POST /auth/jwt/create/
Refresh Token
POST /auth/jwt/refresh/
Register
POST /auth/users/
Add token to headers:

Authorization: Bearer <your_token>
```

