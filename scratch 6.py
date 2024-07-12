

from flask import Flask, jsonify, request
import csv
import pandas as pd

app = Flask(__name__)


def read_csv():
    data = pd.read_csv('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn July 9.csv')

    #    reader = csv.DictReader(csvfile)
    #    data = [row for row in reader]
    return data







@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = read_csv()
    user = next((item for item in data if int(item['id']) == user_id), None)

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = read_csv()
    user = None

    for item in data:
        if int(item['id']) == user_id:
            user = item
            break

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = read_csv()
    new_user = request.json
    new_user['id'] = str(len(data) + 1)
    data.append(new_user)

    with open('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn July 9.csv', 'a', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_user)

    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = read_csv()
    user = next((item for item in data if int(item['id']) == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    updated_data = request.json
    user.update(updated_data)

    with open('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn July 9.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = read_csv()
    user = next((item for item in data if int(item['id']) == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data.remove(user)

    with open('C://Users//AKASH VISHWAKARMA//Documents//attendence docs//attn July 9.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    return jsonify({'message': 'User deleted'})


if __name__ == '__main__':
    app.run(debug=True)

