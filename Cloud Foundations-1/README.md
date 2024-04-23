# Cloud Computing 

It is the on-demand delivery of IT resources with pay-as-you-go pricing. 

Some of the benefits include:

- Scalability

- Elasticity

## AWS Cloud Adoption Framework (AWS CAF) 

### Transformation Value Chain

It refers to the process of identifying and optimizing key activities and processes to create and deliver value to customers, stakeholders, and the organization. 

![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/a1b4ea90-9d54-4d15-bf7f-f0333c341bb2)

A capability is a business's ability to use processes to deploy resources to achieve an outcome.

For any organization to successfully migrate its IT portfolio to the cloud, three elements must be in alignment - People, Process, and Technology. 

AWS CAF suggests 4 iterative and incremental cloud transformation phases:

- Envision Phase - demonstrates how the cloud will help accelerate your business outcomes.

- Align Phase - focuses on identifying capability gaps across the six AWS CAF perspectives, cross-functional dependencies, etc.

- Launch phase - focuses on delivering pilot initiatives in production and on demonstrating incremental business value.

- Scale phase - focuses on expanding production pilots and business value to the desired scale.

## Cloud Service Models

- Infrastructure as a Service (IaaS) provides access to networking features, computers, and storage space.

- Platform as a Service (PaaS) removes the need to manage basic underlying infrastructure, such as hardware and OS.

- Software as a Service (SaaS) gives you a ready-to-use product that is run and managed by a provider.

## Cloud Computing Deployment 

- Cloud-based Deployment - can run, migrate, or design all parts of an application in the cloud.

- Hybrid Deployment - cloud resources are connected to an on-premise infrastructure.

- On-premise deployment - also known as private cloud deployment. Resources are deployed on-premises by using virtualization and resource management tools. 


### Shared Responsibility Model 

AWS is responsible for the security of the cloud, while the customer is responsible for securing what is in the cloud. 

![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/b26296ea-a784-41d7-8680-cbb7f596d985)


## AWS Infrastructure 

### AWS Region

Each **AWS region** consists of multiple, isolated, and physically separate Availability zones within a geographic area. 

An **availability zone** is one or more separated or isolated data centres with redundant power, networking and connectivity. 

An **Edge Location** is a site that **Amazon CloudFront** uses to store cached copies of the content closer to end-users for faster delivery. 

Regions > Availability Zones 

There are atleast 3 isolated availability zones in a single region. 

Businesses deploy their content in multiple regions for the following 

- Disaster recovery and business continuity

- Low latency for end users  (Immediate response time) 

- Data Sovereignty (Follow the respective govt. data laws ex. GDPR)

### Benefits of using Edge Locations 

Security, Performance, Ease of use, Cost savings

### Amazon CloudFront 

Is a web service that speeds up the distribution of static and dynamic web content to your users. 

Benefits: Security, Hign Performance, Cost-effective, Programmable. 

Amazon CloudFront uses a global network of 450+ Points of Presence and 13 regional edge caches in 90+ cities across 48 countries. 

### AWS Globe Accelerator 

Is a networking service that helps us improve the availablity and performance of applications offered to end users. 

easy to setup, configure and manage. directs user traffic to the nearest end-point 

Benefits: 

- instant regional failover(redirects to the most available endpoint)

- High availability - gives 2 IP addresses 

- No variability around clients that cache IP addresses - updates users with new info in secs.

- Improved performance - receives traffic from the nearest regions of end users. 

- Easy managability - fixed IP addresses and single endpoint 

- Fine grained control - useful when conducting perfomance tests, allows you to direct all your tests to a single endpoint

Global Accelerator uses a global network of 104 Points of Presence in 88 cities across 48 countries. 

### Difference between AWS CloudFront and Global Accelerator 

CloudFront caches content at edge locations that are close to end-users to provide a faster experience.  

Global Accelerator doesn't cache content; instead it uses the AWS edge locations to receive end-user requests and then routes these requests to the closest AWS Region over the AWS global network.

## AWS Outposts

AWS Outposts provides local access to AWS infrastructure, so you can build and run applications at your own data centre that use the same programming interfaces as AWS regions. 


![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/f960ae9b-02c9-476d-a41b-b53112beebb7)


## AWS Local Zones 

A Local Zone is an extension of an AWS Region in a geographic proximity to the end users. Local zones are owned, managed and operated by AWS. 

For low latency issues if a regional centre is far away we establish a local zone. 


