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
        if (env.BRANCH_NAME == 'master')
          sh "git pull https://github.com/habiburrehman012/backend.git"
        else if (env.BRANCH_NAME == 'development')
          sh "git pull https://github.com/habiburrehman012/backend.git development"
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

    if (env.BRANCH_NAME == 'master')
    {    
      stage('Apply Deployment') 
      {
        steps
        {
          sh 'kubectl scale --replicas=0 deployment node-frontend'
          sh 'kubectl scale --replicas=1 deployment node-frontend'
        }
      }
    }
  }
}