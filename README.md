# 🌼 Humidity Monitoring API 🌷

## 📝 Description

This is a Flask-based web API for monitoring humidity levels. The application provides endpoints for storing, retrieving, and visualizing humidity data. It also supports setting target humidity values.

## ✨ Features

- Stores real-time humidity readings

- Allows users to set a target humidity level

- Provides historical humidity data

- Includes automated testing with `pytest`

- Uses SQLite as the database backend

- Stores real-time humidity readings

- Allows users to set a target humidity level

- Provides historical humidity data

- Includes automated testing with `pytest`

- Uses SQLite as the database backend

## 🛠️ Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```sh
   git clone HygroMonitor
   cd HygroMonitor
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 💾 Database Initialization

Before running the application, initialize the database:

```sh
python db_init.py
```

## 🏃‍♂️💻 Running the Application

Start the Flask server by running:

```sh
python app.py
```

The API will be available at `http://localhost:8000/`.

## 🌐 API Endpoints

### General Endpoints

- `GET /` - Main index page
- `GET /api/data/` - Returns humidity data for visualization

### Humidity Data

- `GET /api/test/` - Fetches the last 50 humidity records
- `POST /api/get_readings/` - Adds a new humidity reading
  - Example request body:
    ```json
    {
      "humidity": 60
    }
    ```

### Target Humidity

- `GET /api/get_target/` - Retrieves the latest target humidity value
- `POST /` - Sets a new target humidity
  - Example request body:
    ```json
    {
      "target_humidity": 70
    }
    ```

## 🧪 Running Tests

Run the test suite with:

```sh
pytest test_api.py
```

## ⚙️ Technologies Used

- Flask

- Flask-CORS

- Flask-SQLAlchemy

- SQLite

- pytest (for testing)

- Chart.js

- Tailwind CSS

- JavaScript

- HTML

## 🚀 Future Plans

- Implementing an ESP32 microcontroller to read soil humidity data from a sensor and automatically irrigate to maintain the target humidity level

## License

This project is licensed under the MIT License.

## Author

Oskar Michta

