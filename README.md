# Enterprise Resource Planning (ERP) System

A comprehensive Enterprise Resource Planning system built with Django and Django Rest Framework, providing robust business management capabilities.

## Project Structure

```
FULL-STACK-ERP-APP/
├── accounts/                    # User Authentication & Management
│   ├── __pycache__/
│   ├── migrations/
│   ├── views/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── signin.py
│   │   ├── signup.py
│   │   └── user.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── auth.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── companies/                   # Company Management
│   ├── __pycache__/
│   ├── migrations/
│   ├── utils/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core/                       # Project Core Settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── src/                       # Additional Source Files
├── tests/                     # Project-wide Tests
├── .env                      # Environment Variables
├── .gitignore
├── LICENSE
├── manage.py
├── poetry.lock
├── pyproject.toml
└── install.ps1
```

## Technology Stack

- Python 3.11+
- Django 4.2+
- Django Rest Framework
- PostgreSQL
- Simple JWT for authentication
- Poetry for dependency management

## Apps Description

### Accounts App
Handles all user-related functionality including:
- User authentication (signin/signup)
- User management
- Permission handling
- User profiles

### Companies App
Manages company-related features including:
- Company information
- Employee management
- Group/Role management
- Task management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fdantasr/full-stack-erp-app.git
cd full-stack-erp-app
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry env activate
```

4. Configure your environment variables:
```bash
cp .env.example .env
# Edit .env with your database and other configuration settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

### Accounts API

#### Create Account
```http
POST /api/v1/auth/signup
```

| Parameter  | Type     | Required |
|-----------|----------|----------|
| name      | string   | Yes      |
| email     | string   | Yes      |
| password  | string   | Yes      |

#### Login
```http
POST /api/v1/auth/signin
```

| Parameter  | Type     | Required |
|-----------|----------|----------|
| email     | string   | Yes      |
| password  | string   | Yes      |

#### Get User Profile
```http
GET /api/v1/auth/user
```

### Companies API

#### List Company Employees
```http
GET /api/v1/companies/employees
```

#### Create Employee
```http
POST /api/v1/companies/employees
```

| Parameter  | Type     | Required |
|-----------|----------|----------|
| name      | string   | Yes      |
| email     | string   | Yes      |
| password  | string   | Yes      |

#### Groups Management
```http
GET /api/v1/companies/groups
POST /api/v1/companies/groups
```

## Development

### Running Tests

```bash
# Run all tests
poetry run python manage.py test

# Run specific app tests
poetry run python manage.py test accounts
poetry run python manage.py test companies
```

### Code Quality

```bash
# Run black for code formatting
poetry run black .

# Run isort for import sorting
poetry run isort .

# Run flake8 for linting
poetry run flake8
```

## Security

All API endpoints (except authentication) require a valid JWT token:

```http
Authorization: Bearer <your_access_token>
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests to ensure everything works
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```