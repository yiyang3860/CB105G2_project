from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from form import FormRegister

#  取得啟動文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置資料庫為sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(pjdir, 'data_register.sqlite')
app.config['SECRET_KEY']='your key'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form =FormRegister()
    if form.validate_on_submit():
        return 'Success Thank You'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()