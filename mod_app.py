from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from chat import get_response
import mysql.connector
from bert_model import review


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)


# Create a MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="mymysqlZ666#",
    database="cmdet"
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Execute a query to select all entries in the ref_no column
query = "SELECT ref_no FROM restcdata"
cursor.execute(query)

# Fetch all the results and store them in the refnos list
refnos = [row[0] for row in cursor.fetchall()]

# Close the cursor and connection
cursor.close()
conn.close()

feedback_state = False

bot_name = "Serra"

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/predict", methods=['POST'])
def predict():
    global feedback_state
    text = request.get_json().get("message")
    if feedback_state:
        response = handle_message2(text)
    else:
        response = handle_message(text)
    message = {"answer": response}
    socketio.emit('chat_response', message)
    return jsonify(message)

def handle_message(text):
    global feedback_state, ref1
    if text == "1":
        return "Please enter your Reference ID"
    elif text in refnos:
        ref1 = text
        feedback_state = True
        return "Please leave your feedback/review."
    else:
        return get_response(text)

def handle_message2(text):
    global feedback_state, ref1
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="mymysqlZ666#",
        database="cmdet"
    )
    cursor = conn.cursor()
    cursor.execute("update restcdata set comments=%s where ref_no=%s", (text,ref1))
    cursor.close()
    conn.commit()
    conn.close()
    response2 = review(text,ref1)
    feedback_state = False
    return response2

if __name__ == "__main__":
    socketio.run(app, debug=True)