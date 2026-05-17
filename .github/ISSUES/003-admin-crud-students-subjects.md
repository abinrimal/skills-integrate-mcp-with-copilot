# Admin CRUD: manage students and subjects

## Summary
Add admin APIs and UI to create, read, update, and delete students and activity subjects.

## Why
Admins need to manage the roster and available activities without editing code.

## Acceptance criteria
- REST endpoints for CRUD operations for students and activities.
- Pagination and search for large lists.
- Admin-only access enforced by auth (issue #2).
- Basic server-side validation and useful error messages.

## Implementation notes
- Return structured JSON for all admin endpoints.
- Consider adding simple admin pages under `/static/admin/` that call the API.

## Labels
- enhancement, backend, admin, api
