from prediction_service import prediction
from flask import Flask, render_template, request,jsonify
import os
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")


app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)
@app.route("/",methods=['GET','POST'])
def index():
      if request.method == 'POST' :

            try:

                            path = request.files['file']
                            path= path.filename
                            response = prediction.form_response(path)
                            result = "The Top Ten Predictions are "
                            return render_template("index1.html", response=[response],result=result)


            except Exception as e:
                    error = {"error":e}
                    return render_template("404.html",error=error)
 
      else:
          return render_template('index1.html')

if __name__ =="__main__":
    app.run(debug=True)