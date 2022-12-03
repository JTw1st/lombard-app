pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        HEROKU_API_KEY = credentials('HEROKU_API_KEY')
        HEROKU_APP_NAME = credentials('HEROKU_APP_NAME')
        HEROKU_EMAIL = credentials('HEROKU_EMAIL')
    }
    stages {
        stage('Checkout source code') {
            steps {
                checkout scm
            }
        }
        stage('Run unittest') {
            steps {
                sh('python3 -m unittest tests.py')
            }
        }
        stage('Login to docker hub') {
            steps {
                sh('docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD')
            }
        }
    }
}
