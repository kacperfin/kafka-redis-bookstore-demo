from kafka import KafkaConsumer
import redis

import json
import logging

from config import KAFKA_BOOTSTRAP_SERVERS, REDIS_HOST, REDIS_PORT

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('consumer')

consumer = KafkaConsumer('orders',
                         bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         group_id='redis-consumer-group',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         auto_offset_reset='earliest')

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

pipe = r.pipeline()

try:
    for msg in consumer:
        pipe.lpush('orders', json.dumps(msg.value))
        pipe.execute()

        logger.info(f'Order: {msg.value} set in Redis.')
except KeyboardInterrupt:
    print('Consumer has been shut down.')