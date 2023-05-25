pipeline {
    agent any
    
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
        
        stage('Run Frontend Server') {
            steps {
                sh ' nohup python3 web_app.py &'
            }
        }
        
        stage('Run Backend Testing') {
            steps {
                sh 'python3 backend_testing.py'
            }
        }
        
        stage('Run Frontend Testing') {
            steps {
                sh 'python3 frontend_testing.py'
            }
        }
        
        stage('Run Combined Testing') {
            steps {
                sh 'python3 combined_testing.py'
            }
        }
        
        stage('Run Clean Environment') {
            steps {
                sh 'python3 clean_environment.py'
            }
        }
    }
}
