node {
    def app

    stage('Build application')
    {
        sh "rm -r backend" 
        sh "git clone https://github.com/habiburrehman012/backend.git"
        if(env.BRANCH_NAME == 'development')
        {
            sh "git checkout development"
        }
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        dir("backend") 
        {
            sh "docker image build -t habiburrehman344/backend ."
        }
    }

    stage('Push image') {
        
         withDockerRegistry([ credentialsId: "DockerHub", url: "" ]) {
        sh "docker push habiburrehman344/backend"
        }
    }

    if(env.BRANCH_NAME == 'master'){
        stage('Merge') {
            sh 'git merge branch development'
        }

        stage('Deployment') {
            sh 'minikube apply -f frontend.yaml'
            sh 'minikube apply -f backend.yaml'
        }
    }
}