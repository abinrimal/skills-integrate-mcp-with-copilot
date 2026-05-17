# Add authentication and multi-role support (admin, staff, student)

## Summary
Add user accounts, authentication (session or token-based), and role-based access control to separate admin features from student actions.

## Why
Admin flows (add/remove students, add subjects) require authentication and role enforcement.

## Acceptance criteria
- Implement user model with roles: `admin`, `staff`, `student`.
- Add login/logout (session cookies) or JWT-based auth for the API.
- Protect admin endpoints and admin UI routes.
- Provide a seed admin account and setup docs.

## Implementation notes
- Use `fastapi-users` or implement custom auth with `passlib` + `python-jose` for JWT.
- Store users in the DB created by issue #1.

## Labels
- enhancement, security, auth
