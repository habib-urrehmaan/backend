pipeline 
{
  environment 
  {
    registry = "habiburrehman344/backend"
    registryCredential = 'DockerHub'
  }
  
  agent any
  // tools {nodejs "node"}

  stages 
  {
    stage('Pulling Code') 
    {
      steps 
      {
          sh "git pull https://github.com/habiburrehman012/backend.git"
      }
    }

    stage('Building Application')
    {
      steps 
      {
          echo 'Application was built'
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

    stage('Apply Deployment') {
      steps
      {
        sh 'kubectl scale --replicas=0 deployment python-backend'
        sh 'kubectl scale --replicas=1 deployment python-backend'
      }
    }
  }
}