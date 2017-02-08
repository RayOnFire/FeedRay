from flask import Blueprint

userspace = Blueprint('userspace', __name__)

from . import views