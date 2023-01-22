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
        /*stage('DockerRun') {
            steps {
                sh "docker run mlops"
            }
        }*/
        stage('DockerPush') {
            steps{
                sh "docker tag mlops adams21/tpmlops:mlops"
                sh "docker push adams21/tpmlops:mlops"
            }
        }
        stage('MergeToMaster') {
            steps{
                sh "git checkout master"
                sh "git branch --set-upstream-to=master"
                sh "git checkout dev"
                sh "git pull"
                sh "git checkout master"
                sh "git pull"
                sh "git merge dev"
                sh "git push origin master"
            }
        }
    }
}