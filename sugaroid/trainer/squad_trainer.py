import requests
from sugaroid.sugaroid import Sugaroid
request = requests.get('https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json')

training_data = request.json()

data = training_data['data']


sugaroid = Sugaroid(False)
sugaroid.init_local_trainers()

for i in data:
    category_data = i
    print('Training {}'.format(category_data.get('title')))
    paragraphs = category_data.get('paragraphs')
    for j in paragraphs:
        qas = j.get('qas')
        for k in qas:
            question_data = k
            question = question_data.get('question')
            answers = question_data.get('answers')
            print('id: ', question_data.get('id'))
            for answer in answers:
                sugaroid.list_train(
                    [question,
                     answer.get('text')])
