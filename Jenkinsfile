pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "python3 test_main.py"
            }
        }
        stage('DockerBuild') {
            steps {
                sh "docker build -t restfulmlendpoint ."
            }
        }
        /*stage('DockerRun') {
            steps {
                sh "docker run mlops"
            }
        }*/
        stage('DockerPush') {
            steps{
                sh "docker tag tprestfulmlendpoint adams21/tprestfulmlendpoint:restfulmlendpoint"
                sh "docker push adams21/tprestfulmlendpoint:restfulmlendpoint"
            }
        }
        
    }
}