pipeline {
    agent any

    environment {
        IMAGE_NAME = 'watermark-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Check env') {
            steps {
                sh '''
                    python3 --version
                    docker --version
                    kubectl version --client
                '''
            }
        }

        stage('install') {
            steps {
                sh '''
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python3 get-pip.py --break-system-packages
                    /var/jenkins_home/.local/bin/pip3 install opencv-python-headless numpy --break-system-packages
                '''
            }
        }

        stage('Check Images') {
            steps {
                sh '''
                    if [ ! -f "image/main_img.jpg" ]; then
                        echo "main_img not exist"
                        exit 1
                    fi
                    if [ ! -f "image/hidden_img.jpg" ]; then
                        echo "hidden_img not exist"
                        exit 1
                    fi
                    echo "img exist"
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 test_main.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t deweihou/${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag deweihou/${IMAGE_NAME}:${IMAGE_TAG} \
                               deweihou/${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-token',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                        docker push deweihou/${IMAGE_NAME}:${IMAGE_TAG}
                        docker push deweihou/${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                sh '''
                    kubectl delete job watermark-job --ignore-not-found
                    kubectl apply -f deployment.yaml
                    kubectl wait --for=condition=complete job/watermark-job --timeout=60s
                '''
            }
        }
    }

    post {
        success {
            echo 'Watermark Pipeline SUCCESS'
        }
        failure {
            echo 'Watermark Pipeline FAILED'
        }
    }
}