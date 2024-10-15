# ZeN - Personalized Learning Bot

Welcome to **ZeN**, an intelligent, adaptive learning platform designed to create personalized learning experiences based on user preferences, academic background, and interests. ZeN delivers dynamic content generation and tailored evaluation, ensuring an engaging and efficient learning journey.

## Features

### 1. **Personalized User Onboarding**
   - Users sign up with basic information (name, age, academic status) such as *10th grade*, *Second Year of Computer Science Engineering*, etc.
   - A friendly **chatbot** interaction introduces ZeN and helps gather more personalized details, like the user’s hobbies (e.g., sports, music, favorite personalities). This builds a profile that ZeN will use for customizing learning paths.

### 2. **Knowledge Graph Generation**
   - Based on the information provided, ZeN creates a **knowledge graph** that captures the user's preferences, strengths, and areas of interest.
   - This data-driven approach forms the foundation for personalized recommendations and dynamic content delivery.

### 3. **Personalized Learning Path**
   - Users can either browse recommended topics or suggest their own topics to start learning.
   - For each topic, ZeN generates a **learning path** tailored to the user’s needs. For example, if a user selects **Clustering Algorithms**, ZeN will provide:
     - Definition and introduction to Clustering
     - Use cases and real-world applications
     - Examples to solidify understanding
     - Deep dives into related subtopics

### 4. **Dynamic Content Generation**
   - ZeN generates content specific to the user’s preferences and learning style by getting the user preferences from the Knowledge graph. The learning material isn’t just generic; it's tailored to align with the user's interests, making learning more relevant and engaging.

### 5. **Interactive Learning Experience**
   - ZeN asks **contextual questions** during the learning process to gauge the user's understanding and adapt the next steps in the learning path.
   - The platform continuously adjusts based on the **learning curve**, ensuring the right level of challenge at every stage.

### 6. **Personalized Assignments**
   - After each topic, ZeN provides **assignments** or practical tasks to solidify the user’s understanding of the material.
   - These assignments are tailored to the learner’s level of comprehension and the specific subject matter.



## Technologies Used

- **Natural Language Processing (NLP)**: For chatbot interaction and contextual understanding of user responses. [ **LangChain** ]
- **Graph Databases**: To store and manage the knowledge graph for each user. [ **Neo4j** ]
- **Machine Learning Algorithms**: To adapt the learning paths and content based on the user’s progress. 
- **Content Generation Engines**: Used to personalize and dynamically generate learning material tailored to user preferences. [ **LLAMA 3.1 Provided by Groq**]
