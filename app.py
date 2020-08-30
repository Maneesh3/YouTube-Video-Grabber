from flask import Flask, render_template
from YT_VideoGrabber.video_grabber import *
import json
app = Flask(__name__)

app.secret_key = 'Th1s_15_Ma_53cr3t_80i5'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def base():
	return render_template('base.html')

@app.route("/", methods=['POST'])
def base_get():
	chann=latestVideoGrab()
	return render_template('base_get.html',channelUpdates=chann)

if __name__=="__main__":
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(port=5000)
