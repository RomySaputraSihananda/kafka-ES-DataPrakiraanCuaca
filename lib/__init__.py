from .Kafka import Producer
from .Bmkg import Bmkg
from .utils import ConsumerData, ProducerData
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [ %(levelname)s ] :: %(message)s', datefmt="%Y-%m-%dT%H:%M:%S")