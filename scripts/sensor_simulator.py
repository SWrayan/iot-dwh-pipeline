import json
import time
import random

# Параметры
SENSOR_COUNT = 100
LOCATIONS = ["zone_a", "zone_b", "zone_c"]
INTERVAL_SEC = 5  # каждые 5 секунд

print("Запуск симулятора датчиков...")
print("Нажмите Ctrl+C чтобы остановить.\n")

try:
    while True:
        # Генерируем данные для одного "пакета" (все датчики за раз)
        for i in range(1, SENSOR_COUNT + 1):
            sensor_id = f"sensor_{i:03d}"  # sensor_001, sensor_002, ...
            location = random.choice(LOCATIONS)
            temperature = round(random.uniform(-10, 40), 1)  # от -10 до 40°C
            humidity = round(random.uniform(20, 90), 1)      # от 20% до 90%
            
            message = {
                "sensor_id": sensor_id,
                "location": location,
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            
            print(json.dumps(message))
        
        print(f"\n--- Отправлено {SENSOR_COUNT} записей. Ждём {INTERVAL_SEC} секунд ---\n")
        time.sleep(INTERVAL_SEC)

except KeyboardInterrupt:
    print("\nСимулятор остановлен.")
