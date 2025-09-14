

# TTN Webhook Backend with DRF & PostgreSQL

This backend system is built with **Django REST Framework (DRF)** to handle IoT sensor data coming from **The Things Network (TTN)** via webhooks.
The project receives uplink data, stores it into a **PostgreSQL database**, and provides a **REST API** for retrieving real-time sensor data.

---

##  Features

* Receive **uplink messages** from TTN using a webhook endpoint.
* Parse and store sensor readings (e.g., temperature, humidity, gas levels, etc.) into **PostgreSQL**.
* Expose RESTful APIs with **DRF** for retrieving:

  * Latest sensor values in real time
  * Historical data (optional, if implemented)
* Structured and scalable backend for IoT data pipelines.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Django 5.x** (or 4.x depending on your setup)
* **Django REST Framework (DRF)**
* **PostgreSQL**
* **Gunicorn / Uvicorn** (for deployment, optional)

---

## 📂 Project Structure

```
ttn_backend/
│── backend/              
│   ├── settings.py       
│   ├── urls.py           
│   └── wsgi.py / asgi.py
│
│── api/                  # DRF app for APIs
│   ├── models.py         # Database models (sensor data)
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API + Webhook views
│   ├── urls.py           # API endpoints
│   └── tests.py
│
│── requirements.txt      
│── manage.py             
│── README.md             
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ttn-backend.git
cd ttn-backend
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Configure PostgreSQL

Update your **`backend/settings.py`**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ttn_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Run migrations:

```bash
python manage.py migrate
```

### 4. Run development server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### 1. Webhook (TTN → Backend)

* **POST** `/api/webhook/`
  TTN will push uplink messages here. Example payload:

```json
{
  "end_device_ids": {
    "device_id": "my-new-device-2"
  },
  "uplink_message": {
    "decoded_payload": {
      "temperature": 23.4,
      "humidity": 56.7
    }
  }
}
```

### 2. Get latest sensor data

* **GET** `/api/data/latest/`
  Returns the most recent sensor readings.

### 3. Get all sensor data

* **GET** `/api/data/`
  Returns all stored records (can be paginated/filtered).

---

## 📡 Deployment Notes

* Use **Gunicorn/Uvicorn + Nginx** for production.
* Environment variables should be managed with **.env files** (e.g., using `django-environ`).
* Consider **Dockerizing** for easier deployment.

---

## ✅ Future Improvements

* Authentication (JWT/Token-based) for API access.
* Data filtering by date/device.
* Real-time push updates using WebSockets.
* Integration with Grafana/PowerBI for visualization.

---

Would you like me to make this README **production-focused** (with Docker + Render/Heroku deployment instructions) or keep it **developer-focused** (local setup + API usage)?
