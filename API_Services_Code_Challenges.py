from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/hello')
def john():
    return 'Hello, my name is Kenny Batista'

@app.route('/pets',methods=['POST'])
def pets():
    try:
        petIdentity = []

        result = request.form

        name = result['name']
        age = result['age']
        species = result['species']

        petIdentity.append(name)
        petIdentity.append(age)
        petIdentity.append(species)

        print petIdentity
        return 'The dogs name is ' + name + ' and he is ' + age + ' years old. His breed is ' + species
    except Exception as e:
        return ' 404, there was an error with the list input. Check if all inputs were sent '

@app.route('/pets/<name>')
def petsName():
    return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
