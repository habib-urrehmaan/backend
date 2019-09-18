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
    stage('Pulling Master branch') 
    {
      when 
      {
        branch "master"
      }
      steps 
      {
        sh "git pull https://github.com/habiburrehman012/backend.git"
      }
    }

    stage('Pulling Development branch') 
    {
      when 
      {
        branch "development"
      }
      steps 
      {
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

    stage('Apply Development') 
    {
      when 
      {
        branch "master"
      }
      steps
      {
        sh 'kubectl scale --replicas=0 deployment node-frontend'
        sh 'kubectl scale --replicas=1 deployment node-frontend'
      }
    }
  }
}