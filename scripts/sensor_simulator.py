import json
import time
import random
from kafka import KafkaProducer

# Настройки
SENSOR_COUNT = 100
LOCATIONS = ["zone_a", "zone_b", "zone_c"]
INTERVAL_SEC = 5
KAFKA_TOPIC = "sensor_readings"
KAFKA_SERVER = "localhost:9092"

# Создаём продюсера
print("Создаём подключение к Kafka...")
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
print("✅ Подключение к Kafka установлено.")

print("Запуск симулятора датчиков...")
print("Нажмите Ctrl+C чтобы остановить.\n")

try:
    while True:
        for i in range(1, SENSOR_COUNT + 1):
            message = {
                "sensor_id": f"sensor_{i:03d}",
                "location": random.choice(LOCATIONS),
                "temperature": round(random.uniform(-10, 40), 1),
                "humidity": round(random.uniform(20, 90), 1),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }

            # Отправляем в Kafka
            producer.send(KAFKA_TOPIC, value=message)
        
        print(f"📤 Отправлено {SENSOR_COUNT} сообщений в топик '{KAFKA_TOPIC}'")
        time.sleep(INTERVAL_SEC)

except KeyboardInterrupt:
    print("\nОстановка симулятора...")
    producer.close()
    print("✅ Продюсер закрыт.")
