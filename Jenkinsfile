pipeline {
    agent any

    stages {
        stage('Check env') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('install') {
            steps {
                sh '''
                    pip3 install opencv-python-headless numpy --break-system-packages
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

        stage('Run Watermark') {
            steps {
                sh 'python3 main.py'
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