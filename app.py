from flask import Flask,render_template,request,jsonify,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 和前端约定好，发送网络请求，不管用户名和密码是否验证成功
        # 我都返回同样格式的json对象给你
        # {"code":200,"message":""}
        #传统方法和ajax如下:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            # return redirect(url_for('index.html')),传统方法
            return jsonify({"code": 200, "message": "ok,你对了"})
        else:
            # return  "用户名密码错误"，传统方法
            return jsonify({"code": 401, "message": "用户名或密码错误！请仔细检查"})




if __name__ == '__main__':
    app.run()
