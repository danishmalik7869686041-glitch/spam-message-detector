\# 📩 Spam Message Detector



A machine learning-based web application that detects whether a message is \*\*Spam\*\* or \*\*Not Spam\*\*.



\## 🚀 Features



\* Detects spam and legitimate messages

\* Uses Machine Learning for text classification

\* Simple web interface built with Flask

\* TF-IDF text feature extraction

\* Multinomial Naive Bayes classification

\* Trained model saved as a `.pkl` file



\## 🛠️ Technologies Used



\* Python

\* Flask

\* Pandas

\* Scikit-learn

\* HTML

\* CSS

\* JavaScript

\* TF-IDF Vectorization

\* Multinomial Naive Bayes



\## 📊 Model Performance



The trained model currently achieves approximately \*\*75% accuracy\*\* on the test dataset.



\## 📁 Project Structure



```text

spam-message-detector/

│

├── app.py

├── train\_model.py

├── spam\_model.pkl

├── templates/

│   └── index.html

├── static/

│   ├── style.css

│   └── script.js

└── README.md

```



\## ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/danishmalik7869686041-glitch/spam-message-detector.git

```



Move into the project directory:



```bash

cd spam-message-detector

```



Create and activate a virtual environment:



```bash

python -m venv venv

```



Windows:



```bash

venv\\Scripts\\activate

```



Install the required dependencies:



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



Start the Flask application:



```bash

python app.py

```



Then open the local URL shown in the terminal, usually:



```text

http://127.0.0.1:5000

```



\## 🧠 How It Works



1\. The user enters a message.

2\. The message is processed using TF-IDF vectorization.

3\. The trained Naive Bayes model analyzes the text.

4\. The application predicts whether the message is \*\*Spam\*\* or \*\*Not Spam\*\*.

5\. The prediction is displayed on the web interface.



\## 🎯 Purpose



This project was created to demonstrate the practical use of \*\*Machine Learning and Natural Language Processing (NLP)\*\* for text classification.



\## 👨‍💻 Author



\*\*Danish\*\*



GitHub:

https://github.com/danishmalik7869686041-glitch



