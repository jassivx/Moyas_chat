from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Function to read the CSV file and return it as a list of dictionaries
def csv_data():
    try:
        data = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn July9.csv')
        return data.to_dict(orient='records')
    except FileNotFoundError:
        print("File not found")
        return None
    except pd.errors.EmptyDataError:
        print("There is no data in the file")
        return None

    except Exception as e:
        print("there is some error in reading the file, that error is{e} ")
        return None

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    data = csv_data()
    return jsonify(data) #This informs the client application(a web browser or another API)-
                         # -that the data being sent is in JSON format.

#Creating an Endpoint to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = csv_data()
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
