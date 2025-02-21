# Enterprise Resource Planning (ERP) System

A comprehensive Enterprise Resource Planning system built with modern technologies, featuring a ReactJS frontend and Django Rest Framework backend.

## Overview

This project implements a complete business management solution with features including:
- User Authentication and Authorization
- Employee Management
- Role-based Access Control
- Task Management
- Company Administration

## Technology Stack

### Frontend
- ReactJS
- TypeScript
- React Router
- Redux
- Material UI
- Axios

### Backend
- Django
- Django Rest Framework
- Simple JWT

## Getting Started

### Prerequisites
- Python 3.x
- Node.js
- npm or yarn

### Installation

Start the development server:

```bash
python manage.py runserver
```

## API Documentation

### Authentication

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

*Requires Authentication Token*

### Employee Management

#### List Company Employees
```http
GET /api/v1/companies/employees
```

*Requires Authentication*

#### Create Employee
```http
POST /api/v1/companies/employees
```

| Parameter  | Type     | Required |
|-----------|----------|----------|
| name      | string   | Yes      |
| email     | string   | Yes      |
| password  | string   | Yes      |

#### Get Employee Details
```http
GET /api/v1/companies/employees/{id}
```

#### Update Employee
```http
PUT /api/v1/companies/employees/{id}
```

| Parameter  | Type     | Required | Description           |
|-----------|----------|----------|-----------------------|
| groups    | string   | No       | Array of group IDs    |
| name      | string   | No       |                       |
| email     | string   | No       |                       |

### Groups and Permissions

#### List Groups
```http
GET /api/v1/companies/groups
```

#### Create Group
```http
POST /api/v1/companies/groups
```

| Parameter    | Type     | Required | Description              |
|-------------|----------|----------|--------------------------|
| name        | string   | Yes      |                          |
| permissions | string   | Yes      | Array of permission IDs  |

#### Get Group Details
```http
GET /api/v1/companies/groups/{id}
```

#### List Available Permissions
```http
GET /api/v1/companies/permissions
```

### Task Management

#### List Tasks
```http
GET /api/v1/companies/tasks
```

#### Create Task
```http
POST /api/v1/companies/tasks
```

| Parameter    | Type     | Required | Description              |
|-------------|----------|----------|--------------------------|
| employee_id | number   | Yes      |                          |
| status_id   | number   | Yes      |                          |
| title       | string   | Yes      |                          |
| description | string   | No       |                          |
| due_date    | date     | No       | Format: d/m/Y H:M        |

#### Get Task Details
```http
GET /api/v1/companies/tasks/{id}
```

#### Update Task
```http
PUT /api/v1/companies/tasks/{id}
```

| Parameter    | Type     | Required | Description              |
|-------------|----------|----------|--------------------------|
| employee_id | number   | No       |                          |
| status_id   | number   | No       |                          |
| title       | string   | No       |                          |
| description | string   | No       |                          |
| due_date    | date     | No       | Format: d/m/Y H:M        |

## Security

All API endpoints (except authentication) require a valid authentication token. Include the token in the Authorization header:

```http
Authorization: Bearer <your_access_token>
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```