
# 📱 Mobile Application Programming

This course covers the full lifecycle of mobile app development, from UI design and local persistence to sensor integration and cloud synchronization. While the lectures provide a comprehensive overview of the Android ecosystem, the laboratory component requires the development of two distinct applications to contrast native and cross-platform approaches.

> **Note:** All official lecture slides, lab requirements, and detailed assignments can be found on the **[Professor's Website](https://www.cs.ubbcluj.ro/~dan/ma/)**.

### 📅 Weekly Syllabus (Lectures)

The lectures focus on architectural patterns, security, and native capabilities within the Android ecosystem.

| Week | 👨‍🏫 Lecture Content |
|:---:|:---|
| **1** | **Basics:** Android Studio, Activity/Fragment Lifecycle, Basic UI |
| **2** | **Networking:** Lists, Adapters, Background Processing, REST Resources |
| **3** | **Architecture:** Master-Detail flow, NavigationDrawer, JSON parsing, ContentProviders |
| **4** | **Persistence:** Local Data, Shared Preferences, Files, SQLite Databases |
| **5** | **Security:** Android Security Model, JWT (JSON Web Tokens), OAuth 2.0 |
| **6** | **Sync:** Data Synchronization, WebSockets, LoaderManagers, Offline-first strategies |
| **7** | **Reactive:** Reactive Programming (RxJava/RxAndroid), Real-time databases (Realm) |
| **8** | **Hardware:** System Services, Background Processes, Sensors (GPS, Accelerometer) |
| **9** | **UX:** Animations (ValueAnimator, ObjectAnimator), Transitions Framework |
| **10** | **Hybrid:** Hybrid Architectures, Angular 2, Ionic Framework |
| **11** | **Business:** Monetization, Ads, In-app Billing, Firebase Integration |
| **12** | **Context:** Awareness APIs, Nearby Connections, Physical Web, Beacon technology |
| **13** | **Quality:** Testing (JUnit, Mockito, Espresso, UI Automator), Firebase Test Lab |
| **14** | **Review:** Exam simulation and final discussions |

---

### 💻 Laboratory Assessment Plan

The laboratory work is structured around two projects: a main **Native** project (Kotlin) and a secondary **Non-Native** project (React/TypeScript). Requirements are to implement similar CRUD functionality in both to compare the development experiences.

| Lab Session | Plan & Focus | Assignment / Deliverable |
|:---:|:---|:---|
| **1** | **Setup:** Requirements discussion, Environment setup, GitHub Classroom enrollment. | **Project Proposal:** Definition of the app idea and domain entities. |
| **2** | **Native UI:** Implementation of the user interface using native technologies. | **CRUD Project (Native - Kotlin):** UI-only implementation where each operation has its own screen, using in-memory data. |
| **3** | **Non-Native UI:** Exploration of cross-platform frameworks. | **CRUD Project (Non-Native - React/TS):** UI-only implementation using React Native/Flutter with in-memory data. |
| **4** | **Local Persistence:** Implementing offline data storage. | **Native w/ Local DB:** Conversion of the Native project to use a local database (SQLite/Room). Cloud services are not permitted at this stage. |
| **5** | **Evaluation:** Review of previous assignments. | *Interim Evaluation* |
| **6** | **Server Integration:** Connecting to a backend service. | **Native w/ Server:** Implementation of server synchronization. The app must function offline (using local DB) and sync when online via a custom REST server. |
| **7** | **Final Exam:** Final presentation and exam simulation. | **Final Defense:** Presentation of functionality and code. |

---

### 🛠️ Project Implementation Details

#### 🟢 Main Project: Native Android (Kotlin)
The primary focus of the semester is the development of a robust native application.
*   **Language:** Kotlin.
*   **Architecture:** MVVM (Model-View-ViewModel) is recommended.
*   **Persistence:** Room Database (SQLite abstraction).
*   **Networking:** Retrofit for REST API communication.
*   **Features:**
    *   Complete CRUD operations for domain entities.
    *   Offline-first architecture (Local DB acts as the single source of truth).
    *   Automatic synchronization with the server when connectivity is restored.
    *   WebSocket integration for real-time updates.

#### 🔵 Secondary Project: Non-Native (React Native)
A smaller-scale project to demonstrate proficiency in cross-platform development.
*   **Language:** TypeScript / JavaScript.
*   **Framework:** React Native (using Expo or CLI).
*   **Features:**
    *   Replication of the Native App's UI and basic flows.
    *   Implementation of CRUD operations.
    *   State management (e.g., React Context or Redux).

---

### ⚙️ Technology Stack

*   **Native Track:** Kotlin, Android SDK, Room, Retrofit, Coroutines/Flow.
*   **Non-Native Track:** TypeScript, React Native, Axios.
*   **Backend:** Custom REST API (Node.js, Python, or Java) required for data synchronization testing.
*   **Tools:** Android Studio, VS Code, Postman, Git.

