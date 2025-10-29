from kafka import KafkaProducer

import random
from time import sleep, time
import json
import logging

from config import KAFKA_BOOTSTRAP_SERVERS
from consumer_utils.get_random_book import get_random_book

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('producer')

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'))

def on_send_success(record_metadata):
    logger.info(f'Sent order to topic={record_metadata.topic}, partition={record_metadata.partition}, offset={record_metadata.offset}')

def on_send_error(exc):
    logger.error(f'Failed to send order: {exc}')

try:
    while True:
        wait = random.randint(1, 5)
        sleep(wait)

        book = get_random_book()
        book['timestamp'] = int(time()*1_000_000)

        future = producer.send('orders', book)
        logger.debug(f'Attempting to send order: {book}')

        future.add_callback(on_send_success)
        future.add_errback(on_send_error)
        
except KeyboardInterrupt:
    print('Producer has been shut down')
finally:
    producer.flush()