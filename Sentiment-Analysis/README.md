This repository includes everything needed to run a kubernetes based Sentiment-Analyzer.

First, we need to create frontend pods using:

kubectl create -f sa-frontend-deployment.yaml

Then, a service is needed to allow users access those pods via the following command:

kubectl create -f service-sa-frontend-lb.yaml
You should see:
service "sa-frontend-lb" created

After the frontend is created, we create the backend logic service and deployment.

Create Logic deployment via:

kubectl apply -f sa-logic-deployment.yaml --record

Then create logic service via:

kubectl apply -f service-sa-logic.yaml

Finally, deploy SA WebApp using:
kubectl apply -f sa-web-app-deployment.yaml --record

Service the webapp via:
kubectl apply -f service-sa-web-app-lb.yaml

voila,now you should be able to access the sentiment analyzer via the public IP address.

Use kubectl get services to find the external IP address for sa-frontend and go ahead and check it out! 
