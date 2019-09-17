pipeline 
{
  environment 
  {
    registry = "habiburrehman344/backend"
    registryCredential = 'docker-credentials'
  }
  
  agent any
  // tools {nodejs "node"}

  stages 
  {
    stage('Pulling') 
    {
      steps 
      {
        sh "git pull https://github.com/habiburrehman012/backend.git development"
      }
    }



    stage('Building Application')
    {
      steps 
      {
          sh 'Built was successfull'
      }
    }

    stage('Building image') {
      steps
      {
        sh 'docker build -t habiburrehman344/backend:latest .'
      }
    }

    stage('Push image') 
    {
      steps 
      {
        script 
        {
          docker.withRegistry( '', registryCredential ) 
          {
            sh 'docker push habiburrehman344/backend:latest'
          }
        }
      }
    }
  }
}