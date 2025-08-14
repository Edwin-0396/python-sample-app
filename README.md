# python-sample-app

A starter template for new Python applications.

## Features

- Minimal but functional Python project structure
- Example console script with entry point
- Ready for PyPI, Jenkins, flake8, and pytest
- MIT licensed

## Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/Edwin-0396/python-sample-app.git
cd python-sample-app
```

(Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project in editable mode and its dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

### Usage

Run the sample app from the command line:

```bash
sample-app
```

Or run directly from Python:

```bash
python -m python_sample_app.main
```

## Testing

Run tests using pytest:

```bash
pytest
```

## Code Style

Lint your code using flake8:

```bash
flake8
```

## Packaging

To build a wheel and source distribution:

```bash
python setup.py sdist bdist_wheel
```

## License

MIT License. See [LICENSE.md](LICENSE.md) for details.
