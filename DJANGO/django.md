### Migrations and Migrate

#### makemigrations
(Creates migration files based on model changes)
- Looks at changes in your models
- Generates migration files (Python files)
- These files describe what needs to change in the database
- It does not change the database
```bash
python manage.py makemigrations

output:- creates file app_name/migrations/0001_initial.py
```
the above This file contains instructions like: create table, add column, remove field, alter field

#### migrate
(Applies migration files to the database)
- Executes migration files
- Actually creates / updates database tables
- Keeps track of applied migrations in django_migrations table
```bash
python manage.py migrate
```
Result: Tables created, Columns added/modified, Database schema updated

```bash
# 1. Change models.py
# 2. Create migration file
python manage.py makemigrations

# 3. Apply changes to DB
python manage.py migrate
```

#### migration File
A **migration file** contains a **Migration class** with dependencies and operations that describe database schema changes such as creating tables, adding fields, or modifying columns.
```bash
from django.db import migrations, models

class Migration(migrations.Migration):
    # Present in the first migration, Tells Django this is the app’s initial DB structure
    initial = True

    dependencies = [
    ]

# most important, This is where actual database instructions live.
    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
```
```bash
# Ensures order of execution
# Required when: ForeignKey to another app, Depends on earlier migrations
dependencies = [
    ('auth', '0012_alter_user_first_name_max_length'),
]

# eg:- ForeignKey(User) → depends on auth app migration
```
```bash
# Common Migration Operations
# Create Table
migrations.CreateModel()
# Add Field
migrations.AddField(
    model_name='student',
    name='email',
    field=models.EmailField(),
)
# Remove Field
migrations.RemoveField(
    model_name='student',
    name='age',
)
# Alter Field
migrations.AlterField(
    model_name='student',
    name='name',
    field=models.CharField(max_length=200),
)
# Delete Table
migrations.DeleteModel(
    name='Student',
)
# Custom SQL / Python Code
migrations.RunSQL("UPDATE student SET age=18")
migrations.RunPython(forward_func, reverse_func)
# Used for: Data migrations, Backfilling data
```
##### How Django Knows What Changed
Django compares: current models.py, last migration file.
Generates new migration with only the differences

### Django Request–Response Cycle (High-Level View)

The Django request–response cycle starts when a client sends a request to the WSGI/ASGI server, passes through middleware, URL routing, view logic, optional model and template processing, and returns a response back through middleware to the client.
```bash
Client
  ↓
WSGI/ASGI
  ↓
Middleware (request)
  ↓
URL Resolver
  ↓
View
  ↓
Model / DB
  ↓
Template (optional)
  ↓
Response
  ↓
Middleware (response)
  ↓
Client

```
1️⃣ Client Sends Request

Browser / Mobile app sends an HTTP request
Example: GET /api/users/

2️⃣ WSGI / ASGI Server

Request first hits:
- WSGI → synchronous apps
- ASGI → async apps (WebSockets, async views)
Converts raw HTTP request into a Django HttpRequest object

3️⃣ Middleware (Request Phase)

Middleware is a chain of hooks. Each middleware can: Modify request, Block request, Add data (user, session, etc.)

📌 Common middleware actions: Authentication, Session handling, CSRF validation, Logging
Flow:-
```bash
Request → Middleware 1 → Middleware 2 → ...
```

4️⃣ URL Dispatcher (urls.py)

Django matches URL against urls.py
```bash
Eg:- path('users/', views.user_list)
```
Chooses the correct view function/class

5️⃣ View (Business Logic)

View processes request.
Interacts with: Models (database), External APIs, Serializers (DRF)
Eg:- 
```bash
def user_list(request):
    users = User.objects.all()
    return JsonResponse({"users": users})
```
6️⃣ Model (Database Interaction)

- ORM converts Python code → SQL
- Fetches / inserts / updates data
- Returns QuerySets to view

7️⃣ Template Rendering (Optional)

- For web apps (not APIs)
- Combines: HTML template, Context data
- (Skipped in REST APIs)
```bash
return render(request, "users.html", context)
```

8️⃣ Response Object Created

View returns: HttpResponse, JsonResponse, Response (DRF)

9️⃣ Middleware (Response Phase)

Same middleware runs in reverse order.
Can: Modify response, Add headers, Compress response
```bash
Middleware N → Middleware 2 → Middleware 1 → Client
```

🔟 Server Sends Response to Client

- Final HTTP response sent back
- Browser renders it / API client reads it

### Middlewares

**Middleware** is a framework of hooks that allows Django to process requests and responses globally before views are executed and after responses are returned.

**Middleware** is a layer between the **request** and the **response** that processes requests before they reach the view and responses before they go back to the client.
👉 Think of middleware as filters or hooks in Django’s request–response cycle.
Middleware is used for cross-cutting concerns like authentication, security, logging, and request/response modification in Django.
```bash
Request → Middleware → View → Middleware → Response
```
Runs twice
- Once while request comes in
- Once while response goes out

#### ⚙️ What Middleware Can Do

**During Request**
- Authenticate user
- Check permissions
- Validate CSRF token
- Block or redirect requests
- Add request attributes

**During Response**
- Add headers
- Modify response content
- Handle exceptions
- Logging
- Compression

#### Common Built-in Django Middlewares
| Middleware                 | Purpose             |
| -------------------------- | ------------------- |
| `SecurityMiddleware`       | Security headers    |
| `SessionMiddleware`        | Session handling    |
| `AuthenticationMiddleware` | Adds `request.user` |
| `CsrfViewMiddleware`       | CSRF protection     |
| `CommonMiddleware`         | URL normalization   |
| `MessageMiddleware`        | Flash messages      |

#### How Middleware Is Configured
In settings.py:
```bash
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```
#### Custom Middleware Example

Step 1️⃣ Create Middleware
```bash
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")

        response = self.get_response(request)

        print("After view")
        return response
```
Step 2️⃣ Register Middleware
```bash
MIDDLEWARE.append('app.middleware.SimpleMiddleware')
```

#### Exception Handling in Middleware
Middleware can catch exceptions:
```bash
def process_exception(self, request, exception):
    return HttpResponse("Something went wrong")
```

### Hooks
**Hooks** are predefined execution points in Django’s request–response lifecycle where middleware code is automatically invoked.
**Hooks** are like checkpoints on a highway where Django allows middleware to inspect, modify, or stop traffic.
A hook is simply a predefined place where Django lets you plug in your own code so it runs automatically at a specific point in the request–response cycle.
- Hooks = predefined interception points

#### Hooks in Django Middleware (Lifecycle Points)

Django calls middleware code at specific hooks during request handling.

**1️⃣ Request Hook (Before View)**
```bash
def __call__(self, request):
```
Runs before the view.
Can: Modify request, Block request, Return response directly

**2️⃣ View Hook (Before View Is Called)**
```bash
def process_view(self, request, view_func, view_args, view_kwargs):
```
Runs just before view execution
Used for: Permission checks, Conditional logic based on view

**3️⃣ Exception Hook**
```bash
def process_exception(self, request, exception):
```
Runs if the view raises an exception. Can return custom error response

**4️⃣ Response Hook (After View)**
```bash
response = self.get_response(request)
```
Runs after view returns response
Can: Modify headers, Log response, Compress data

Flow:-
```bash
Request
  ↓
process_request / __call__
  ↓
process_view
  ↓
View
  ↓ (exception?)
process_exception
  ↓
process_response / __call__
  ↓
Response
```
#### Why Hooks Are Important
Hooks allow you to:
- Add authentication globally
- Enforce security rules
- Log requests
- Modify responses
- Handle errors centrally

Without hooks: Logic would be duplicated in every view

**⚠️ Modern Django Note (Very Important)**

*Old-style middleware had:*
- process_request
- process_response

*New-style middleware (current Django) uses:*
- __init__
- __call__
- optional process_view, process_exception