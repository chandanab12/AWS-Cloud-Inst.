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


## Core AWS Services 

## Compute 

Compute describes concepts and objects related to s/w computation. Used to refer processing power, memory, networking, storage and other resources. 

### Amazon EC2 ( Elastic Compute Cloud) 

It is a virtual cloud computing environment. 

Can launch instances with a variety of OS, custom application environments, n/w access permissions and run images

### Amazon ECS (Elastic Container Service)

Fully managed container orchestration service that enables customers to deploy, manage and scale containerized applications 

Containerized - a program/application that runs in its own environment. Has a designated OS that runs specifically for the program. 

### Amazon Lightsail 

Easy to use virtual private server(VPS instances), containers, storage, dbs, and more at a cost-effective price. 

Generally used for launching simple web applications, creating custom websites, and building small business applications. 

### AWS Lambda 

Enables to run code without provisioning or managing servers. They pay only for the compute time used. Just need to upload the code. 

## Storage 

### Amazon S3 (Simple Storage Service) 

It is an object storage service that offers scalability, data availability, security, and performance. It is designed for 99.9999999% durability. 

### Amazon S3 Glacier 

Built for data archiving, high performance, retrieval flexibility , and lowest cost archive storage. provides unlimited virtual scalability and data durability. 

### Amazon EBS (Elastic Block Storage) 

It is an easy to use scalable, high perf block storage service designed for Amazon EC2. Used for things lke big-data analytic engines and dbs. 

# Q 

What is the diff btw object storage and block storage. How would you know what service to use. 

### Amazon EFS ( Amazon Elastic File System) 

Automatically grows and shrinks as customers add and remove files. Does not require management or provisioning. 

## Networking 

A CDN(Content Delivery Network) is a geographically distributed group of servers that work together to provide fast delivery of internet content. 

### Amazon VPC (Virtual Private Cloud) 

Gives customers full control over a virtual networking environment, including resource placement, connectivity and security. 

After setting up a VPC, resources such as EC@ instances are connected to it and communication is setup across accounts, availability zones and regions. 

### Amazon CloudFront 

It is a fast CDN that securely delivers data, videos , applications and API's to customers globally with low latency in a developer friendly environment. 

Works with Amazon Shield Standard for DDos mitigation. 

### ELB ( ELastic Load Balancing) 

It works as a traffic director. Automatically distributes application traffic across  multiple targets and virtual appliances in one or more availability zones. 

## Database 

A DB is an electronically stores, systematic collection of data. Can contain any type of data, including words, numbers, images, etc. 

### Amazon RDS ( Relational Database Service) 

Is a collection of managed services that make it simple to set up , operate, and scale dbs in the cloud. 

Can be setup using the following engines: Amazon Aurora with MySQL Compatibility, Amazon Aurora with PostGreSQL Compatiblity, MySQL, MariaDB, PostgreSQl, Oracle, SQL Server. 

### Amazon Dynamo DB 

It is a NoSQL DB that supports key-value and document data models. 

DynamoDB delivers single-digit millisecond performance at any scale. Can support 10-trillion requests per day and peaks of more than 20 million requests per second. 

It is a fully managed, multi region, multi master, durable db with built in security, backup and restore, and in memory caching. 

## Management and Governance 

### AWS CloudTrail 

It is a service that enables governance, compliance , operational auditing, and risk auditiong for AWS account.

It logs, continuously monitors and retains acc related activity across AWS infrastructure. Provides event history that simplifies security analysis, resource change tracking and troubleshooting. 

### Amazon CloudWatch 

Collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance. 

### AWS Config 

Continually assessess, audits, and evaluates to the config and relationships of AWS resources. 

### AWS Audit Manager 

Helps custormers map their compliance req to AWS usage data with pre built and custom frameworks and automated evidence collection 

# Q.

AWS config and cloud watch kinda same. What to use when 

## AI and ML 

ML is the science of developing algorithms and statistical models that computer systems use to perform tasks without explicit instructions, relying on patterns and inference. 

### Amazon Sagemaker 

Provides the ability to build, train, and deploy ML models. 

It covers the entire ML workflow to label and prepare data, choose an algo, train the model, tune and optimize it for deployment, make predictions, and take actions. 

### Amazon Comprehend 

Is an NLP service that uses ML to uncover valuable insight and connections in text. 

### Amazon Translate 

Is a text-translation service that uses adv. ML to provide high-quality translation. 

## Data Analytics

### Amazon Quicksight 

Is a cloud-scale BI service that is used to deliver easy-to-understand insights. 

### Amazon Redshift 

is a fully managed, petabyte-scale data warehouse service in the cloud. It helps companies run complex analytics queries against petabytes of structured data. 

Amazon Redshift uses SQL with hardware and ML to analyze structured and semi-structured data across warehouses, operational Dbs, and data lakes. 

### Amazon EMR (Elastic Map Reduce) 

Is a managed cluster platform that simplifies running big data frameworks on AWS to process and analyze vast amounts of data. 

## Application Integration 

App integration on AWS is a suite of services that enable communication between decoupled components within microservices, Distributed systems, and serverless applications. 

- Decouple - Systems are decoupled when they are able to execute actions independent of each other( without using another system's resources) but are still able to communicate with each other.

- Serverless architecture - is a way to build and run applications and services without having to manage infrastructure.

### Amazon SQS (Simple Queue Service) 

It offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems. 

### Amazon SNS (Simple Notification Service)

Is a web service that co-ordinates and manages the delivery or sending of messages to subscribing endpoints or clients. 

There are 2 types of clients - publishers and subscribers also referred to as producers and consumers. 

### Amazon EventBridge 

It is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. 

## Business Applications

They are meant to increase business agility, improve employee collaboration, and customer experience. 

### Amazon Connect 

Is an omnichannel cloud contact centre that helps companies provide better customer service at a lower cost. 

You can setup a contact centre in a few steps, add agents located anywhere and start engaging with customers. 

### Amazon SES (Simple Email Service)

Is a cloud email service provider that can integrate into any application for bulk email sending. 

Also supports variety of deployments including dedicated, shared or owned IP addresses. Reports on sender stats and deliverability dashboards. 

## End-user computing services

provides secure access to the applications and desktops the workforce needs to get their job done. 

### Amazon AppStream 

Is a fully managed non persistent desktop and application service for remotely accessing work on any computer

### Amazon Workspaces 

Fully managed, secure desktop computing service that runs on AWS cloud. 

### Amazon Workspaces Web

Is an on demand fully managed, Linux based service designed to facilitate secure browser access to internal website and Saas applications. 

## Developer Tools 

### AWs AppConfig 

A capability of AWS Systems Manager, helps developers manage, store and safely deploy application configurations to hosts at runtime. 

### AWS Cloud9 

Is a cloud based IDE that lets developers write, run and debug code with just a browser. 

### AWS CloudShell 

Is a browser based shell, which lets developers quickly run scripts with AWS CLI, experiment with service API's using the AWS CLI and other tools to increase productivity. 

### AWS CodeArtifact

Is a managed artifact repo that lets developers securely store, publish and share s/w packages. 

### AWS CodeBuild 

Is a fully managed, continous integration servce that compiles source code, runs tests and 
produces ready to deploy s/w packages

### AWS Codecommit 

Is a secure, highly scalable, and fully managed source control service that hosts private Git repos. 

### AWS Codedeploy 

Is a fully managed deployment service that automates s/w deployments to various compute services such as Amazon EC2, ECS, Lambda and on premise servers. 

### AWS Codepipeline

Fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.

### AWS Codestar 

Enables developers to quickly develop, deploy, build and deploy applications on AWS. Provides unified user interface, and enables s/w development activities management in one place. 

Entire CD Toolchain can be set up in AWS codestar

Allows teams to release code faster. 

- CodeStar Project

Comes with project management dashboard, including an integrated issue tracking capability. 

### AWS X-Ray

Provides a complete view of requests as they travel through an application and filters visual data across payloads, functions, traces, with low code and low code motions. 

## Front End web and mobile 

AWS offers tools and services giving developers the ability to develop, deploy and operate applications all within a web browser. 

### AWS Amplify

Consists of a set of tools and services to let front-end web and mobile developers build, ship, and host full stack applications on AWS, with the flexibility to leverage the breadth of AWS services as use cases evolve. 

No prior cloud expertise is needed. 

### AWS Appsync

Allows applications to access exactly the data they need. Developers can create a flexible API to securely access, manipulate, and combine data from multiple sources, 

Customers pay only for requests to the API and for real time messages deliverred to connected clients. 

## IOT 

IOT refers to the collective network of connected devices, and the technology that facilitates communication, both between devices and the cloud. 

### AWS IOT Core

Lets customers connect IOT devices and route messages to AWS services without managing infrastructure. 

### AWS IOT GreenGrass

Is a cloud service that allows you to build, deploy, and manage device s/w. It also includes an open edge runtime for running that s/w on devices at n/w edge

## Web API's 

Application Programming Interface - A web API is an application processing interface between a web server and a web browser. It allows different systems and services to communicate and share data with each other. 

All web servers are APIs but not all APIs are web servers. 

- REST API - Representational State Transfer

It defines a set of functions like POST, GET, PUT, and DELETE, which clients can use to access server data by using HTTP Protocols. 

Its main feature is **statelessness**. Meaning servers do not save client data betweenv requests. 

Benefits: 

- Integration - used to integrate new applications with new software. can be used to leverage existing code.

- Innovation - Incase of rapid deployment of innovative services, changes can be made at the API level without having to re-write the whole code.

- Expansion - API's allow you to match the client's ever changing needs.

- Ease of maintenance - APIs act as gateway between 2 systems. so changes made by one party do not imapact the other or their internal APIs

## AWS CLI 

Unified tool used to manage and automate AWS service. Can control AWS resources from the Command line, making it easier to manage large no. of AWS services. 

## AWS Management Console 

It is a web based GUI that provides a centralized, user friendly platform to manage and monitor AWS services such as EC2, S3, etc. 

Requires a **username and password** to use it. 

## AWS SDKs 

They are a collection of libraries, code samples, and documentation that make it easier for developers to interact with AWS services from within their own applications. 

Available for multiple programming languages. 

## AWS Identity and Access Management (IAM) 

IAM allows you to control access to compute, storage, db, and application services in the AWS cloud. 

Can be used to handle authentication, and enforce authorization policies, so you can specify users access privileges. 

It centrally manages access to launching, configuring, and terminating resources in AWS Acc. Provides granular control over access to resources, including specification of which API calls the user is authorized to make. 


## IAM Identities (Users, Groups, and Roles)

- AWS Account Root User - The first account created on AWS with a Single Sign-in identity that has complete access to all AWS Services and resources in the account. 

Do not use the root user for everyday tasks. 

### IAM User 

Is an identity that you create in AWS. Consists of name and credentials. 

### IAM Group 

Is a collection of users. can attach one or more IAM policies to groups instead of users. Any new person added to the group will have those policies applied and when removed from the group those access permissions will be gone. 

A group cannot contain another group but only users in it. 

### IAM Role 

Is an identity created that has specific permissions. Instead of being uniquely assosciated with one person, a role is intended to be assigned to anyone who needs it. 

## Access and Permissions 

### Authentication 

A user or system must first prove their identity. 

Enable MFA. 

### Access Keys

They are long-term credentials for an IAM user. 

Access keys consist of two parts: an access key ID and a secret access key, you must use both to authenticate your requests. 

Keep rotating access keys. 

### MFA

It is an IAM best practice that requires a second authentication in addition to username and password sign-in. 

- The IAM password policy does not apply to the AWS account root-user password or IAM user access keys. If a password expires, the IAM user can't sign in to the AWS Management Console, but can continue to use their access keys.

### Authentication 

It is the process of determining what permissions a user, service or application should be granted. 

An **IAM Policy** is a JSON document that allows or denies permissions to AWS Services and resources. 

Sample Identity-based policy 


![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/b188f5b9-d7a7-4e9d-a806-1a8d2c0a4f34)

For **resource** based policy you must use the **Principal** element in the JSON policy to specify the principal that is allowed or denied access to a resource. 

### Identity Federation

It is a system of trust between two parties for the purpose of authenticating users and conveying information needed to authorize their access to resources. 


## Some AWS Support Technologies

- AWS Trusted Advisor - helps with billing, performance and policy improvisation.

- AWS Abuse Support - any suspicious phishing abuse emails can be sent their way (abuse@amazonaws.com)

- 

- 
