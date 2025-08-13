import sqlite3

# Connect to (or create) database
conn = sqlite3.connect("qa_database.db")
cursor = conn.cursor()

# Create a sample table (if not exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS qa (
    question TEXT,
    answer TEXT
)
''')

# Insert sample Q&A (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM qa")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ("What is Python?", "Python is a high-level programming language."),
        ("Who developed Python?", "Python was developed by Guido van Rossum."),
        ("What is SQLite?", "SQLite is a lightweight, file-based database.")
    ]
    cursor.executemany("INSERT INTO qa (question, answer) VALUES (?, ?)", sample_data)
    conn.commit()

# Function to find answer
def get_answer(question):
    cursor.execute("SELECT answer FROM qa WHERE question LIKE ?", ('%'+question+'%',))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return "Sorry, I don't know the answer."

# Example usage
while True:
    user_question = input("Ask a question (or type 'exit'): ")
    if user_question.lower() == "exit":
        break
    print("Answer:", get_answer(user_question))

conn.close()
