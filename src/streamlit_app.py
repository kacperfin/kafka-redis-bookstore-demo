import streamlit as st
import redis
import pandas as pd

import json
from time import sleep
import logging

from config import REDIS_HOST, REDIS_PORT

if 'redis' not in st.session_state:
    st.session_state.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

st.title('📚 Bookstore')

n_of_orders = st.session_state.redis.llen('orders')
st.metric('Number of orders', n_of_orders)

st.write('Last 20 orders:')
orders = st.session_state.redis.lrange('orders', 0, 19)
orders = [json.loads(msg) for msg in orders]
df = pd.DataFrame(orders)
st.dataframe(df)

sleep(1)
st.rerun()