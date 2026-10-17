# Contributing

Thank you for your interest in contributing to **my-rest-api**.
Contributions may include bug fixes, new features, documentation improvements, bug reports, feature requests, and Pull Request reviews.
Before contributing, please check existing Issues and Pull Requests to avoid duplicate work.

## Development Workflow
**my-rest-api** follows a GitHub Flow-style development workflow.
The `main` branch is the primary protected branch. Changes should not be made directly in `main`.

For each change:
1. Create or select an Issue describing the requested change.
2. Create a separate branch from the current `main` branch.
3. Implement the required changes.
4. Run local checks.
5. Commit and push the changes.
6. Create a Pull Request to `main`.
7. Wait for the required GitHub Actions checks to pass.
8. Request a review from another contributor.
9. Resolve review comments if necessary.
10. Merge the Pull Request using Squash and merge.

## Branches
Use short and descriptive branch names.
Recommended formats:
- `feature/<description>`
- `fix/<description>`
- `docs/<description>`
- `issue-<number>-<description>`

One branch should normally contain one logical change.

## Development Setup
Install project dependencies with `uv sync`.
Before creating a Pull Request, make sure all local checks complete successfully.

## Issues
For non-trivial changes, create an Issue before implementation. An Issue should include a clear description of the problem, the proposed solution, and the expected result.

## Pull Requests
Pull Requests should target the `main` branch.
If the Pull Request resolves an Issue, use `Closes #<issue-number>` in the description. All required GitHub Actions checks must pass before merging.

## Code Review & Merge Strategy
Every Pull Request should be reviewed by another contributor. At least one approving review is required before merging into `main`. The project uses the **Squash and merge** strategy.

## Code of Conduct
All contributors are expected to follow the project Code of Conduct. Please communicate respectfully and provide constructive feedback.
