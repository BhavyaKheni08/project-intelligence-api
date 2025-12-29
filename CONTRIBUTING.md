# Contributing to Project Intelligence API

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)

### Suggesting Features

1. Check existing issues and discussions
2. Create a new issue with:
   - Clear description of the feature
   - Use case and motivation
   - Potential implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Update documentation as needed
4. **Test your changes**
   ```bash
   # Run tests (if available)
   pytest
   
   # Test the API manually
   uvicorn main:app --reload
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add: description of your changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**
   - Provide a clear description
   - Reference any related issues
   - Wait for review and feedback

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/project-intelligence-api.git
   cd project-intelligence-api
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

## Code Style

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable names

### Formatting

We recommend using `black` for code formatting:

```bash
pip install black
black .
```

## Testing

When adding new features:
- Add tests if possible
- Test manually with different inputs
- Test error cases
- Ensure backward compatibility

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update API documentation examples
- Keep EXAMPLES.md updated

## Questions?

Feel free to open an issue for questions or discussions!

