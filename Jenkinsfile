pipeline {
    agent any

    triggers {
        pollSCM('H/30 * * * *')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '20', artifactDaysToKeepStr: '5'))
    }

    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker_hub')
    }

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/EmilyDubnik/devops_course_python_project.git'
            }
        }

        stage('Install Requirenments') {
           steps {
                sh ' python3 -m pip install -r requirenments.txt '
            }
        }

        stage('Run Backend Server') {
            steps {
                sh ' nohup python3 rest_app.py &'
            }
        }

        stage('Run Backend Testing') {
            steps {
                sh 'python3 backend_testing.py'
            }
        }

        stage('Run Clean Environment') {
            steps {
                sh 'python3 clean_environment.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t emydubnik/rest_app:latest .'
            }
        }

        stage('Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_hub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                }
            }
        }
        stage('Push') {
            steps {
                sh 'docker push emydubnik/rest_app:latest'
            }
        }

        stage('Set Compose Image Version') {
            steps {
                sh 'echo "IMAGE_TAG=${BUILD_NUMBER}" > .env'
            }
        }

        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test Dockerized App') {
            steps {
                sh 'python3 docker_backend_testing.py'
            }
        }
        stage('Clean Environment') {
            steps {
                sh 'docker-compose down'
                sh 'docker rmi rest_app:latest'
            }
        }
    }
}