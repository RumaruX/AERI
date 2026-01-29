# Contributing to AERI

Thank you for your interest in contributing to AERI! This document provides guidelines and instructions for contributing to this developmental AI project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Teaching AERI](#teaching-aeri)
- [Research Contributions](#research-contributions)
- [Questions and Help](#questions-and-help)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please read our [Code of Conduct](docs/spec/ethics.md) before contributing.

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- Basic understanding of developmental AI concepts

### Setting Up Development Environment

1. **Fork and Clone**
```
git clone https://github.com/YOUR_USERNAME/aeri.git
cd aeri
```

2. **Create Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

3. **Install Dependencies**
```
pip install -e ".[dev]"
```

4. **Set Up Pre-commit Hooks**
```
pre-commit install
```

### Understanding the Project Structure
Familiarize yourself with the [project architecture](docs/spec/architecture.md) before contributing.

## Development Workflow

### 1. Find an Issue
- Check [GitHub Issues](https://github.com/RumaruX/AERI/issues)
- Look for issues tagged `good-first-issue` or `help-wanted`
- Discuss your approach in the issue comments before starting

### 2. Create a Branch
```
git checkout -b type/description
```
Branch naming conventions:
- `feature/` - New features or enhancements
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `experiment/` - Research experiments
- `refactor/` - Code refactoring
- `test/` - Test additions or improvements

Examples:
- `feature/memory-optimization`
- `bugfix/segmentation-error`
- `docs/teaching-guide-update`

### 3. Make Changes
Follow the [Code Standards](#code-standards) below.

### 4. Test Your Changes
```
# Run all tests
make test

# Run specific test
pytest tests/unit/test_your_feature.py -v

# Run with coverage
make test-cov
```

### 5. Run Code Quality Checks
```
make check  # Runs lint, format-check, and type-check
```

### 6. Commit Changes
Use [Conventional Commits](https://www.conventionalcommits.org/):
```
git commit -m "feat: add episodic memory recall"
git commit -m "fix: correct grammar induction algorithm"
git commit -m "docs: update teaching protocol"
```

Commit types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `refactor`: Code restructuring
- `style`: Formatting
- `perf`: Performance improvements
- `chore`: Maintenance

### 7. Push and Create Pull Request
```
git push origin your-branch-name
```
Then create a Pull Request on GitHub.

## Code Standards

### Python Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all function signatures
- Write docstrings for all public functions/classes
- Maximum line length: 88 characters

### File Organization
- One class per file (unless closely related)
- Group related functions together
- Keep files focused and under 300 lines

### Naming Conventions
- **Classes**: `PascalCase`
- **Functions/Methods**: `snake_case`
- **Variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

### Imports Order
1. Standard library imports
2. Third-party imports
3. Local application imports

Each group separated by a blank line, sorted alphabetically.

## Testing

### Writing Tests
- Tests go in `tests/` mirroring `src/` structure
- Use descriptive test names: `test_function_does_something_when_condition`
- One assertion per test (when possible)
- Use fixtures for shared setup

### Test Coverage
- Aim for 80%+ coverage for new code
- Test edge cases and error conditions
- Include integration tests for critical paths

### Running Tests
```
# All tests
make test

# Specific module
pytest tests/unit/test_memory.py

# With coverage report
make test-cov
```

## Documentation

### Code Documentation
- All public functions/classes need docstrings
- Use Google-style docstrings
- Include type hints in docstrings
- Document parameters, returns, and exceptions

### Example Docstring
```python
def learn_word(word: str, context: List[str]) -> bool:
    """
    Learn a new word from contextual usage.
    
    Args:
        word: The word to learn
        context: List of surrounding words providing context
        
    Returns:
        bool: True if word was successfully learned
        
    Raises:
        ValueError: If word is empty or context is invalid
    """
```

### Project Documentation
- Update `docs/` when changing functionality
- Keep examples in `docs/tutorials/` up to date
- Update README.md for significant changes

## Pull Request Process

### Before Submitting
1. Ensure all tests pass
2. Run code quality checks: `make check`
3. Update documentation if needed
4. Add or update tests for new functionality
5. Rebase on latest main branch

### PR Description Template
```markdown
## Description
Brief description of changes

## Related Issues
Fixes #123, Related to #456

## Changes Made
- List specific changes
- Explain design decisions

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing performed

## Documentation
- [ ] Docstrings added/updated
- [ ] README updated if needed
- [ ] Tutorials updated if needed

## Checklist
- [ ] Code follows style guidelines
- [ ] Type hints added
- [ ] No breaking changes (or documented)
- [ ] Self-reviewed code
```

### Review Process
1. At least one maintainer must approve
2. Address all review comments
3. All checks must pass
4. Keep PR focused (one feature/fix per PR)

## Teaching AERI

### Becoming a Teacher
1. Read the [Teaching Protocol](docs/tutorials/teaching_protocol.md)
2. Understand AERI's current developmental stage
3. Use consistent teaching methods

### Recording Sessions
- Save session logs in `data/raw/interactions/`
- Use descriptive filenames: `YYYY-MM-DD_stageX_teacherY.json`
- Include metadata about teaching approach

### Sharing Insights
- Document interesting learning moments
- Share effective teaching strategies
- Report issues with learning patterns

## Research Contributions

### Experimental Code
- Place in `experiments/` directory
- Use Jupyter notebooks for exploration
- Document protocols in `experiments/protocols/`

### Publishing Results
- Share findings in project discussions
- Contribute to documentation
- Consider academic publication

### Data Sharing
- Anonymize interaction data
- Respect participant privacy
- Follow ethical guidelines

## Questions and Help

### Getting Help
- Check existing documentation
- Search GitHub issues and discussions
- Ask in GitHub Discussions

### Reporting Bugs
1. Use the bug report template
2. Include AERI version and stage
3. Provide reproduction steps
4. Attach relevant logs

### Feature Requests
1. Explain the use case
2. Describe expected behavior
3. Discuss potential implementation

## Recognition

Contributors are acknowledged in:
- Release notes
- Contributor list
- Project documentation

Thank you for contributing to AERI's development!