# Task Management System API

A Django REST Framework backend API for managing tasks with authentication, categories, filtering, pagination, soft delete, and analytics.

---

## 🚀 Features

- User authentication (JWT)
- Task CRUD operations
- Category system (user-based)
- Task filtering (completed, category)
- Search (title + category name)
- Ordering (created_at, title)
- Pagination
- Soft delete (trash & restore)
- Task statistics dashboard
- Custom actions (toggle, mark all completed)
- Swagger API documentation

---

## 🔐 Authentication

This API uses JWT authentication.

### Login flow:
1. Register user
2. Obtain token
3. Use token in headers:

Authorization: Bearer <your_token>


---

## 📦 API Endpoints

### Auth
- POST `/api/register/`
- POST `/api/login/`
- POST `/api/token/`
- POST `/api/token/refresh/`

---

### Tasks
- GET `/api/tasks/`
- POST `/api/tasks/`
- GET `/api/tasks/{id}/`
- PATCH `/api/tasks/{id}/`
- DELETE `/api/tasks/{id}/`

---

### Custom Task Actions
- GET `/api/tasks/trash/`
- POST `/api/tasks/{id}/restore/`
- POST `/api/tasks/{id}/toggle/`
- POST `/api/tasks/mark-all-completed/`

---

### Stats
- GET `/api/tasks/stats/`

---

## 🧠 Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- MySQL (or SQLite)
- drf-yasg (Swagger)

---

## 📄 API Documentation

Swagger UI available at:
/swagger/


---

## ⚙️ Installation

```bash
git clone <repo-url>
cd project-folder
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 👨‍💻 Author

Built by me... a backend developer learning Django REST Framework.

