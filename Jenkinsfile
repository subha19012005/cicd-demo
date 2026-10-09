pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building application'
                sh 'python3 -m compileall -q app.py'
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install pytest'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh 'mkdir -p deployed'
                sh 'cp app.py deployed/app.py'
                echo 'Deployment successful'
            }
        }
    }
}