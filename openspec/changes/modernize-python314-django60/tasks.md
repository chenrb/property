## 1. Baseline Assessment

- [x] 1.1 Confirm the local interpreter availability and record whether Python
  3.14 is installed for validation.
- [x] 1.2 Run the current Django test suite or available smoke checks before
  dependency changes to establish a baseline.
- [x] 1.3 Inspect Django settings, URL configuration, migrations, and app
  registrations for Django 6.0 compatibility concerns.

## 2. Dependency and Runtime Update

- [x] 2.1 Update `requirements.txt` to pin Django 6.0.x and compatible direct
  support dependencies for Python 3.14.
- [x] 2.2 Update setup documentation to state Python 3.14 as the target runtime
  and describe the dependency installation flow.
- [x] 2.3 Update Django-version-specific comments or generated documentation
  references that still point at Django 4.1.

## 3. Compatibility Tests and Hygiene

- [x] 3.1 Add focused model tests for string representations and choice display
  behavior that should remain unchanged.
- [x] 3.2 Add a view or URL test that verifies the root index page renders
  successfully.
- [x] 3.3 Add an admin registration smoke test for the existing property models.
- [x] 3.4 Make only minimal compatibility or hygiene refactors required by
  Django 6.0 checks.

## 4. Validation

- [x] 4.1 Run `python manage.py check` with the updated dependencies.
- [x] 4.2 Run migration validation to confirm the existing migration graph loads
  under Django 6.0.
- [x] 4.3 Run `python manage.py test` and resolve any upgrade regressions.
- [x] 4.4 Review changed files to confirm no financial domain behavior or schema
  changes were introduced unintentionally.
