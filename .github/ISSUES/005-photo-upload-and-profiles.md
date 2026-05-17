# Add photo upload and student profile management

## Summary
Allow students to upload a profile photo and manage their profile information.

## Why
Photo uploads and profiles improve identification and the admin experience.

## Acceptance criteria
- API endpoint to upload profile photos, store files safely, and return URLs.
- Add profile fields to the user/student model (name, grade, contact email).
- Validate file types and size limits. Store files on disk or use S3-compatible storage.

## Implementation notes
- Use `python-multipart` for file uploads with FastAPI.
- Add server-side image validation and optional image resizing.

## Labels
- enhancement, frontend, backend, media
