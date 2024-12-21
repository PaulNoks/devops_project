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

        stage('Run Services') {
            steps {
		dir("${WORKSPACE}"){
                sh 'docker-compose up -d'
		}
            }
        }

            }
        }
