import sqlite3
import os

def create_database():
    db_path = os.path.join('resources', 'proofreading_tool.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create user_prompts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_prompts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt_name TEXT UNIQUE NOT NULL,
        prompt_content TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()