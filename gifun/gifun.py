from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')
def up():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def gif():
    picture = request.files['load']

    picture.save(picture.filename)

    up = requests.post('https://api.imagga.com/v2/uploads',

                        auth=('acc_d208876839edf33', 'b1ab9fb2e2f810eb0d66785bd2204b13'),

                        files={'image': open(picture.filename, 'rb')}).json()['result']['upload_id']

    export = requests.get('https://api.imagga.com/v2/tags',

                            auth=('acc_d208876839edf33', 'b1ab9fb2e2f810eb0d66785bd2204b13'),

                            params={'image_upload_id': up}).json()['result']['tags'][0]['tag']['en']

    show = requests.get('http://api.giphy.com/v1/gifs/search',

                        params={'q': export, 'api_key': 'fMWrKsvbTS55nnmdkY8Wss15zGaTw2Y5'}).json()['data']

    array = []

    for i in range(0, 10):
        tt = show[i]['images']['fixed_height']['url']
        array.append(tt)

    return render_template('finally.html', resp=array)

if __name__ == '__main__':
    app.run(debug=True)