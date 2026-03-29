# FAQ

## What is this repository for?

This repository provides reusable GitHub Actions templates that can be adapted for different projects.

## How do I use a template?

Copy the workflow file or template you need into your repository, then update the names, paths, secrets, and triggers to match your project.

## Can I customize the templates?

Yes. The templates are designed to be adapted. You should review each file before using it so it matches your repository structure and workflow needs.

## Are these templates production-ready?

They are intended as starting points. You should test them in your environment before relying on them for important automation.

## Where should I report a bug?

Open an issue in this repository with a clear explanation of the problem, expected behavior, and any relevant logs or configuration.

## Can I request a new template?

Yes. Feature requests are welcome if the request fits the repository’s purpose and would be useful to other users.

## Do I need to credit this repository?

You may use the templates according to the repository license. Check the license file for the exact terms.

## Why did a workflow fail?

Common reasons include:
- Missing secrets.
- Incorrect file paths.
- Permission issues.
- Invalid YAML syntax.
- A trigger that does not match the event you expected.

## How can I troubleshoot quickly?

Start by:
- Checking the workflow run logs.
- Verifying secrets and permissions.
- Confirming the workflow file is in the correct location.
- Testing with a small change before expanding the workflow.