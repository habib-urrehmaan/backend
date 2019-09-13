node {
    def app

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        sh "docker build -t habiburrehman344/backend ."
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }

    stage('Deployment') {
        sh 'minikube apply -f frontend.yaml'
        sh 'minikube apply -f backend.yaml'
    }
}