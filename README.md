# Umar's Chatbot Project
    
<h2>Project Overview</h2>
    <p>
        This project is a chatbot powered by the Google Gemini AI model. The chatbot interacts with users and provides personalized responses based on predefined information about the owner, Umar. It is built using <strong>Streamlit</strong> and integrated with <strong>Google Generative AI</strong> for natural language processing. 
    </p>

<h2>Key Features</h2>
    <ul>
        <li><strong>Personalized Responses:</strong> The chatbot responds with detailed information about the creator, Umar, including personal background, skills, internships, and projects.</li>
        <li><strong>Chat History Persistence:</strong> The chatbot saves the chat history to ensure continuity across sessions. Even after refreshing the page, the history is restored.</li>
        <li><strong>Customizable Queries:</strong> Users can ask various questions about Umar (e.g., "Who is Umar?", "Tell me about Umar's skills") and receive consistent, accurate responses.</li>
        <li><strong>Streamlit Interface:</strong> The chatbot is integrated with Streamlit to create an easy-to-use interface for users.</li>
    </ul>

<h2>Technologies Used</h2>
    <ul>
        <li><strong>Streamlit:</strong> A framework for building interactive web applications.</li>
        <li><strong>Google Generative AI (Gemini):</strong> Provides natural language processing for the chatbot.</li>
        <li><strong>Python:</strong> The programming language used to build the application.</li>
        <li><strong>Pickle:</strong> Used to store and load chat history persistently.</li>
        <li><strong>Dotenv:</strong> Loads environment variables for secure API key management.</li>
    </ul>

<h2>How to Run the Project</h2>
    <p>Follow these steps to run the chatbot on your local machine:</p>
    <ol>
        <li>Clone the repository to your local machine:</li>
        <code>git clone https://github.com/yourusername/umar-chatbot</code>
        
<li>Install the necessary dependencies:</li>
        <code>pip install -r requirements.txt</code>
        
<li>Set up the environment variables for the Google API key:</li>
        <p>Create a <strong>.env</strong> file in the root directory and add the following content:</p>
        <code>GOOGLE_API_KEY=your_google_api_key_here</code>
        
<li>Run the Streamlit app:</li>
        <code>streamlit run app.py</code>
        
<li>Open your browser and navigate to <strong>http://localhost:8501</strong> to interact with the chatbot.</li>
    </ol>

<h2>Chatbot Responses</h2>
    <p>
        The chatbot is designed to provide responses based on predefined patterns. For example, if a user asks "Who is Umar?", the chatbot responds with a personalized description of Umar, including information such as:
    </p>
    <ul>
        <li>Name: Muhammad Umar</li>
        <li>Education: Final-year BS Computer Science student</li>
        <li>Internships: Machine Learning Engineer Intern at Technocolabs Softwares</li>
        <li>Skills: Python, Data Analysis, Deep Learning, etc.</li>
        <li>Projects: Home Price Prediction, Employee Attrition Forecasting, etc.</li>
    </ul>

<h2>Future Improvements</h2>
    <ul>
        <li>Integration with more advanced natural language processing models for dynamic responses.</li>
        <li>Incorporating additional user-specific queries to expand chatbot's functionality.</li>
        <li>Enhance UI/UX to make the chatbot interface more engaging.</li>
    </ul>



