# Kafka-Redis Bookstore Demo

A learning project demonstrating real-time data streaming with Kafka, Redis, and Streamlit.

## Architecture

- **Kafka** - Message broker for streaming book orders
- **Redis** - In-memory data store for order history
- **Producer** - Generates random book orders and sends them to Kafka
- **Consumer** - Reads from Kafka and stores orders in Redis
- **Dashboard** - Streamlit app displaying real-time order metrics from Redis

## Tech Stack

- Python 3.12
- Apache Kafka (message broker)
- Redis (data store)
- Streamlit (visualization)
- Docker Compose (infrastructure)

## Setup

1. Copy environment configuration:
   ```bash
   cp .env.example .env
   ```

2. Start all services:
   ```bash
   docker compose up
   ```

3. Open dashboard at `http://localhost:8501`

## Management

**View logs**:
```bash
docker compose logs -f [service_name]  # producer, consumer, streamlit_app, kafka, redis
```

**Stop all services**:
```bash
docker compose down
```

**Stop and remove volumes**:
```bash
docker compose down -v
```

## Project Structure

- `src/producer.py` - Kafka producer generating book orders
- `src/consumer.py` - Kafka consumer writing to Redis
- `src/streamlit_app.py` - Real-time dashboard
- `src/config.py` - Configuration loader
- `docker-compose.yml` - Orchestrates all 5 services
- `Dockerfile` - Python service container definition
- `requirements.txt` - Python dependencies list
