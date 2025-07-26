pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                echo 'Creating virtual environment...'
                sh 'python3 -m venv venv'
            }
        }
        stage('Test & Package') {
            steps {
                echo 'Installing dependencies and running tests...'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                sh '. venv/bin/activate && pytest tests/'
                echo 'Packaging application...'
                sh '. venv/bin/activate && python setup.py sdist bdist_wheel'
            }
        }
    }
}