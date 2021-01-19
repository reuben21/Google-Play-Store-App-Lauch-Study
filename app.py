from flask import Flask, g, request, jsonify
from functools import wraps
from Questions import Questions

app = Flask(__name__)


@app.route('/ques0', methods=['GET'])
def answer_to_ques0():
    dictionary = Questions.ques0()
    return jsonify(dictionary)


@app.route('/ques1', methods=['GET'])
def answer_to_ques1():
    dictionary = Questions.ques1()
    return jsonify(dictionary)


@app.route('/ques2', methods=['GET'])
def answer_to_ques2():
    list1, list2 = Questions.ques2()

    dict = {
        "list_1": list1,
        "list_2": list2
    }
    return jsonify(dict)


@app.route('/ques3', methods=['GET'])
def answer_to_ques3():
    new_list, label = Questions.ques3()

    dict = {
        "val": new_list,
        "label": label
    }

    return jsonify(dict)


@app.route('/ques4', methods=['GET'])
def answer_to_ques4():
    x, y = Questions.ques4()

    dict = {
        "val": y,
        "label": x
    }

    return jsonify(dict)


@app.route('/ques5', methods=['GET'])
def answer_to_ques5():
    list1, list2 = Questions.ques5()

    dict = {
        "val": list1,
        "label": list2
    }

    return jsonify(dict)


@app.route('/ques6', methods=['GET'])
def answer_to_ques6():
    list1, list2 = Questions.ques6()

    dict = {
        "val": list1,
        "label": list2
    }

    return


@app.route('/ques7a', methods=['GET'])
def answer_to_ques7a():
    list1, list2 = Questions.ques7_a()

    dict = {
        "val": list1,
        "label": list2
    }

    return jsonify(dict)


@app.route('/ques7b', methods=['GET'])
def answer_to_ques7b():
    list1, list2 = Questions.ques7_b()

    dict = {
        "val": list1,
        "label": list2
    }

    return jsonify(dict)


if __name__ == '__main__':
    app.run(debug=True)
