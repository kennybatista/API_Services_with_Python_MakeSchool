from flask import Flask, request, json
app = Flask(__name__)

listOfPets = []
nameOfPets = []

# / route
@app.route("/")
def index():
    return "Hey buddy! This is the index page"

# /hello route
@app.route("/hello")
def hello():
    return "Hello World"

# /pets route
# We will be able to POST and REQUEST data from this route
@app.route("/pets", methods=["GET","POST"])
def pets():
    if request.method == "GET":
        return json.dumps(listOfPets)

    elif request.method == "POST":
        result = request.args.to_dict()

        if ('name' in result.keys()) & ('age' in result.keys()) & ('species' in result.keys()):
            nameOfPet = result["name"]

        if nameOfPet not in nameOfPets:

            listOfPets.append(result)

            nameOfPets.append(nameOfPet)
            return ""

        else:
            return "HTTP 409 Error: Conflict -- Pet already exits in store", 409

    else:
        return "HTTP 400 Error: Bad Request"




# /pets/<name>
@app.route("/pets/<path:name>", methods=["GET", "PUT", "DELETE"])
def petPath(name):
    if request.method == "GET":
        for pet in listOfPets:
            if pet["name"] == name:
                return json.dumps(pet)
        return "HTTP 404 Error: Page Not Found -- Pet does not exist in store", 404

    elif request.method == "PUT":
        result = request.args.to_dict()

        if name in nameOfPets:
            if "age" in result.keys():

                indexOfPet = nameOfPets.index(name)

                listOfPets[indexOfPet]["age"] = result["age"]
                return ""
            else:
                return "HTTP 400 Error", 400
        else:
            return "HTTP 404 Error: Page not found"
    elif request.method == "DELETE":
        if name in nameOfPets:
            indexOfPet = nameOfPets.index(name)
            petObject = listOfPets[indexOfPet]

            del listOfPets[indexOfPet]
            del nameOfPets[indexOfPet]

            return json.dumps(petObject)
        else:
            return "HTTP 404 Error: Page Not Found"


if __name__ == "__main__":
    app.run()
