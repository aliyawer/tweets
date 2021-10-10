from flask import Flask
from flask_celery import make_celery
import os
import json

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = make_celery(app)


@app.route('/count', methods=['GET'])
def process():
    result = count.delay()
    return result.get()


@celery.task(name='app.count')
def count():
    number_of_hon = 0
    number_of_han = 0
    number_of_den = 0
    number_of_det = 0
    number_of_denna = 0
    number_of_denne = 0
    number_of_hen = 0

    for file in os.listdir("../data"):
        with open(os.path.join("../data", file)) as f:
            lines = f.readlines()

            for line in lines:
                try:
                    data = json.loads(line)
                    if(data['retweeted'] == False):
                        hon = data['text'].count(" hon ")
                        han = data['text'].count(" han ")
                        den = data['text'].count(" den ")
                        det = data['text'].count(" det ")
                        denna = data['text'].count(" denna ")
                        denne = data['text'].count(" denne ")
                        hen = data['text'].count(" hen ")

                        number_of_hon += hon
                        number_of_han += han
                        number_of_den += den
                        number_of_det += det
                        number_of_denna += denna
                        number_of_denne += denne
                        number_of_hen += hen

                except json.decoder.JSONDecodeError:
                    pass

    result = {
        "hon": number_of_hon,
        "han": number_of_han,
        "den": number_of_den,
        "det": number_of_det,
        "denna": number_of_denna,
        "denne": number_of_denne,
        "hen": number_of_hen,
    }

    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
