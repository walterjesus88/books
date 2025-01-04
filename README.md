Username: wjesus88

Password: 123456

🛠 Tech Stack

Django

Django REST Framework Docker & Docker Compose GitHub Actions (CI/CD) AWS EC2 (Deployment)

Swagger (API documentation)

🚀 Project Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/walterjesus88/books.git
cd books

2️⃣ Build and Run with Docker

The project is containerized using Docker. To build and run the API locally, use the following command:

docker-compose up --build

This will build the Docker images and start the containers.

3️⃣ Swagger API Documentation

The project includes Swagger for interactive API documentation. Once the server is running, you can access the Swagger interface at:

http://localhost:8000/swagger/

Here, you can explore all the API endpoints, see request and response formats, and test the API directly from the browser.

4️⃣ GitHub Actions (CI/CD)

This project uses GitHub Actions to automate testing and deployment processes. The workflow file is defined in the .github/workflows/ directory.

Every push to the repository triggers the following actions:

Run Tests: Ensures the application is working as expected.

Build Docker Images: Creates Docker images for the application.

Deploy to EC2: Automatically deploys the updated application to the EC2 instance.

5️⃣ AWS EC2 Deployment

The application has been deployed to an AWS EC2 instance. Below are the steps followed for the deployment:

✅ Steps to Deploy on EC2:

Launch an EC2 Instance:

Amazon Linux 2 or Ubuntu as the OS.

SSH into the Instance:

ssh -i <your-key.pem> ec2-user@<ec2-public-ip>

Install Docker and Docker Compose:

sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

Clone the Project Repository:

git clone <your-repository-url>
cd <project-folder>

Run the Docker Containers:

docker-compose up --build -d

The application will be accessible at the EC2 public IP address on port 8000.

📚 API Endpoints

🔐 Authentication

The API requires authentication for certain endpoints. Users can register and log in to access protected endpoints.

📚 Books API

Method

Endpoint

Description

GET /api/books/

Retrieve all books

POST /api/books/

Create a new book

GET /api/books/{title}/

Retrieve a book by title

PUT /api/books/{title}/

Update a book by title

DELETE /api/books/{title}/

Delete a book by title

📊 Average Price API

Method Endpoint Description

GET /api/books/avg-price/{year}/

Retrieve the average price of books for a given year

🧑‍💻 User Registration API

Method Endpoint Description

POST /api/register/

Register a new user

🔍 Swagger Integration

Swagger has been integrated to provide a user-friendly interface for exploring the API. It automatically documents all available endpoints and provides an interactive platform to test them.

To access the Swagger UI:

http://54.215.184.113:8000/swagger/

🔧 Project Structure

├── books
│   ├── books
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── manage.py
│   └── .github
│       └── workflows
│           └── django.yml
│   ├── myapp
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── urls.py
│   │   └── manage.py


🛡 Security Considerations

Do not expose sensitive credentials in your code.

Always use environment variables for sensitive data like passwords, tokens, etc.

Secure your EC2 instance by configuring security groups to allow only necessary traffic.

🧩 Future Improvements

Add JWT authentication.

Implement pagination for large datasets.

Add unit tests for better coverage.

Use a cloud database service like AWS RDS for better scalability.

🤝 Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

📞 Contact

For any inquiries, you can contact:

Author: Walter

Email: [wjesus88@gmail.com]