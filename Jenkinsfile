pipeline {
  
  agent any
  stages {
    def app
    stage('Cloning Git') {
      steps {
        sh "if [ -d backend ]; then rm -Rf backend; fi"
        // sh 'git clone https://github.com/habiburrehman012/backend.git'
        checkout scm
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
          app = docker.build("habiburrehman344/backend")
        }
      }
    }

    stage('Push image') {
      steps {
        docker.withRegistry('https://registry.hub.docker.com', 'DockerHub') {
            app.push("latest")
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