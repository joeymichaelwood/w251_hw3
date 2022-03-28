# w251_hw3

Face location:
https://berkeley-251.s3.amazonaws.com/ffd194c9-d767-43c8-b2f6-bf27177aa0a9.png

10 points for explaining the MQTT topics and the QoS that you used.

MQTT is a messaging protocol that works extremely well in the age of IoT because it can scale to any number of devices connected to it. That's because it is extremely lightweight and flexible. Publishers publish or send data to a topic which brokers read in order to send to subscribers. A subscriber listens for certain topics, and all other messages and other topics are completely ignored. This allows for any number of topics and messages to flow through the architecture without overwhelming small clients, as those clients only need to handle their messages. New clients can join and new topics can be written and subscribed to without it affecting any existing clients.

For this homework, I used QoS Zero. Given that this was a learning experience and not a system built to support enterprise software, it seemed reasonable to support just QoS Zero. This means that the there is no guarantee of message delivery, it's just a best effort scenario. It works much like TCP protocol in that it's a fire and forget strategy. This strategy would not work for larger applications that care about ensuring each message arrives, especially ones with real customers as users as they aren't as patient with lost information. 


### Docker and Kube Commands
To run this application, I utilized the kube and docker command line. For the edge device I applied each of their configs like so:
kubectl apply -f kubernetesDeployment.yaml
kubectl apply -f mosquittoService.yaml
kubectl apply -f subWorkflowDeployments.yaml

To build the docker containers I utilized the commands provided in the Lab:
docker build -t <image-name> .
For this face detector this would look like:
docker build -t joeyw526/face-detector:v1 .

This was done for each of the components
