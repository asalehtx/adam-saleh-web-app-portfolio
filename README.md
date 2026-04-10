Adam Saleh - Web App Portfolio 🚀

A full-stack portfolio demonstrating RESTful API design, frontend JavaScript integration, and responsive CSS. Built with Python and Flask, this application serves as both an interactive developer portfolio and a live demonstration of three custom-built backend engines.

View Live Deployment: https://adam-saleh-web-app-portfolio.up.railway.app

TECH STACK
Backend: Python, Flask, REST APIs, Gunicorn

Frontend: Vanilla JavaScript, HTML5, CSS3 (Flexbox/Media Queries)

Data Visualization: Chart.js

Deployment: Railway

FEATURED PROJECTS
Personal Finance Dashboard (Full-Stack)
A complete, interactive financial tracking application that functions without page reloads.

Asynchronous CRUD: Users can add, edit, and delete transactions using the Fetch API.

Data Visualization: Utilizes Chart.js to render real-time Categorical Pie Charts and Time-Series Line Graphs.

Dynamic Budgeting: Backend logic monitors category limits and issues dynamic frontend overspending alerts.

CSV Export: Generates downloadable, formatted .csv reports of ledger data via a custom Python io.StringIO buffer.

Responsive Design: Features a mobile-first transaction table that transforms into a custom "Card" layout on small screens using advanced CSS media queries.

User Configuration Manager (API)
A complete CRUD REST API that allows applications to store, retrieve, modify, and delete user preferences (theme, language, notification toggles) using a mock database.

Content Feed & Subscription (API)
A RESTful service implementing a Pub/Sub model. Users can subscribe to topics, retrieve an algorithmically filtered personalized feed of articles, and receive dynamic topic recommendations based on missing subscriptions.

LOCAL INSTALLATION & SETUP
If you want to run this application locally on your machine, follow these steps in your terminal:

Clone the repository:
git clone https://github.com/asalehtx/adam-saleh-web-app-portfolio.git
cd adam-saleh-web-app-portfolio

Create and activate a virtual environment:

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Install the dependencies:
pip install -r requirements.txt

Run the Flask server:
flask run

(The app will be available at http://127.0.0.1:5000)

DEPLOYMENT
This application is configured for production deployment using Gunicorn. The included Procfile and requirements.txt allow for seamless deployment on platforms like Railway, Heroku, or Render.

Start Command: gunicorn app:app

Designed and built by Adam Saleh.
