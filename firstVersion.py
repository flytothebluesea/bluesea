from flask import Flask, request, jsonify

app = Flask(__name__)

# 예시 퀴즈 데이터베이스
quizzes = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "id": 2,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    }
]

# 현재 접속자 수를 저장하기 위한 변수
current_users = 0

@app.route('/quiz', methods=['GET'])
def get_quiz():
    global current_users
    current_users += 1
    return jsonify({
        "question": quizzes[0]["question"],
        "options": quizzes[0]["options"],
        "current_users": current_users
    })

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global current_users
    current_users -= 1
    user_answer = request.json.get('answer')
    correct_answer = quizzes[0]["answer"]
    is_correct = user_answer == correct_answer
    return jsonify({"is_correct": is_correct})

if __name__ == '__main__':
    app.run()
