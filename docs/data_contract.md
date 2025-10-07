# Data Contract: Sensor Readings

## Источник
Имитация IoT-датчиков температуры и влажности.

## Частота
Каждые 5 секунд от каждого датчика.

## Формат сообщения (JSON)
```json
{
  "sensor_id": "string, уникальный ID датчика, например 'sensor_001'",
  "location": "string, зона размещения: 'zone_a', 'zone_b' или 'zone_c'",
  "temperature": "number, температура в °C, диапазон [-20; 50]",
  "humidity": "number, влажность в %, диапазон [0; 100]",
  "timestamp": "string, ISO 8601, например '2024-06-15T10:23:45Z'"
}
