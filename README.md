Username: wjesus88

Password: 123456

🛠 Tech Stack

Django

<h1 align="center">Django REST Framework Docker & Docker Compose GitHub Actions (CI/CD) AWS EC2 (Deployment) </h1>

El desarrollo de este proyecto se hizo con las siguientes tecnologias
Swagger (API documentation)

🚀 Project Setup Instructions

1️⃣  <p align="left">  Clone the Repository  </p>

    git clone https://github.com/walterjesus88/books.git
    cd books

2️⃣ Build and Run with Docker

El proyecto está en contenedores utilizando Docker. Para compilar y ejecutar la API localmente, utilice el siguiente comando:

    docker-compose up --build

Esto creará las imágenes de Docker e iniciará los contenedores.

    docker-compose exec web python manage.py makemigrates
    docker-compose exec web python manage.py migrate   #creara las tablas de django y books

Para correr los test ejecuta lo siguiente:

    docker-compose exec web python manage.py test books


3️⃣ Swagger API Documentation 

El proyecto incluye Swagger para documentación API interactiva. Una vez que el servidor se esté ejecutando, puede acceder a la interfaz Swagger en:

    http://localhost:8000/swagger/ 

Aquí puede explorar todos los puntos finales de la API, ver los formatos de solicitud y respuesta y probar la API directamente desde el navegador.

4️⃣ GitHub Actions (CI/CD)

Este proyecto utiliza GitHub Actions para automatizar los procesos de prueba e implementación. El archivo de flujo de trabajo se define en el directorio .github/workflows/.

Cada envío al repositorio desencadena las siguientes acciones:

Ejecutar pruebas: garantiza que la aplicación funcione como se esperaba.

Crear imágenes de Docker: crea imágenes de Docker para la aplicación.

Implementar en EC2: implementa automáticamente la aplicación actualizada en la instancia EC2.

5️⃣ AWS EC2 Deployment

La aplicación se ha implementado en una instancia AWS EC2. A continuación se detallan los pasos seguidos para la implementación:

✅ Steps to Deploy on EC2:

Launch an EC2 Instance:

Ubuntu as the OS.

SSH into the Instance:

ssh -i <your-key.pem> ec2-user@<ec2-public-ip>

En este cado se uso el ip http://54.215.184.113:8000/swagger/

Se Instalo Docker y Docker Compose:

sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

El github actions ya clona e instala dependencias para su funcionamiento

Run the Docker Containers:

docker-compose up --build -d en caso de quere reiniciar

The application will be accessible at the EC2 public IP address on port 8000.

![Texto alternativo](swagger.png)


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