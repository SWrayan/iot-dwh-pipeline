-- Создаём схему raw
CREATE SCHEMA IF NOT EXISTS raw;

-- Создаём таблицу
CREATE TABLE raw.sensor_readings (
    sensor_id TEXT,
    location TEXT,
    temperature NUMERIC(5,2),
    humidity NUMERIC(5,2),
    event_time TIMESTAMP
);
