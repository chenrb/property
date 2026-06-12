## ADDED Requirements

### Requirement: Python 3.14 runtime baseline

The project SHALL document Python 3.14 as the target runtime for local
development and validation.

#### Scenario: Developer reviews setup instructions

- **WHEN** a developer reads the project setup documentation
- **THEN** the documentation identifies Python 3.14 as the expected runtime

#### Scenario: Unsupported older Python is considered

- **WHEN** a developer attempts to use Python below 3.12
- **THEN** the documented dependency baseline makes clear that the runtime is
  unsupported because Django 6.0 requires Python 3.12 or newer

### Requirement: Current Django dependency baseline

The project SHALL pin direct runtime dependencies to current versions compatible
with Python 3.14 and Django 6.0.x.

#### Scenario: Dependencies are installed

- **WHEN** a developer installs dependencies from `requirements.txt`
- **THEN** Django 6.0.x and compatible direct support packages are installed

#### Scenario: Dependency file is reviewed

- **WHEN** a developer reviews `requirements.txt`
- **THEN** the pinned versions reflect the modernized Python 3.14 and Django
  6.0 baseline

### Requirement: Django application compatibility validation

The project SHALL validate that the existing Django application loads and runs
under the modernized dependency baseline.

#### Scenario: Django system check runs

- **WHEN** `python manage.py check` is run after installing the modernized
  dependencies
- **THEN** Django completes the system check without errors

#### Scenario: Database migrations are checked

- **WHEN** Django migration commands are run against the project
- **THEN** the existing migration graph loads without requiring unrelated model
  changes

#### Scenario: Test suite runs

- **WHEN** `python manage.py test` is run
- **THEN** the test suite completes successfully under the modernized dependency
  baseline

### Requirement: Existing financial behavior preservation

The project SHALL preserve existing behavior for financial domain models, admin
registration, URL routing, and the index view during the runtime upgrade.

#### Scenario: Model display behavior is tested

- **WHEN** model instances are created in tests
- **THEN** their string representations and choice display behavior remain
  consistent with the pre-upgrade behavior

#### Scenario: Admin registrations are tested

- **WHEN** the property app admin site is inspected in tests
- **THEN** the existing financial models remain registered with the Django admin

#### Scenario: Index view is requested

- **WHEN** the root URL is requested in tests
- **THEN** the index template renders successfully
