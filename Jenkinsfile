node {
    def app

    stage('Build application')
    {
        sh "rm -r backend" 
        sh "git clone https://github.com/habiburrehman012/backend.git"
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
        
         withCredentials([usernamePassword( credentialsId: 'DockerHub', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
            def registry_url = "registry.hub.docker.com/"
            sh "docker login -u $USER -p $PASSWORD ${registry_url}"
            docker.withRegistry("http://${registry_url}", "DockerHub") {
                // Push your image now
                sh "docker push habiburrehman344/backend"
            }
        }
    }

    // stage('Deployment') {
    //     sh 'minikube apply -f frontend.yaml'
    //     sh 'minikube apply -f backend.yaml'
    // }
}