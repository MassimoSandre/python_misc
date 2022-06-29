import csv

file = open('words.csv', encoding="utf8")

csvreader = csv.reader(file)

header = []

header = next(csvreader)

content = []
for row in csvreader:
    content.append(row)



code = """
<html>
    <head>
        <style>
            @import 'https://fonts.googleapis.com/css?family=Lily+Script+One';
            body {
            background: #eee;
            font-family: 'Lily Script One';
            }

            .card {
            
            top: 50%;
            left: 50%;
            width: 350px;
            height: 350px;
            margin: 50px;
            float: left;
            perspective: 500px;
            }

            .content {
            position: absolute;
            width: 100%;
            height: 100%;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);

            transition: transform 1s;
            transform-style: preserve-3d;
            }

            .card:hover .content {
            transform: rotateY( 180deg ) ;
            transition: transform 0.5s;
            }

            .front,
            .back {
            position: absolute;
            height: 100%;
            width: 100%;
            background: white;
            line-height: 150px;
            color: #03446A;
            text-align: center;
            font-size: 60px;
            border-radius: 5px;
            backface-visibility: hidden;
            }

            .back {
            background: #03446A;
            color: white;
            transform: rotateY( 180deg );
            }
        </style>
    </head>
    <body>
"""

for word in content:
    code = code + """
        <div class="card">
            <div class="content">
                <div class="front">"""
    code = code + word[0]
    code = code+ """
                </div>
                <div class="back">
                """
    code = code + word[2]
    code = code+ """
                </div>
            </div>
        </div>
    """

code = code + "</body></head>"

output_file = open("japanese_to_italian.html", "w", encoding="utf8")

output_file.write(code)

output_file.close()

code = """
<html>
    <head>
        <style>
            @import 'https://fonts.googleapis.com/css?family=Lily+Script+One';
            body {
            background: #eee;
            font-family: 'Lily Script One';
            }

            .card {
            
            top: 50%;
            left: 50%;
            width: 350px;
            height: 350px;
            margin: 50px;
            float: left;
            perspective: 500px;
            }

            .content {
            position: absolute;
            width: 100%;
            height: 100%;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);

            transition: transform 1s;
            transform-style: preserve-3d;
            }

            .card:hover .content {
            transform: rotateY( 180deg ) ;
            transition: transform 0.5s;
            }

            .front,
            .back {
            position: absolute;
            height: 100%;
            width: 100%;
            background: white;
            line-height: 150px;
            color: #03446A;
            text-align: center;
            font-size: 60px;
            border-radius: 5px;
            backface-visibility: hidden;
            }

            .back {
            background: #03446A;
            color: white;
            transform: rotateY( 180deg );
            }
        </style>
    </head>
    <body>
"""

for word in content:
    code = code + """
        <div class="card">
            <div class="content">
                <div class="front">"""
    code = code + word[2]
    code = code+ """
                </div>
                <div class="back">
                """
    code = code + word[0]
    code = code+ """
                </div>
            </div>
        </div>
    """

code = code + "</body></head>"


output_file = open("italian_to_japanese.html", "w", encoding="utf8")

output_file.write(code)

output_file.close()