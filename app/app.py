#importing flask
from flask import Flask,render_template,request,send_file


app = Flask(__name__)
 
@app.route('/',methods=['POST','GET'])
def plotify():

   

   if request.method=='POST':
        x_axis=request.form.get('x_axis')
        y_axis=request.form.get('y_axis')
        x_axis_updated=[]
        y_axis_updated=[]
        x_axis=x_axis.split(",")
        y_axis=y_axis.split(",")
        for value in x_axis:
            x=float(value)
            x_axis_updated.append(x)
        for value in y_axis:
            y=float(value)
            y_axis_updated.append(y)

        if len(x_axis_updated)!=len(y_axis_updated):
            x_axis=None
            y_axis=None
            return render_template('index.html',x_axis=x_axis,y_axis=y_axis)

        else:

            x_axis=x_axis_updated
            y_axis=y_axis_updated
            return render_template('index.html',x_axis=x_axis,y_axis=y_axis)


   else:

    return render_template('index.html')

   
 
