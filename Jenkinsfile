pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'subhaparamesh/cicd-demo'
    }

    stages {
        stage('Build and Test') {
            steps {
                sh 'python3 -m compileall -q app.py'
                sh 'python3 -m pip install --user -r requirements.txt'
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push "$DOCKER_IMAGE:$BUILD_NUMBER"
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl set image deployment/cicd-demo \
                      cicd-demo=$DOCKER_IMAGE:$BUILD_NUMBER
                    kubectl rollout status deployment/cicd-demo --timeout=120s
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get deployments'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
