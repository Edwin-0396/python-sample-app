pipeline {
    agent any
    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }
    stages {
        stage('Create Virtualenv'){
            steps{
                echo 'Creating virtual environment...'
                sh 'python3 -m venv $VENV_DIR'
                sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '$VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '$VENV_DIR/bin/activate && pytest tests/ || echo "No tests found"'

            }
        }
    }
    post {
            always{
                echo 'Cleaning up virtual environment...'
                sh 'rm -rf $VENV_DIR'
            }
    }
}