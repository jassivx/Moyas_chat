
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Function to read the CSV file and return it as a list of dictionaries
def csv_data():
    try:
        data = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//July 111.csv')
        return data.to_dict(orient='records'), None
    except FileNotFoundError:
        error_message = "File not found"
        return None, error_message
    except pd.errors.EmptyDataError:
        error_message = "There is no data in the file"
        return None, error_message
    except Exception as e:
        error_message = f"There is some error in reading the file, that error is {e}"
        return None, error_message

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    print("Endpoint /users called")
    data, error = csv_data()
    if error:
        return jsonify({'error is-': error}), 500
    return jsonify(data)  # This informs the client application (a web browser or another API) that the data being sent is in JSON format.

# Creating an Endpoint to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data, error = csv_data()
    if error:
        return jsonify({'error': error}), 500

    user = None
    for item in data:
        if int(item['id']) == user_id:
            user = item
            break

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

