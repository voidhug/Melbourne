# coding: utf-8
from flask import request ,Flask, jsonify, Response

app = Flask(__name__)

template = u'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>canvasTest2</title>
</head>
<body>
<div>
<img width="200" height="200" src=%s>
<img width="200" height="200" src=%s>
</div>
<canvas id="canvas" style=" display:block; margin:50px auto">
    当前浏览器不支持 Canvas，请更换浏览器后再试
</canvas>
<script>
    window.onload = function() {
        var grade = %s;
        var canvas = document.getElementById("canvas");
        canvas.width  = 500;
        canvas.height = 500;
        var context = canvas.getContext("2d");
        context.fillStyle = "#e84e40";
        context.beginPath();
        context.arc(canvas.width / 2, canvas.height / 2, canvas.width / 2, 0, 2 * Math.PI);
        context.closePath();
        context.fill();

        context.font = "normal 200px/0 \\"Lucida Console\\", Monaco, monospace";
        context.fillStyle = "#ffffff";
        context.textAlign = "center";
        context.textBaseline = "middle";
        context.fillText(grade, canvas.width / 2, canvas.height / 2);
    };
</script>
</body>
</html>
'''


@app.route('/score', methods=['GET'])
def score_page():
    print request.args.get('img_user')
    print '=============='
    print request.args.get('img_url')
    return template % (request.args.get('img_user'), request.args.get('img_url'), request.args.get('grades'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
