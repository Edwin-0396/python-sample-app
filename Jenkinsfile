pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pytest tests/'
            }
        }
        stage('Package') {
            steps {
                sh 'python3 setup.py sdist bdist_wheel'
                sh 'twine upload --repository testpypi dist/* --dry-run'
            }
        }
    }
}