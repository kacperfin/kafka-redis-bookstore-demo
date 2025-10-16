from kafka import KafkaProducer

import random
from time import sleep, time
import json
import logging

from config import KAFKA_BOOTSTRAP_SERVERS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('producer')

authors = ['Amadeusz Burdziak', 'Kacper Aleksander', 'J.K. Rowling', 'Jan Kolwicz', 'Dan Pena', 'Rafał Mazur']

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'))

try:
    while True:
        wait = random.randint(1, 5)
        sleep(wait)

        author = random.choice(authors)
        price = random.randint(40, 110)

        book = {
            'author': author,
            'price': price,
            'timestamp': int(time()*1_000_000)
        }

        producer.send('orders', book)
        logger.info(f'New order: {book}')
except KeyboardInterrupt:
    print('Producer has been shut down.')