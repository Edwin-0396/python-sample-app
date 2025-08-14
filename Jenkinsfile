pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                // Step 1: Set up Python virtual environment and install dependencies
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                // Step 2: Run tests
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest
                '''
                // Step 3: Lint code (good practice for build stage)
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install flake8
                    flake8 .
                '''
            }
        }
        stage('Package and Publish') {
            steps {
                // Step 1: Build the package
                sh '''
                    . $VENV_DIR/bin/activate
                    python setup.py sdist bdist_wheel
                '''
                // Step 2: Check the package with twine
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install twine
                    twine check dist/*
                '''
                // Step 3: Publish to TestPyPI (securely with Jenkins credentials)
                withCredentials([string(credentialsId: 'pypi-test-token', variable: 'PYPI_TOKEN')]) {
                    sh '''
                        . $VENV_DIR/bin/activate
                        twine upload --repository testpypi -u __token__ -p $PYPI_TOKEN dist/*
                    '''
                }
                // Step 4: Archive built distributions as Jenkins artifacts
                archiveArtifacts artifacts: 'dist/*'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
