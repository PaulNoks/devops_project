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
        stage('Start Services') {
            steps {
                script {
                    // Запускаем контейнеры для фронтенда и бэкенда
                    sh 'docker-compose up -d frontend backend'
                }
            }
        }
  stage('Run Tests') {
            steps {
                {
                    // Запуск тестов в контейнере
                    sh 'docker-compose run --rm test'
                }
            }
        }
      stage('Clean Up') {
            steps {
                script {
                    // После выполнения тестов удаляем контейнер для тестов
                    sh 'docker-compose down'
                }
            }
        } 
    }
}
