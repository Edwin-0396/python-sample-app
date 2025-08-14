pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Step 1: Install dependencies
                sh 'pip install -r requirements.txt'
                // Step 2: Run tests
                sh 'pytest'
            }
        }
        stage('Package and Publish') {
            steps {
                // Step 1: Build the package
                sh 'python setup.py sdist bdist_wheel'
                // Step 2: Publish to TestPyPI (securely, with Jenkins credentials)
                withCredentials([string(credentialsId: 'pypi-test-token', variable: 'PYPI_TOKEN')]) {
                    sh 'twine upload --repository testpypi -u __token__ -p $PYPI_TOKEN dist/*'
                }
            }
        }
    }
}