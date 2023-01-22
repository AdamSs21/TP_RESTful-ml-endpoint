pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "python3 test_main.py "
            }
        }
        stage('DockerBuild') {
            steps {
                sh "docker build -t mlops ."
            }
        }
        stage('DockerRun') {
            steps {
            }
        }
        stage('DockerPush') {
            steps{
                sh "docker tag mlops adams21/tpmlops:mlops"
                sh "docker push adams21/tpmlops:mlops"
            }
        }
    }
}