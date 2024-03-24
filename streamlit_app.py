import streamlit as st

from tornado.web import RequestHandler
from injectApi import CustomRule, init_global_tornado_hook, uninitialize_global_tornado_hook

class HelloWorldHandler(RequestHandler):
    def get(self):
        self.write({
            "text": "Hello World"
        })

enable_rest = st.checkbox("Enable REST API", value=True)

if enable_rest:
    # http://localhost:8501/hello -> {"text": "Hello World"}
    init_global_tornado_hook([CustomRule("/hello", HelloWorldHandler)])
else:
    uninitialize_global_tornado_hook()
