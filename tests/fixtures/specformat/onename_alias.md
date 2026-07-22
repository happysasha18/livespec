# One-name fixture: one thing referenced under two names

This is a preamble. Bracket codes like `INV-1` trail each criterion.

## Glossary

- **widget** — one unit the product shows.
- **backlog item** — one row that tracks a single request.

## Requirement 1: A widget shows and its work is tracked

**Context:** The product shows widgets. Each request to change one opens a backlog item. The work is tracked to close.

**User Story:** As a person, I want each change tracked, so that none is lost.

### Acceptance Criteria

**Case: the work is tracked**

1. *when* a person asks for a change, the system *shall* open a ticket for it. [INV-1]
