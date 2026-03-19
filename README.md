This project is a full-stack web application built for a national car dealership network. It allows users to browse dealerships across the country, view detailed car inventories, and submit reviews for specific branches. The application is built using a microservices architecture, separating the core user logic from the dealership data management.

Key Features
User Authentication: Secure registration and login functionality.

Dealership Directory: Browse a nationwide list of car dealerships.

Dynamic Reviews: View past reviews for specific dealerships.

Sentiment Analysis: Automatically analyzes review text to tag it as positive, negative, or neutral using an external AI microservice.

Post a Review: Authenticated users can submit new reviews for dealerships they have visited.

Installation & Running Locally
1. Clone the repository

2. Start the Node/MongoDB Microservice:

cd server/database

docker build . -t nodeapp

docker-compose up -d

3. Install Django Dependencies:

cd ../

pip install -r requirements.txt

4. Run Database Migrations:

python manage.py makemigrations

python manage.py migrate

5. Start the Django Development Server:

python manage.py runserver

6. Build the React Frontend:

cd ../frontend

npm install

npm run build

7. View the Application:
Open your browser and navigate to http://localhost:8000/
