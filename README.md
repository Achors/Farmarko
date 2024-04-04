# Farmarko

# Online Marketplace for Local Farmers

Welcome to the Online Marketplace for Local Farmers! This project aims to create a platform that connects local farmers with consumers, allowing them to buy fresh produce directly from the source. The platform facilitates the listing of products by farmers, browsing and purchasing by consumers, and order management by farmers.

## Features

- **User Roles:** Farmers/suppliers and consumers can register, create profiles, and interact with the platform based on their roles.
- **Product Listings:** Farmers can list their products with details such as name, description, price, and quantity available.
- **Search and Filter:** Consumers can search for products based on categories, keywords, and price range.
- **Shopping Cart:** Consumers can add products to a shopping cart, review selections, and proceed to checkout for payment.
- **Order Management:** Farmers can view and manage orders, fulfill orders, and update order status.
- **Payment Integration:** Secure online payments are facilitated through integration with a payment gateway.
- **Reviews and Ratings:** Consumers can leave reviews and ratings for products they've purchased.
- **Messaging System:** Farmers and consumers can communicate regarding orders and product inquiries.
- **Delivery/Pickup Options:** Consumers can choose between delivery and pickup options for their orders.

## Tech Stack

- **Frontend:** React with TypeScript, React Router, Axios, and Redux for state management.
- **Backend:** Python with Django framework, Django ORM, and Django REST Framework for API development.
- **Database:** PostgreSQL for storing user data, product listings, and orders.

## Setup Instructions

1. Clone the repository:

        git clone <this repo url>

2. Navigate to the project directory:

        cd online-marketplace-for-local-farmers


3. Install dependencies for the frontend and backend:

                cd frontend
                npm install
                cd ../backend
                pip install -r requirements.txt


4. Set up the database and run migrations:

            python manage.py makemigrations
            python manage.py migrate


5. Start the frontend and backend servers:

            cd ../frontend
            npm start
            cd ../backend
            python manage.py runserver

6. Access the application in your web browser:

        http://localhost:3000


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This project was inspired by the need to support local farmers and promote sustainable agriculture.
- Special thanks to all contributors and open-source projects used in the development of this application.

