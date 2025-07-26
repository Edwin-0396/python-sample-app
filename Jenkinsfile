pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run & Package') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'
                echo 'Packaging application...'
                sh 'python setup.py sdist bdist_wheel'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished!'
            // Optionally clean up artifacts
        }
    }
}