-- Practice: DB safety habits + hierarchical structure
-- (based on common "developer mistakes" discussion)

-- 1. Safe practice: never test destructive commands on real data
CREATE TABLE readings_practice AS SELECT * FROM readings;

-- 2. DELETE supports WHERE (row-level, conditional)
DELETE FROM readings_practice WHERE status = 'OK';

-- 3. TRUNCATE does NOT support WHERE (whole-table only)
-- TRUNCATE TABLE readings_practice WHERE status = 'Warning';
-- -> ERROR: syntax error at or near "WHERE"
-- TRUNCATE always wipes everything; use DELETE for conditional removal

-- 4. Hierarchical structure: splitting equipment metadata
-- instead of flattening site/plant into every reading row
CREATE TABLE equipment (
    equipment_id TEXT PRIMARY KEY,
    site TEXT,
    plant TEXT
);

INSERT INTO equipment VALUES ('CV-101', 'Pilbara Mine', 'Crusher Area');
INSERT INTO equipment VALUES ('PMP-07', 'Pilbara Mine', 'Pump Station');
INSERT INTO equipment VALUES ('CV-102', 'Pilbara Mine', 'Crusher Area');

-- 5. JOIN connects readings to equipment via shared key
SELECT readings.equipment_id, equipment.plant, readings.temperature
FROM readings
JOIN equipment ON readings.equipment_id = equipment.equipment_id
WHERE equipment.plant = 'Crusher Area';
