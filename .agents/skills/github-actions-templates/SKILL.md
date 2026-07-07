```markdown
# github-actions-templates Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the `github-actions-templates` repository. The codebase is written in TypeScript and provides reusable templates for GitHub Actions workflows. While no specific framework is detected, the repository follows clear coding conventions and uses conventional commit messages. You'll learn about file naming, import/export styles, and how to structure tests in this environment.

## Coding Conventions

### File Naming
- Files use **PascalCase**.
  - Example: `MyTemplate.ts`, `ActionRunner.ts`

### Import Style
- **Relative imports** are used for internal modules.
  ```typescript
  import { ActionRunner } from './ActionRunner';
  ```

### Export Style
- **Named exports** are preferred.
  ```typescript
  // In ActionRunner.ts
  export function runAction() { ... }
  ```

### Commit Messages
- **Conventional commit** style is used.
- Prefixes like `docs` indicate documentation changes.
  - Example: `docs: update README with usage examples`

## Workflows

*No automated workflows detected in the repository.*

## Testing Patterns

- Test files follow the pattern: `*.test.*`
  - Example: `ActionRunner.test.ts`
- The specific testing framework is **unknown**, but tests are colocated with source files or in the same directory.

  ```typescript
  // ActionRunner.test.ts
  import { runAction } from './ActionRunner';

  describe('runAction', () => {
    it('should execute successfully', () => {
      expect(runAction()).toBe(true);
    });
  });
  ```

## Commands
| Command | Purpose |
|---------|---------|
| /conventions | Show coding conventions and examples |
| /test-patterns | Show how to write and organize tests |
| /commit-style | Show commit message guidelines |
```
