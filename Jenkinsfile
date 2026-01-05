pipeline {
    agent any
    environment {
        AWS_REGION      = 'us-east-1'
        CLUSTER_NAME    = 'my-cluster'
        DOCKER_REGISTRY = 'mydockerhub'
        IMAGE_TAG       = 'v1'
        SERVICES        = 'students courses grades teachers library attendance frontend'
    }
    stages {
        stage('Login Docker') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }
        stage('Build & Push Docker') {
            steps {
                script {
                    SERVICES.split().each { service ->
                        sh """
                        echo "Building and pushing $service..."
                        docker build -t $service:$IMAGE_TAG ./services/$service
                        docker tag $service:$IMAGE_TAG $DOCKER_REGISTRY/$service:$IMAGE_TAG
                        docker push $DOCKER_REGISTRY/$service:$IMAGE_TAG
                        """
                    }
                }
            }
        }
        stage('Configurer kubectl') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECFG')]) {
                    sh '''
                    export KUBECONFIG="$KUBECFG"
                    kubectl get ns
                    '''
                }
            }
        }
        stage('Déployer sur Kubernetes') {
            steps {
                script {
                    SERVICES.split().each { service ->
                        sh "kubectl apply -f ./k8s/deployments/${service}-deployment.yml"
                    }
                }
            }
        }
    }
    post {
        success {
            echo "Pipeline terminé avec succès ! ✅"
        }
        failure {
            echo "Erreur dans le pipeline. Vérifie les logs ! ❌"
        }
    }
}
