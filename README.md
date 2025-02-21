# 💻📱 Sistema de Gestão Empresarial (ERP)

Esta documentação descreve a implementação de um Sistema de Gestão Empresarial (ERP), desenvolvido com tecnologias modernas, incluindo **ReactJS** para o frontend e **Django Rest Framework** para o backend.

## ⛏️ Instalação

Para executar o projeto, utilize o seguinte comando:

```bash
py manage.py runserver
```

## 💎 Tecnologias Utilizadas

**Frontend:** ReactJS, TypeScript, React Router, Redux, Material UI, Axios  
**Backend:** Django, Django Rest Framework, Simple JWT

---

# 📌 Documentação da API

## 🔐 Autenticação

### Criar uma conta

```http
POST /api/v1/auth/signup
```

#### Parâmetros

| Parâmetro  | Tipo     | Descrição       |
|-------------|----------|----------------|
| `name`      | `string` | **Obrigatório** |
| `email`     | `string` | **Obrigatório** |
| `password`  | `string` | **Obrigatório** |

### Fazer login

```http
POST /api/v1/auth/signin
```

#### Parâmetros

| Parâmetro  | Tipo     | Descrição       |
|-------------|----------|----------------|
| `email`     | `string` | **Obrigatório** |
| `password`  | `string` | **Obrigatório** |

### Obter informações do usuário autenticado

```http
GET /api/v1/auth/user
```

#### Cabeçalho

| Parâmetro        | Tipo     | Descrição                            |
|------------------|----------|---------------------------------|
| `Authorization`  | `string` | **Obrigatório**. Access Token |

---

## 🏢 Empresas e Funcionários

### Listar funcionários de uma empresa

```http
GET /api/v1/companies/employees
```

### Criar um funcionário

```http
POST /api/v1/companies/employees
```

#### Parâmetros

| Parâmetro  | Tipo     | Descrição       |
|-------------|----------|----------------|
| `name`      | `string` | **Obrigatório** |
| `email`     | `string` | **Obrigatório** |
| `password`  | `string` | **Obrigatório** |

### Obter um funcionário

```http
GET /api/v1/companies/employees/{id}
```

#### Parâmetros

| Parâmetro | Tipo     | Descrição                     |
|------------|----------|--------------------------------|
| `id`       | `number` | **Obrigatório**. ID do funcionário |

### Atualizar dados de um funcionário

```http
PUT /api/v1/companies/employees/{id}
```

#### Parâmetros

| Parâmetro  | Tipo     | Descrição                                        |
|-------------|----------|-------------------------------------------------|
| `id`        | `number` | **Obrigatório**. ID do funcionário                |
| `groups`    | `string` | **Opcional**. Lista de IDs de grupos             |
| `name`      | `string` | **Opcional**                                     |
| `email`     | `string` | **Opcional**                                     |

### Deletar um funcionário

```http
DELETE /api/v1/companies/employees/{id}
```

---

## 📊 Tarefas

### Listar tarefas de uma empresa

```http
GET /api/v1/companies/tasks
```

### Criar uma tarefa

```http
POST /api/v1/companies/tasks
```

#### Parâmetros

| Parâmetro    | Tipo     | Descrição                         |
|--------------|----------|--------------------------------|
| `employee_id` | `number` | **Obrigatório**. ID do funcionário  |
| `status_id`   | `number` | **Obrigatório**. ID do status da tarefa |
| `title`       | `string` | **Obrigatório**                         |
| `description` | `string` | **Opcional**                          |
| `due_date`    | `date`   | **Opcional**. Formato: d/m/Y H:M     |

### Obter uma tarefa

```http
GET /api/v1/companies/tasks/{id}
```

### Atualizar uma tarefa

```http
PUT /api/v1/companies/tasks/{id}
```

### Deletar uma tarefa

```http
DELETE /api/v1/companies/tasks/{id}
```

---

## 🔑 Permissões e Grupos

### Listar grupos de uma empresa

```http
GET /api/v1/companies/groups
```

### Criar um grupo

```http
POST /api/v1/companies/groups
```

#### Parâmetros

| Parâmetro    | Tipo     | Descrição                                 |
|--------------|----------|--------------------------------|
| `name`       | `string` | **Obrigatório**                         |
| `permissions`| `string` | **Obrigatório**. Lista de IDs de permissões |

### Obter um grupo

```http
GET /api/v1/companies/groups/{id}
```

### Atualizar um grupo

```http
PUT /api/v1/companies/groups/{id}
```

### Deletar um grupo

```http
DELETE /api/v1/companies/groups/{id}
```

### Listar permissões disponíveis

```http
GET /api/v1/companies/permissions
```

---

Esta documentação fornece informações detalhadas sobre os endpoints da API, garantindo uma integração eficiente e segura ao sistema de gestão empresarial.

