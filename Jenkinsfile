pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Build step 1: Install dependencies (simulado)"'
                sh 'echo "Build step 2: Compile (simulado)"'
            }
        }
        stage('Test & Package') {
            steps {
                sh 'echo "Test step 1: Run tests (simulado)"'
                sh 'echo "Test step 2: Package app (simulado)"'
            }
        }
    }
}