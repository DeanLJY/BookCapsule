from imports import *

app = Flask(__name__)

app.config["PDF_UPLOADS"] = "/home/falloutone/PycharmProjects/summarization/static/pdf/uploads"
app.config["ALLOWED_EXTENSIONS"] = ["PDF"]

def allowed_pdf(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    return False

@app.route('/upload-pdf', methods = ["GET", "POST"])
def upload_pdf():
    if request.method == "POST":

        if request.files:
            pdf = request.files["pdf"]

            if pdf.filename =="":
                print("PDF must have a filename.")
                return redirect(request.url)
            if not allowed_pdf(pdf.filename):
                print("Incorrect extension. Please upload a PDF.")
                return redirect(request.url)
            else:
                filename = secure_filename(pdf.filename)
                pdf.save(os.path.join(app.config["PDF_UPLOADS"], filename))
            return redirect(request.url)

    return render_template('public/upload_pdf.html')

if __name__ == '__main__':
    app.run()
