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
                sh 'docker build -t rest_app:latest .'
            }
        }
    }
}
