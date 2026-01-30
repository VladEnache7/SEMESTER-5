
# ☁️ Cloud Application Architecture

This course introduces the paradigm shift from on-premise hosting to Cloud Computing. The curriculum follows a practical maturity model: starting with lifting-and-shifting applications to Virtual Machines (**IaaS**), optimizing them with Containers (**PaaS**), and finally refactoring them into Event-Driven Serverless functions (**FaaS**).

**Primary Provider:** Amazon Web Services (AWS)

### 📅 Weekly Syllabus

The course is structured to guide you through the "Cloud Migration" journey.

| Week | 👨‍🏫 Lecture Content | ☁️ Hands-on Concepts |
|:---:|:---|:---|
| **1** | **Intro:** Landscape, Providers, Pricing Models, Regions/AZs | AWS Console, Account Setup |
| **2** | **IaaS:** Virtual Machines (EC2), Images (AMI), Block Storage (EBS) | Launching EC2, SSH Keys |
| **3** | **Networking:** VPCs, Subnets, Firewalls (Security Groups) | Defining Network Boundaries |
| **4** | **Scalability:** Horizontal vs Vertical, Load Balancing (ELB), Auto-scaling | Configuring ASGs and LBs |
| **5** | **Web Capabilities:** Static Hosting (S3), DNS (Route53), CDNs (CloudFront) | Hosting a static site on S3 |
| **6** | **Resilience:** High Availability, Multi-AZ deployments, Disaster Recovery | Designing for failure |
| **7** | **Infra Security:** IAM (Users, Roles, Policies), Least Privilege | Managing Permissions |
| **8** | **PaaS:** Docker, Containers, Orchestration (ECS/EKS) | Dockerizing applications |
| **9** | **Data:** Managed Databases (RDS), NoSQL (DynamoDB), Caching (Redis) | Setting up RDS |
| **10** | **App Security:** OAuth, OIDC, Identity Providers (Cognito) | Securing App Access |
| **11** | **Integration:** Decoupling, Queues (SQS), Pub/Sub (SNS) | Async Communication |
| **12** | **Serverless:** FaaS (Lambda), Triggers, Event Sources | Writing Lambda functions |
| **13** | **APIs:** REST Design, API Gateway, Throttling | Exposing Lambda via HTTP |
| **14** | **Recap:** Final Review & Design Patterns | **Project Grading** |

---

### 💻 Laboratory: The Cloud Project

The laboratory involves deploying a real-world application, gradually evolving its architecture.

#### 🧪 Lab Phase 1: Infrastructure as a Service (IaaS)
*   **Networking:** creating a Virtual Private Cloud (VPC) with public/private subnets.
*   **Compute:** Deploying the application on **EC2** instances.
*   **Security:** configuring **Security Groups** (Firewalls) to allow traffic only on specific ports.
*   **Storage:** Using **S3** for object storage (images/files).

#### 🧪 Lab Phase 2: Platform as a Service (PaaS)
*   **Containerization:** Dockerizing the application.
*   **Orchestration:** Deploying the container cluster using **AWS ECS** (Elastic Container Service).
*   **Database:** Moving from a local DB to **AWS RDS** (Managed Relational Database).
*   **CDN:** Setting up **CloudFront** for global content distribution.

#### 🧪 Lab Phase 3: Serverless & Integration
*   **Decoupling:** Breaking monolithic logic into microservices using **SQS** (Queues) and **SNS** (Notifications).
*   **FaaS:** Replacing heavy backend logic with **AWS Lambda**.
*   **API Gateway:** Managing traffic and routing to Lambda functions.
*   **Identity:** Implementing User Management using **AWS Cognito**.

---

### 🧠 Key Concepts (Mind Map Breakdown)

<details>
<summary><strong>Click to expand detailed topic list</strong></summary>

#### I. Infrastructure (IaaS) & Networking
*   **Architecture Pillars:** Reliability, Performance Efficiency, Cost Optimization.
*   **Scalability:**
    *   **Vertical:** Bigger instance (more RAM/CPU).
    *   **Horizontal:** More instances (Auto-scaling Groups).
*   **Networking:**
    *   **VPC:** Your isolated section of the cloud.
    *   **NAT Gateways:** Allowing private instances to talk to the internet.
    *   **Hybrid:** Connecting On-Prem to Cloud (VPN/Direct Connect).

#### II. Platform (PaaS) & Data
*   **Containers:** Solving the "it works on my machine" problem.
*   **Managed Databases:**
    *   *Relational:* Aurora, PostgreSQL.
    *   *NoSQL:* Key-Value (DynamoDB), Document (Mongo).
    *   *Caching:* ElastiCache (Redis/Memcached).
*   **Disaster Recovery:** Backup strategies, Pilot Light, Warm Standby.

#### III. Serverless & Application Security
*   **API Design:**
    *   REST vs GraphQL.
    *   **API Gateway:** Rate limiting, auth offloading, routing.
*   **AuthN vs AuthZ:**
    *   *Authentication (AuthN):* Who are you? (Login/Cognito).
    *   *Authorization (AuthZ):* What can you do? (IAM Policies).
    *   **OAuth/OIDC:** Standard protocols for delegation.
*   **Integration:**
    *   Event-Driven Architecture.
    *   Pub/Sub patterns for fanning out messages (Email/SMS).

</details>

---

### 🛠️ AWS Services Toolbox

*   **Compute:** EC2, Lambda, ECS.
*   **Storage:** S3 (Object), EBS (Block), EFS (File).
*   **Database:** RDS, DynamoDB.
*   **Networking:** VPC, Route53, API Gateway, CloudFront, ELB.
*   **Integration:** SQS, SNS.
*   **Security:** IAM, Cognito, Security Groups.

---

> *"There is no cloud, it's just someone else's computer... but with better uptime and an API."*
