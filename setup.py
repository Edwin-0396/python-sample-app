from setuptools import setup

# Used in pypi.org as the README description of your package
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='python-sample-app',
    version='1.0',
    description=(
        "python-sample-app is a starter temp/"
        "late for new python applications"
    ),
    author='Benjamin Costa',
    author_email='benjamin.costa.75@gmail.com',
    license="MIT",
    url="https://github.com/becosta/python-sample-app",
    packages=['python_sample_app'],
    entry_points={
        'console_scripts': [
            'sample-app=python_sample_app.main:main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown"
)
