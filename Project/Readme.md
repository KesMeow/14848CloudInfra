#### Please use the following Google Drive link to access Demo Video
[https://drive.google.com/drive/folders/19cEPGf_RuDa49U_8mxdpUGUMt33cck_-?usp=sharing][https://drive.google.com/drive/folders/19cEPGf_RuDa49U_8mxdpUGUMt33cck_-?usp=sharing]



#### To Deploy Hadoop on Kubernetes via yaml files

1.  Deploy both the deployment and service via: 

        kubectl apply -f hadoop-datanode-deployment.yaml
        kubectl apply -f hadoop-namenode-deployment.yaml


#### To Deploy Hadoop on Kubernetes via Container Registry

1.  First pull both container images to the cluster
        
        docker pull bde2020/hadoop-namenode
        docker pull bde2020/hadoop-datanode

2.  Tag both container images before push to the container registry
    (In my case, PROJECT-ID is final-project-14848, please use accordingly)

        docker tag bde2020/hadoop-datanode gcr.io/PROJECT-ID/datanode
        docker tag bde2020/hadoop-namenode gcr.io/PROJECT-ID/namenode

3.  Push to Google Container registry for deployment

        docker push gcr.io/PROJECT-ID/datanode
        docker push gcr.io/PROJECT-ID/namenode

4.  Go to Kubernetes Engine Page of Google Cloud and choose Workload from the left

5.  Select Deploy Icon and choose the namenode container from exisitng container images.

6.  In Environment Variables, add the following 9 variables for the namenode container.
        
        - key: CLUSTER_NAME
        value: "Test"
        - key: CORE_CONF_fs_defaultFS
        value: "hdfs://namenode:9000"
        - key: CORE_CONF_hadoop_http_staticuser_user
        value: root
        - key: CORE_CONF_hadoop_proxyuser_hue_hosts
        value: *
        - key: CORE_CONF_hadoop_proxyuser_hue_groups
        value: *
        - key: CORE_CONF_io_compression_codecs
        value: org.apache.hadoop.io.compress.SnappyCodec
        - key: HDFS_CONF_dfs_webhdfs_enabled
        value: true
        - key: HDFS_CONF_dfs_permissions_enabled
        value: false
        - key: HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check
        value: false

7.   Click continue, in the next page, change the app label name to "namenode"

8.   Pick the appropriate cluster this pod is deploying to, in my case, it is autocluster-1

9.   After deploying the namenode, go to the workload and choose namenode pod.

10.  Choose Edit and find the Replicas, change it from 3 to 1 since we only need one namenode.

11.  After changing the number of replicas, find expose button in Action.

12   Map 9870 to TargetNode 9870, 9000 to TargetNode 9000 and change service type to Loadbalancer.

13.  Click Expose to create the service. Go to Service & Ingress to record the service name. 

14.  Follow the similar step from 4 - 10 to deploy the datanode. But use the following environment variable. Use the previously recorded service name for NAMENODE-SERVICE-NAME to connect datanode to
namenode.
        
        - key: CLUSTER_NAME
            value: "Test"
        - key: SERVICE_PRECONDITION
        value: "NAMENODE-SERVICE-NAME:9000"
        - key: CORE_CONF_fs_defaultFS
        value: "hdfs://NAMENODE-SERVICE-NAME:9000"
        - key: CORE_CONF_hadoop_http_staticuser_user
        value: root
        - key: CORE_CONF_hadoop_proxyuser_hue_hosts
        value: *
        - key: CORE_CONF_hadoop_proxyuser_hue_groups
        value: *
        - key: CORE_CONF_io_compression_codecs
        value: org.apache.hadoop.io.compress.SnappyCodec
        - key: HDFS_CONF_dfs_webhdfs_enabled
        value: true
        - key: HDFS_CONF_dfs_permissions_enabled
        value: false
        - key: HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check
        value: false

15.  In workload, choose datanode and Edit the replicas to 2 since we only need 2 datanodes.
        
#### To Deploy Apache-Spark on Kubernetes

1.  Deploy both the deployment and service via: 

        kubectl apply -f apache-spark-deployment.yaml

#### To Deploy Jupyter Notebook on Kubernetes

1. Deploy both the deployment and service via: 

        kubectl apply -f jupyter-notebook-deployment.yaml

#### To Deploy SonarQube Deployment on Kubernetes

1. Deploy both the deployment and service via: 

        kubectl apply -f sonarqube-deployment.yaml

#### To Run the Terminal on Kubernetes

1. First pull the image from docker via:

        docker pull kesterzhou/project-terminal 

2. Then, use kubernetes to run the docker image via:
    
        kubectl run term --image=kesterzhou/project-terminal -it

3. Finally, open another terminal and interactive with the pod in interactive mode using:

        kubectl exec term -it python terminal.py