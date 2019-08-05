from flask import Flask, render_template
import random

def create_app ():
    app = Flask(__name__)

    @app.route("/")
    def start():
        return render_template('template.html', my_string="Hi! That's DICE ROLLER by myself, "
                                                          "go home for more and enjoy :-)", title='Small dice roller')

    @app.route("/home")
    def home():
        return render_template(
            'template.html', my_string="A traditional die "
                                       "is a cube with each of its "
                                       "six faces marked with a "
                                       "different number of dots (pips) "
                                       "from one to six. When thrown or"
                                       " rolled, the die comes to rest "
                                       "showing on its upper surface a "
                                       "random integer from one to six,"
                                       " each value being equally likely. Go to ROLL and try it by yourself!",
                                        title="Home")

    @app.route("/roll")
    def roll():
        nowy = random.randint(1, 6)
        return render_template('rolltemp.html', my_string="The devil leads him by the nose "
                                                          "who the dice too "
                                                          "often throws. Have fun!", points=nowy, title='Roll')

    @app.route("/about")
    def about():
        return render_template(
            'template.html', my_string="It is small and simple web application. It takes a few days to understand how to use well templates, routings "
                                       "and etc., but im "
                                       "proud of myself that at least "
                                       "I can do something like that. I used sites like: "
                                       "realpython.com / tutorial.djangogirls.org / alicja.it / code.tutsplus.com.", title="About")

    @app.route("/contact")
    def contact():
        return render_template(
            'template.html', my_string="If something is wrong you "
                                       "can contact me by e-mail: zxcvmarcin1@wp.pl", title="Contact Me")


    return app

create_app().run()