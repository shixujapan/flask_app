from flask import Blueprint, render_template
from common.models.user import User

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    name = "hello"
    context = {"name": name}
    context["user"] = {"nickname": "xxxx",
                       "id": "xxxxx", "home_page": "http://www.xxx"}
    context["num_list"] = [1, 2, 3, 4, 5]

    result = User.query.all()
    context['result'] = result

    return render_template("index.html", **context)
