# IK Seoul Django CMS

## Local run

SQLite works automatically for local development:

```powershell
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py seed_content
$env:CMS_ADMIN_PASSWORD = "choose-a-strong-password"
.\venv\Scripts\python.exe manage.py bootstrap_admin
.\venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` for the public site and
`http://127.0.0.1:8000/dashboard/` for the CMS. During local development,
`http://dash.localhost:8000/` also redirects to the CMS. The custom CMS is
available directly during local development and does not use Django admin login.

## PostgreSQL

PostgreSQL 18 is installed locally and listens on `localhost:5432`.
Create the dedicated database with the PostgreSQL password chosen during
installation:

```powershell
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -h localhost -U postgres -f .\postgres_setup.sql
Copy-Item .env.example .env
```

Replace the placeholder secrets in `.env`, then run:

```powershell
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py seed_content
```
