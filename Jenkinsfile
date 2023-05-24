pipeline {
    agent any
    
    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/EmilyDubnik/devops_course_python_project.git'
            }
        }
        
        stage('Run requirements') {
            steps {
                sh ' python3 -m pip install -r requirements.txt '
            }
        }       
        
        stage('Run backend server') {
            steps {
                sh ' nohup python3 rest_app.py &'
            }
        }
        
        stage('Run frontend server') {
            steps {
                sh ' nohup python3 web_app.py &'
            }
        }
        
        stage('Run backend Testing') {
            steps {
                sh 'python3 backend_testing.py'
            }
        }
        
        stage('Run frontend testing') {
            steps {
                sh 'python3 frontend_testing.py'
            }
        }
        
        stage('Run combined testing') {
            steps {
                sh 'python3 combined_testing.py'
            }
        }
        
        stage('Run clean environment') {
            steps {
                sh 'python3 clean_environment.py'
            }
        }
    }
}
