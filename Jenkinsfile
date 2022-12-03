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
        stage('Create docker image from Dockerfile') {
            steps {
                sh('docker build -t lombard-app:ver-${env.GIT_COMMIT} .')
            }
        }
        stage('Push my docker image to docker hub') {
            steps {
                sh """
                'docker tag lombard-app:ver-${env.GIT_COMMIT} jtwist/lombard-app:ver-${env.GIT_COMMIT}'
                'docker push jtwist/lombard-app:ver-${env.GIT_COMMIT}'
                """
            }
        }
    }
}
