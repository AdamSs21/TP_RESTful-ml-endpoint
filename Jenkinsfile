pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "pip3 install --upgrade pip"
                sh "pip3 install --upgrade wheel"
                sh "pip3 install --upgrade setuptools"
                sh "pip3 install -r requirements.txt"
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