# Working agreements

Read ofk/index.md and only the task-relevant guides. Keep knowledge and executable workflows separate. Source code takes precedence over draft guidance. Preserve OKF metadata and source provenance; refreshing hashes requires reviewing the associated claims. Do not label structural checks as semantic verification.

Keep changes focused, comments short, and commit messages one line. Ask before adding production dependencies. Do not push, create pull requests, or expose secrets. Keep working notes untracked in the repository root. Run relevant tests and formatting after code changes and report unavailable checks.

Use .venv/bin/python tools/validate.py to check skills, links, knowledge provenance, and element coverage. Run .venv/bin/python -m unittest discover -s tests -v and Ruff checks after tooling changes. Document coverage separately from runtime validation; profile-only elements still need targeted source inspection.
