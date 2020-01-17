#!/usr/bin/env groovy Jenkinsfile

pipeline() {

  agent any

  stages {
    stage('Clean') {
      when {
        branch 'master'
      }
      steps {
        script {
          dir("macos") {
            sh "make clean"
          }
        }
      }
    }
  }

    stages {
    stage('Testing') {
      when {
        branch 'master'
      }
      steps {
        script {
          dir("macos") {
            sh "make test"
          }
        }
      }
    }
  }

}
