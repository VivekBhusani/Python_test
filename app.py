from flask import Flask,render_template,send_from_directory
app = Flask(__name__)
import markdown
@app.route('/')
def index():
    file = open("file1.txt", 'r')
    Lines = file.readlines()
    return render_template('result.html',Lines=Lines,fname="file1")

@app.route('/<filename>', defaults={'numbers': None})
@app.route("/<filename>/<numbers>",methods=['GET'])
def fileReader(filename, numbers):
    if numbers==None and filename!='file4':
        file = open(filename+".txt", 'r')
        Lines = file.readlines()
        return render_template('result.html',Lines=Lines,fname=filename)

    elif numbers !=None and filename!="file4":
        file = open(filename + ".txt", 'r')
        Lines = file.readlines()
        Lines = Lines[0:int(numbers)]
        return render_template('result.html',Lines=Lines,fname=filename)


    elif filename == 'file4':

        return send_from_directory('templates', 'index.html')






if __name__ == "__main__":
    app.run()