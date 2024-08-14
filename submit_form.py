import cgi
import sqlite3

form = cgi.FieldStorage()
nickname = form.getvalue('nickname')
user_input = form.getvalue('user-input')

conn = sqlite3.connect('submissions.db')
cursor = conn.cursor()

cursor.execute('''
INSERT INTO submissions (nickname, user_input) 
VALUES (?, ?)
''', (nickname, user_input))

conn.commit()
conn.close()

print("Content-Type: text/html")
print()
print("<html><body>")
print("<h1>Submission Received</h1>")
print(f"<p>Thank you, {nickname}. Your submission has been saved.</p>")
print('<a href="../index.html">Go back to home page</a>')
print("</body></html>")
