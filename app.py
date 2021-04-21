from flask import Flask
import tbbt

app = Flask(__name__)

css = """     @import url(https://fonts.googleapis.com/css?family=Lato:300,400,700);
     

        body {
            background: #fb887c;
            color: #fff;
            font-family: 'Lato', Arial, sans-serif;
        }

        h1 {
            font-family: "proxima-nova",sans-serif;
            letter-spacing: -0.01em;
            font-weight: 700;
            font-style: normal;
            font-size: 60px;
            margin-left: -3px;
            line-height: 1em;
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
            text-rendering: optimizeLegibility;
        }

        table {
            width: 80%;
            margin: auto;
        }

        table, th, td {
            border: 1px solid #fff;
            border-collapse: collapse;
        }

        th, td {
            padding: 15px;
        }"""

@app.route("/")
def hello_world():

    # return 'Hello, World!'
    return "<style>"+css+"</style>" + tbbt.get()


if __name__ == "__main__":
    app.run()
