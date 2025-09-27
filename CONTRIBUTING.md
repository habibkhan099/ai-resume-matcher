# Contributing to AI Resume Matcher

Thank you for your interest in contributing to the AI Resume Matcher project! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information** including:
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Screenshots if applicable
   - System information (OS, Python version, etc.)

### Making Changes

1. **Fork the repository**
2. **Create a feature branch** from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the coding standards
4. **Test your changes** thoroughly
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 📝 Coding Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Maximum line length: 88 characters
- Use type hints where appropriate

### Frontend Code Style

- Use consistent indentation (2 spaces for HTML/CSS/JS)
- Follow semantic HTML practices
- Use Bootstrap classes consistently
- Comment complex JavaScript functions

### Commit Message Format

```
Type: Brief description

Optional longer description

Fixes #issue-number
```

**Types:**
- `Add:` New features
- `Fix:` Bug fixes
- `Update:` Updates to existing features
- `Remove:` Removing code/features
- `Doc:` Documentation changes
- `Style:` Code formatting changes
- `Refactor:` Code refactoring
- `Test:` Adding or updating tests

## 🧪 Testing

Before submitting a PR, please ensure:

1. **Manual Testing**
   - Test with different file formats (PDF, DOCX, TXT)
   - Test with various job descriptions and resumes
   - Test edge cases (empty files, large files, special characters)
   - Test on different browsers and screen sizes

2. **Code Quality**
   - Run linting tools
   - Check for Python syntax errors
   - Validate HTML/CSS

## 💡 Feature Ideas

We welcome contributions in these areas:

### High Priority
- [ ] Add support for more file formats (RTF, ODT)
- [ ] Implement advanced NLP models (spaCy, BERT)
- [ ] Add user authentication system
- [ ] Create REST API endpoints
- [ ] Improve mobile responsiveness

### Medium Priority
- [ ] Add resume parsing for structured data
- [ ] Implement caching for better performance
- [ ] Add internationalization (i18n)
- [ ] Create admin dashboard
- [ ] Add email notifications

### Low Priority
- [ ] Dark mode theme
- [ ] Advanced filtering options
- [ ] Export results to PDF/Excel
- [ ] Integration with job boards
- [ ] Batch processing capabilities

## 🐛 Bug Report Template

When reporting bugs, please include:

```
**Bug Description**
A clear description of what the bug is.

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**
- OS: [e.g. Windows 10, macOS Big Sur]
- Browser: [e.g. Chrome 96, Firefox 95]
- Python Version: [e.g. 3.9.7]
- Flask Version: [e.g. 2.0.2]

**Additional Context**
Any other context about the problem.
```

## 📋 Pull Request Template

```
## Description
Brief description of the changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] I have tested these changes locally
- [ ] I have added tests for new functionality
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots of UI changes.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code where necessary
- [ ] My changes generate no new warnings
- [ ] I have updated the documentation accordingly
```

## 🏆 Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Project documentation

## 📞 Getting Help

If you need help with contributing:

1. **Check the documentation** in the README
2. **Search existing issues** for similar questions
3. **Create a new issue** with the "question" label
4. **Contact the maintainer** directly

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for helping make AI Resume Matcher better! 🚀