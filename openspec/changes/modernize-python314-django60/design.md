## Context

This is a small Django project for tracking personal assets, liabilities, and
monthly financial review data. Runtime dependencies are currently pinned to
Django 4.1-era versions:

- `Django==4.1`
- `asgiref==3.5.2`
- `sqlparse==0.4.2`
- `tzdata==2022.1`

The application code is compact and mostly consists of Django models, admin
registration, a root URL include, and a simple index view. The main upgrade
work is therefore runtime and dependency modernization rather than domain
behavior redesign.

## Goals / Non-Goals

**Goals:**

- Make Python 3.14 the documented and tested runtime target.
- Upgrade to the latest compatible Django 6.0.x dependency set.
- Keep the project runnable with SQLite for local development.
- Preserve existing financial domain behavior.
- Add enough tests or smoke checks to detect upgrade regressions in models,
  admin registration, URL routing, and template rendering.
- Update setup documentation so new environments use the modernized runtime.

**Non-Goals:**

- Do not redesign the financial data model.
- Do not introduce PostgreSQL, containers, background jobs, or API frameworks.
- Do not add new user-facing financial features.
- Do not migrate away from Django's built-in test runner as part of this
  change.

## Decisions

### Target Django 6.0.x for Python 3.14 compatibility

Django 6.0 is the appropriate target because it supports Python 3.14 and keeps
the project on the current major Django line. Staying on Django 4.1 or 5.x would
reduce immediate change but preserve upgrade debt and delay compatibility work.

Alternative considered: upgrade only to a Django 5.x LTS line. That would be a
smaller jump, but it does not satisfy the goal of aligning the project with the
latest dependency baseline for Python 3.14.

### Keep dependency management simple

Continue using `requirements.txt` for runtime dependencies unless implementation
uncovers a strong reason to introduce `pyproject.toml`. The current project is
small, and a dependency management migration is not required to complete the
runtime upgrade.

Alternative considered: move immediately to `pyproject.toml` with grouped
development dependencies. That can be valuable later, but it would expand the
scope beyond the requested dependency update.

### Use focused compatibility tests

Add concise Django tests that exercise behavior most likely to be affected by a
framework upgrade:

- Model string representations and choice display behavior.
- Index URL rendering through the configured URL tree.
- Admin registrations for the property models.

Alternative considered: broad refactoring before tests. That increases risk for
little benefit because the existing code is already simple.

### Limit refactoring to upgrade hygiene

Implementation may make small style or compatibility refactors, such as using
`settings.AUTH_USER_MODEL` in abstract model mixins if needed, updating generated
comments that reference Django 4.1, and cleaning ignored Python cache files.
These refactors must not change persisted model semantics unless explicitly
required for Django 6.0 compatibility.

## Risks / Trade-offs

- Python 3.14 may not be installed in the local environment -> Document the
  required interpreter and run available checks with the installed interpreter
  if Python 3.14 is unavailable.
- Django 6.0 may surface deprecated or changed settings behavior -> Run
  `python manage.py check`, `python manage.py migrate --check` where
  appropriate, and `python manage.py test`.
- Existing migrations were generated under Django 4.1 -> Validate that the
  migration graph loads cleanly under Django 6.0 and avoid regenerating
  migrations unless model definitions actually change.
- Latest transitive dependency versions may shift over time -> Pin direct
  runtime dependencies in `requirements.txt` for reproducible local setup.

## Migration Plan

1. Update runtime dependency pins for Django 6.0.x and compatible support
   packages.
2. Update setup documentation to state Python 3.14 as the target runtime.
3. Add focused compatibility tests.
4. Run Django system checks, migrations, and tests.
5. If validation fails due to framework behavior changes, make the smallest
   compatibility refactor and rerun checks.

Rollback is straightforward: restore the previous dependency pins and
documentation if Django 6.0 compatibility cannot be completed in this change.

## Open Questions

- Should the implementation introduce `pyproject.toml` now, or keep
  `requirements.txt` as the only dependency manifest for this small project?
- Should Python 3.14 be enforced through tooling, or documented only until the
  repository has a dedicated version manager configuration?
