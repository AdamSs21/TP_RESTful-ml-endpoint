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
        stage('PushToMaster') {
            steps{
                sh "git checkout master"
                sh "git pull origin master"
                sh "git push origin master"
            }
        }
    }
}