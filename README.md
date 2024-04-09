# Counter-Billing-System
Assignment for SPACE-Y Organisation

This project is a web-based billing system for a small-scale shopping mall. It allows employees to manage products, and customers, and generate bills for cash payments.

## Features

- **Authentication:** Employees can authenticate themselves to access the system.
- **Product Management:** Add, update, and delete products from the system.
- **Customer Management:** Add, update, and delete customers.
- **Billing:** Generate bills for customers, supporting only cash payment method.

## Technology and Libraries used-
- Django Framework
- Django REST Framework with Generic Views
- Python for APIs
- Google-Cloud-Platform
- PostgreSQL for database hosted on GCP
- Swagger interface with Drf-spectacular library 
- JWT for Authentication

## Bonus Features added-
-	Analytics API which tells which user(employee) made the maximum sales, which product sells the most
-	JWT AUTHENTICATION to update Employee Details and Password


## How to Run code-
## Prerequisites

- Python 3.x installed on your Linux VM/Windows (local)
- pip package manager installed
- Virtualenv package installed (optional but recommended)

## Setup ( FROM VM machine hosted on GCP)

1. SSH into your Linux VM hosted on Google Cloud Platform.
2. Clone the project repository:
   ```bash
   git clone <repository_url>
   ```
3. Navigate to the project directory:
   ```bash
   cd Counter_Billing_System
   ```
4. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Navigate to the billingapp directory:
   ```bash
   cd billingapp
   ```
7. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
8. Run the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Setup (on local windows machine)

1. Open Command Prompt (cmd) or PowerShell on your Windows machine.
2. Clone the project repository:
   ```bash
   git clone <repository_url>
   ```
   If you don't have Git installed, you can download the repository as a ZIP file and extract it.
3. Navigate to the project directory:
   ```bash
   cd Counter_Billing_System
   ```
4. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
5. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Navigate to the billingapp directory:
   ```bash
   cd billingapp
   ```
7. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
8. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Accessing the Application

Once the development server is running, you can access the application in your web browser by navigating to:
```
http://127.0.0.1:8000
```

## More functionalities soon to be added to be added to this Project such as-
- Sales Analytics with Best Product recommendation based on customer purchase behaviour.
- Customer Loyalty and Reward Programs that offer Discounts, Coupons and exclusive deals.
- Analysis and Data Visualization of Traffic and customers to know at what peak time the store operates at its potential.
- Inventory management API, to handle large inventory into sub-sections.
- Multiple Payment modes like UPI and cards other than Cash.


