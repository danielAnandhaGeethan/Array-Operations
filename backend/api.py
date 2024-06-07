from flask import Flask, request, jsonify
import math
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/reverse", methods = ["GET"])
def get_reverse_array():
    
    data = request.json
    arr = data['array']
    reversed_array = arr[-1::-1]

    return jsonify(reversed_array)

@app.route("/sort-ascending", methods = ["GET"])
def get_sort_ascending():
    
    data = request.json
    arr = data['array']
    sorted_array = sorted(arr)

    return jsonify(sorted_array)

@app.route("/sort-descending", methods = ["GET"])
def get_sort_descending():
    
    data = request.json
    arr = data['array']
    sorted_array = sorted(arr)[-1::-1]

    return jsonify(sorted_array)

@app.route("/smallest", methods = ["GET"])
def get_smallest():
    
    data = request.json
    arr = data['array']

    smallest = math.inf
    for i in arr:
        if i < smallest:
            smallest = i

    return jsonify(smallest)

@app.route("/largest", methods = ["GET"])
def get_largest():
    
    data = request.json
    arr = data['array']

    largest = -math.inf
    for i in arr:
        if i > largest:
            largest = i

    return jsonify(largest)

@app.route("/count", methods = ["GET"])
def get_count():
    
    data = request.json
    arr = data['array']
    count = 0

    for _ in arr:
        count += 1

    return jsonify(count)

@app.route("/get-values-lesser", methods = ["GET"])
def get_values_less_than_n():
    
    data = request.json

    arr = data['array']
    key = data['key']

    answer = []
    for i in arr:
        if i <= key:
            arr.append(i)

    return jsonify(arr)

@app.route("/get-values-greater", methods = ["GET"])
def get_values_greater_than_n():
    
    data = request.json

    arr = data['array']
    key = data['key']

    answer = []
    for i in arr:
        if i >= key:
            arr.append(i)

    return jsonify(arr)

@app.route("/shuffle", methods = ["GET"])
def get_shuffled_array():
    
    data = request.json

    arr = data['array']

    return jsonify(random.shuffle(arr))

if __name__ == "__main__":
    app.run(debug = True)