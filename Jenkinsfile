pipeline {
    environment {
    registry = "habiburrehman344/backend"
    registryCredential = 'DockerHub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        sh "if [ -d backend ]; then rm -Rf $WORKING_DIR; fi"
        sh 'git clone https://github.com/habiburrehman012/backend.git'
      }
    }

    stage('Checkout') {
      when
      {
        branch 'development'
      }
      steps {
        sh 'git checkout development'
      }
    }

    stage('Building Application')
    {
        // if(env.BRANCH_NAME == 'master'){
            steps {
                echo 'Build Successfull'
            }
        // }
        // if (env.BRANCH_NAME == 'development') {
        //     steps {
        //         sh 'npm install'
        //     }
        // }
    }

    stage('Testing')
    {

        steps{
            sh "git status"
        }
    }

    stage('Building image') {
      steps{
        script {
          // dockerImage = docker.build registry + ":latest"
          sh "docker build image -t habiburrehman344/backend"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }

    // if(env.BRANCH_NAME == 'master'){
    //     stage('Update Deployment')
    //     {
    //         steps{
    //             sh 'kubectl apply -f backend'
    //         }
    //     }
    // }
}
}