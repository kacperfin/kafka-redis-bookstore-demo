# Kafka-Redis Bookstore Demo

A learning project demonstrating real-time data streaming with Kafka, Redis, and Streamlit.

## Architecture

- **Producer** - Generates random book orders and sends them to Kafka
- **Consumer** - Reads from Kafka and stores orders in Redis
- **Dashboard** - Streamlit app displaying real-time order metrics

## Tech Stack

- Apache Kafka (message broker)
- Redis (data store)
- Streamlit (visualization)
- Docker Compose (infrastructure)

## Setup

1. Copy environment configuration:
   ```bash
   cp .env.example .env
   ```

2. Start infrastructure:
   ```bash
   docker-compose up -d
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the pipeline:
   ```bash
   # Terminal 1 - Start producer
   python src/producer.py

   # Terminal 2 - Start consumer
   python src/consumer.py

   # Terminal 3 - Start dashboard
   streamlit run src/streamlit_app.py
   ```

5. Open dashboard at `http://localhost:8501`

## Project Structure

- `src/producer.py` - Kafka producer generating book orders
- `src/consumer.py` - Kafka consumer writing to Redis
- `src/streamlit_app.py` - Real-time dashboard
- `docker-compose.yml` - Kafka and Redis containers
