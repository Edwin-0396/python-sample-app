pipeline {
    agent {
        docker { image 'python:3.11' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/'
            }
        }
        stage('Package') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
                sh 'twine upload --repository testpypi dist/* --dry-run'
            }
        }
    }
}