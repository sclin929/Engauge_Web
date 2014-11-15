# Imports
import json

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from flask.ext.login import (current_user, login_required, \
    login_user, logout_user)
from app import app, login_manager

import firebase
