from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        symptoms = request.form['symptoms'].lower()
        if "yellow" in symptoms:
            diagnosis = "Leaf Blight"
            treatment = "Use neem oil and remove affected leaves."
        elif "spots" in symptoms:
            diagnosis = "Powdery Mildew"
            treatment = "Apply antifungal spray."
        elif "fever" in symptoms:
            diagnosis = "Anthrax"
            treatment = "Isolate the animal and call a vet immediately."
        else:
            diagnosis = "Unknown"
            treatment = "Please consult an expert."
        result = {"diagnosis": diagnosis, "treatment": treatment}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
