# ✈️ ALX Travel App

This project is a robust Django-based travel booking application designed to demonstrate the integration of **Chapa's Payment Gateway API** for secure transactions and the use of **Celery with RabbitMQ** for efficient asynchronous task processing, such as sending booking confirmation emails.

It offers a hands-on experience in building the backend of booking system with modern payment and background task functionalities.

---

## 🎯 Project Goals

* **Seamless Payment Integration**: Integrate Chapa’s Payment Gateway for a smooth and secure payment experience for bookings.
* **Asynchronous Task Handling**: Utilize Celery and RabbitMQ to manage background tasks, ensuring responsive user interactions and timely email notifications.
* **Data Consistency**: Implement secure, atomic booking and payment operations using Django transactions to maintain data integrity.
* **Best Practices**: Adhere to Django and Django REST Framework (DRF) best practices for clean, maintainable, and testable code.

---

## 🛠️ Tech Stack

* **Backend Framework**: Django
* **API Development**: Django REST Framework (DRF)
* **Payment Gateway**: [Chapa API](https://docs.chapa.co/docs/)
* **Asynchronous Tasks**: Celery with RabbitMQ (as message broker)
* **Database**: SQLite (for development; PostgreSQL or MySQL recommended for production)
* **Environment Management**: `python-decouple` for `.env` file configuration
* **API Testing**: Postman, `curl`
* **Admin Interface**: Django Admin
* **HTTP Client**: `requests` library for external API calls (Chapa API)

*(If you're using other technologies like React for frontend, pytest for testing, or Heroku for deployment, feel free to let us know to include them!)*

---

## ⚙️ Features

* **Booking Creation**: Users can create travel bookings by specifying listings, check-in/check-out dates, and guest details.
* **Payment Initiation**: Seamlessly initiate payments via a `POST` request to generate a redirect URL for Chapa’s hosted payment page.
* **Payment Verification**: Automated verification of transactions post-payment using Chapa’s API to confirm payment success.
* **Asynchronous Email Notifications**: Automated booking and payment confirmation emails sent in the background using Celery.
* **Atomic Transactions**: Critical booking and payment processes are wrapped in Django database transactions to guarantee data consistency.
* **RESTful API**: Well-defined API endpoints for managing listings, bookings, and payments.

---

---

## 🚀 How It Works

This application follows a typical request-response and asynchronous processing pattern for bookings and payments:

### 1. Booking Creation

* **Endpoint:** `POST /api/bookings/`
* **Payload Example:**
    ```json
    {
      "listing_id": 1,
      "check_in": "2025-07-01",
      "check_out": "2025-07-05",
      "guests": 2
    }
    ```
* **Action:** Creates a `Booking` object in the database with a `booking_status` of `'pending'`.

### 2. Payment Initiation

* **Endpoint:** `POST /api/initiate-payment/`
* **Payload Example:**
    ```json
    {
      "listing_id": 1,
      "check_in": "2025-07-01",
      "check_out": "2025-07-05",
      "guests": 2,
      "amount": 1000,
      "phone_number": "0912345678"
    }
    ```
* **Action:** Your backend communicates with the Chapa API, receives a checkout URL, and redirects the user to Chapa’s secure hosted payment page.

### 3. Payment Verification (Webhook/Callback)

* **Process:** After the user completes their payment on Chapa's hosted page, Chapa sends an asynchronous notification (a webhook) to your configured `api/verify-payment/` endpoint.
* **Action:** Your backend receives this webhook, then makes a secure server-to-server call back to Chapa's verification API to confirm the definitive payment status. The booking status in your database is updated accordingly (e.g., to 'confirmed' or 'failed').

### 4. Email Confirmation

* **Task:** Upon successful payment verification, a Celery task (e.g., `send_booking_confirmation_email`) is immediately dispatched to RabbitMQ.
* **Action:** The Celery worker picks up this task from the queue and sends an automated confirmation email to the user (e.g., "Hi, your booking for [Listing Title] has been confirmed!"). This process happens in the background, ensuring your API remains responsive.

---

## 📸 Screenshots

### 🧾 Chapa Checkout Page
![Chapa Checkout Page](./screenshots/chapa_checkout.jpg)

---

### 🧾 Test Payment Receipt
![Chapa receipt](./screenshots/chapa_receipt.jpg)