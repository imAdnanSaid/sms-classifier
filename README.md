<h1 style="text-align: center; color: #0066cc;">📧 SMS/Email Spam Classifier</h1>

<p style="font-size: 16px; line-height: 1.6;">
Welcome to the SMS/Email Spam Classifier project! This project is designed to help you identify whether a given SMS or email message is spam or not, using a machine learning model that I built and deployed as a <a href="https://my-sms-classifier.streamlit.app/" target="_blank" style="color: #ff6600; font-weight: bold;">Streamlit app</a>.
</p>

<h2 style="color: #0066cc;">🚀 Project Overview</h2>

<ol style="font-size: 16px; line-height: 1.6;">
  <li><strong>Data Cleaning:</strong> The data was cleaned to ensure that only relevant and high-quality information was fed into the model.</li>
  <li><strong>Exploratory Data Analysis (EDA):</strong> In-depth analysis of the data was performed to understand patterns and distributions.</li>
  <li><strong>Text Preprocessing:</strong> Tokenization, stemming, and stopwords removal were applied to transform the raw text.</li>
  <li><strong>Model Building:</strong> Various models were tested, and the Multinomial Naive Bayes model achieved 100% precision.</li>
  <li><strong>Model Improvement:</strong> TF-IDF with a maximum of 3000 features was used to enhance accuracy.</li>
  <li><strong>Model Training:</strong> The model was trained and fine-tuned for optimal performance.</li>
  <li><strong>Streamlit App Development:</strong> A user-friendly web application was built using Streamlit.</li>
  <li><strong>Deployment:</strong> The app was deployed and is available for the community.</li>
</ol>

<h2 style="color: #0066cc;">🎯 Features</h2>

<ul style="font-size: 16px; line-height: 1.6;">
  <li><strong>Real-time Classification:</strong> Instantly classify messages as "Spam" or "Not Spam".</li>
  <li><strong>High Precision:</strong> The model is fine-tuned to achieve 100% precision.</li>
  <li><strong>User-Friendly Interface:</strong> The Streamlit app is intuitive and easy to use.</li>
  <li><strong>Community Access:</strong> The app is deployed and available for public use.</li>
</ul>

<h2 style="color: #0066cc;">🔧 Installation</h2>

<ol style="font-size: 16px; line-height: 1.6;">
  <li><strong>Clone the repository:</strong></li>
  <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
    <code>git clone https://github.com/imAdnanSaid/sms-classifier.git<br>cd sms-classifier</code>
  </pre>
  
  <li><strong>Install the required packages:</strong></li>
  <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
    <code>pip install -r requirements.txt</code>
  </pre>
  
  <li><strong>Run the Streamlit app:</strong></li>
  <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
    <code>streamlit run app.py</code>
  </pre>
</ol>

<h2 style="color: #0066cc;">🛠️ Technologies Used</h2>

<ul style="font-size: 16px; line-height: 1.6;">
  <li><strong>Python:</strong> The primary programming language.</li>
  <li><strong>Pandas & NumPy:</strong> For data manipulation and analysis.</li>
  <li><strong>Scikit-learn:</strong> For building and evaluating the machine learning model.</li>
  <li><strong>NLTK:</strong> For text preprocessing.</li>
  <li><strong>Streamlit:</strong> For building and deploying the web application.</li>
</ul>

<h2 style="color: #0066cc;">📊 Model Performance</h2>

<p style="font-size: 16px; line-height: 1.6;">
The Multinomial Naive Bayes model, improved with TF-IDF vectorization, achieved remarkable performance, particularly in precision, making it highly reliable for spam detection.
</p>

<h2 style="color: #0066cc;">🌐 Deployment</h2>

<p style="font-size: 16px; line-height: 1.6;">
The app is deployed on Streamlit and accessible <a href="https://my-sms-classifier.streamlit.app/" target="_blank" style="color: #ff6600; font-weight: bold;">here</a>.
</p>

<h2 style="color: #0066cc;">🤝 Contributing</h2>

<p style="font-size: 16px; line-height: 1.6;">
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
</p>


<h2 style="color: #0066cc;">✨ Acknowledgments</h2>

<p style="font-size: 16px; line-height: 1.6;">
- Special thanks to the Streamlit community for their support and resources.<br>
- The datasets used for training the model were sourced from open data repositories.
</p>
