from flask import Flask

my_awesome_app=Flask(__name__)

@my_awesome_app.route('/')
def hello_world():
	return 'hello Toby u have hustlled bro!'

if __name__ =='__main__':
	my_awesome_app.run()	