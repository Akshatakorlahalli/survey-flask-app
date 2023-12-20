from flask import Flask,render_template,request
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    online_count=0
    offline_count=0
    if request.method == "POST":
        name1 = request.form.get("n")
        email = request.form.get("em")
        preferred_teaching = request.form.get("pref")


        if preferred_teaching=="online":
            online_count=online_count+1
        else:
            offline_count=offline_count+1


        fp=open("responses.txt","a")
        fp.write(f"Name:{name1},Email:{email},Preferred_teaching:{preferred_teaching}\n")
       
     
        labels = ['Online', 'Offline']
        counts = [10, 5]

        plt.bar(labels, counts)
        plt.xlabel('Teaching Preference')
        plt.ylabel('Number of Responses')
        plt.title('Teaching Preference Distribution')

        plt.show()
       
        return "<h2>Your Response has been submitted. Thank you, {}!!!</h2>".format(name1)
   




