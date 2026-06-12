## Why

The project is still pinned to Django 4.1-era dependencies and currently runs
against an older Python baseline. Moving to Python 3.14 and current Django
dependencies reduces upgrade drift and gives the project a supported runtime
foundation before further financial tracking features are added.

## What Changes

- Update the supported runtime baseline to Python 3.14.
- Upgrade Django from 4.1 to the latest compatible Django 6.0.x release.
- Refresh direct runtime dependencies to current compatible versions.
- Add or update project metadata and documentation so setup, migration, and
  test commands reflect the new runtime baseline.
- Add focused compatibility tests or smoke checks around models, admin-facing
  registrations, URL routing, and template rendering.
- Perform small project hygiene refactors that reduce upgrade friction without
  changing financial domain behavior.
- **BREAKING**: Python versions below 3.12 will no longer be supported because
  Django 6.0 requires Python 3.12 or newer.

## Capabilities

### New Capabilities

- `runtime-modernization`: Defines the supported Python/Django runtime,
  dependency baseline, setup documentation, and compatibility validation for
  the project.

### Modified Capabilities

- None.

## Impact

- Affected files are expected to include `requirements.txt`, environment or
  setup documentation such as `README.md` and `ENV.md`, Django settings or URL
  configuration if required by Django 6.0 checks, and tests under `apps/`.
- The SQLite database remains the local development database; no data model or
  migration change is intended unless Django 6.0 compatibility requires it.
- Existing financial domain behavior for assets, liabilities, targets, and the
  index view should remain unchanged.
