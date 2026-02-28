# Future Ideas & Improvements

## Technical Debt

### Build System - License Format Update (setuptools)
**Priority:** Low  
**Timeline:** Before 2027-02-18 (setuptools deadline)  
**Issue:** `pyproject.toml` uses deprecated `project.license` as a TOML table  
**Current:** v0.1.0 build produces deprecation warnings from setuptools 82.0.0+  
**Action Required:**
- Update `project.license` from table format to simple SPDX string
- Remove `project.license-files` if present
- Remove deprecated license classifiers (`License :: OSI Approved :: MIT License`)
- See: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license

**Example Fix:**
```toml
# Current (deprecated)
[project.license]
text = "MIT"

# New (recommended)
license = "MIT"
```

---

## Feature Ideas

### Phase 5+: Method Name Translation
- Translate object methods to Portuguese (e.g., `.append()` → `.acrescentar()`)
- Requires significant refactoring of translator
- Deferred from MVP

### Phase 5+: IDE Support
- Visual Studio Code extension for syntax highlighting
- IntelliSense/autocomplete for Portuguese keywords
- Linting rules for python-pt-br

### Phase 5+: CI/CD Integration
- GitHub Actions for automated testing
- Automated PyPI releases
- Version bump automation

### Phase 6+: Internationalization
- Support other languages beyond Portuguese
- Generic translator framework
- Language pack system

---

## Known Limitations (MVP)

- **Method Names:** Object methods remain in English (e.g., `.append()` not `.acrescentar()`)
- **IDE Support:** No built-in IDE integration yet
- **Performance:** Translation occurs at import time (negligible overhead, but present)
- **Debugging:** Stack traces show translated code, not original

