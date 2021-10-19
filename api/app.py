from flask import Flask, render_template
from celery import Celery
import os
import json

app = Flask(__name__, template_folder='template')

celery = Celery('worker',
                broker='amqp://admin:admin@rabbit:5672//',
                backend='rpc://')


@app.route('/data', methods=['GET'])
def data():
    AcyncResult = counter.delay()
    data = AcyncResult.get()
    labels = [*data.keys()]
    values = [*data.values()]
    json_object = json.dumps(data, indent = 4) 
    return render_template('index.html', data=json_object , labels=labels, values=values)


@celery.task(name='app.count')
def counter():
    number_of_hon = 0
    number_of_han = 0
    number_of_den = 0
    number_of_det = 0
    number_of_denna = 0
    number_of_denne = 0
    number_of_hen = 0

    for file in os.listdir("data"):
        with open(os.path.join("data", file)) as f:
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

    return result


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
