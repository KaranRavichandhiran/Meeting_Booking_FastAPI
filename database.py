from logger import logger
import sqlite3

DB_NAME = "booking.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    logger.debug("Database connection established.")
    return conn

#Create Bookings Table
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_email TEXT UNIQUE NOT NULL,
    customer_phone INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    description TEXT,
    version INTEGER DEFAULT 1,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(date, time) -- Prevent double booking
)
""")

conn.commit()
conn.close()

logger.info("Database and bookings table initialized.")
print("Booking table created!")
