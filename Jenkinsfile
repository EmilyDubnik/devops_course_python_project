pipeline {
    agent any

    triggers {
        pollSCM('H/30 * * * *')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '20', artifactDaysToKeepStr: '5'))
    }

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/EmilyDubnik/devops_course_python_project.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Backend Server') {
            steps {
                sh 'nohup python3 rest_app.py &'
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

        stage('Push Docker Image') {
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