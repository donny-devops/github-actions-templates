"""Syntax and structural validator for workflow templates (Zero-dependency)."""
import os
import sys
import re

def validate_yaml_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    assert len(content.strip()) > 0, f"{filename} is empty"
    assert re.search(r"^name:\s*.+", content, re.MULTILINE), f"{filename} missing valid 'name:' declaration"
    assert re.search(r"^on:\s*", content, re.MULTILINE), f"{filename} missing valid 'on:' declaration"
    assert re.search(r"^jobs:\s*", content, re.MULTILINE), f"{filename} missing valid 'jobs:' declaration"
    
    # Check that job keys exist under jobs:
    jobs_match = re.search(r"^jobs:\s*\n((?:[ \t]+.*\n?)+)", content, re.MULTILINE)
    assert jobs_match, f"{filename} has no job definitions under 'jobs:'"

    return True

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    templates_dir = os.path.join(root, "templates")
    readme_path = os.path.join(root, "README.md")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    count = 0
    errors = []
    
    template_files = sorted([f for f in os.listdir(templates_dir) if f.endswith(".yml") or f.endswith(".yaml")])
    
    print(f"Scanning {len(template_files)} workflow templates in {templates_dir}...\n")
    for f in template_files:
        full_path = os.path.join(templates_dir, f)
        try:
            validate_yaml_file(full_path)
            # Check README catalog coverage
            in_readme = f in readme_content
            status = "OK" if in_readme else "WARN: Not in README"
            print(f"  [PASS] {f:<38} -> Syntax OK ({status})")
            count += 1
        except Exception as e:
            print(f"  [FAIL] {f:<38} -> FAILED: {e}")
            errors.append((f, str(e)))

    print(f"\nSuccessfully validated {count}/{len(template_files)} templates.")
    if errors:
        print(f"\nErrors encountered: {len(errors)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
