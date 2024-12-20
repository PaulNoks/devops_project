pipeline {
    agent any

stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PaulNoks/devops_project'
            }
        }

        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t backend:latest .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t frontend:latest .'
                }
            }
        }
  stage('Run Tests') {
            steps {
                dir('backend') {
                    // Запуск тестов в контейнере
                    sh 'docker run --rm backend:latest'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
