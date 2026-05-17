# Admin UI and dashboards

## Summary
Provide server-rendered or static admin UI for dashboards: student lists, activity management, and enrollment views.

## Why
A human-friendly admin UI makes routine management tasks faster than calling APIs manually.

## Acceptance criteria
- Add an admin dashboard with pages for students, activities, and enrollment management.
- Dashboard calls the admin CRUD APIs (issue #3).
- Include confirmations for destructive actions.

## Implementation notes
- Use the existing `src/static` folder and add `admin.js` / HTML pages.
- Keep the UI lightweight (vanilla JS or small framework like Alpine/Vue).

## Labels
- enhancement, frontend, admin
