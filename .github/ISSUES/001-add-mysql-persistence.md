# Add persistent MySQL storage for activities and students

## Summary
Add a MySQL database and persistence layer so activities and student signups survive server restarts.

## Why
Currently data is in-memory. Persistence is required for real usage and for admin operations.

## Acceptance criteria
- Add SQL schema and migrations (activities, students, enrollments).
- Integrate SQLAlchemy (or equivalent) with FastAPI.
- Replace in-memory `activities` with DB-backed models and CRUD.
- Update README with setup steps and a sample `student.sql` import.

## Implementation notes
- Use `SQLAlchemy` + `alembic` or `Tortoise-ORM` for simplicity.
- Add `requirements.txt` updates: `sqlalchemy`, `alembic`, `pymysql` (or `mysqlclient`).
- Provide a simple local Docker Compose sample with MySQL for development (optional).

## Labels
- enhancement, backend, database
