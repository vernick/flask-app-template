# My Flask App

This is a simple Flask application that listens for incoming webhooks on port 3000.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python run.py
   ```

## Usage

The application listens for POST requests on the `/webhook` endpoint. You can send your webhook data to this endpoint to handle incoming requests.

## License

This project is licensed under the MIT License.