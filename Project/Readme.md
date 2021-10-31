#### To Run the Terminal on Kubernetes

1. First pull the image from docker via:

        docker pull kesterzhou/project-terminal 

2. Then, use kubernetes to run the docker image via:
    
        kubectl run term --image=kesterzhou/project-terminal -it

3. Finally, interactive with the pod in interactive mode using:

        kubectl exec term -it python terminal.py

#### To Deploy Hadoop on Kubernetes

1. First deploy both namenode and datanode via:

        kubectl apply -f hadoop-datanode-deployment.yaml
        kubectl apply -f hadoop-namenode-deployment.yaml

2. Then create services for corresponding deployment using:

        kubectl apply -f service-hadoop-datanode.yaml
        kubectl apply -f service-hadoop-namenode.yaml

#### To Deploy Apache-Spark on Kubernetes

1. First deploy the apache-spark-deployment via:

        kubectl apply -f apache-spark-deployment.yaml

2. Then create service for corresponding deployment using:

        kubectl apply -f service-apache-spark.yaml


#### To Deploy Jupyter Notebook on Kubernetes

1. Deploy both the deployment and service via: 

        kubectl apply -f jupyter-notebook-deployment.yaml

#### To Deploy SonarQube Deployment on Kubernetes

1. Deploy both the deployment and service via: 

        kubectl apply -f sonarqube-deployment.yaml

