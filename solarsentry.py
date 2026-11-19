import reflex as rx
from .home import home
from .input1 import input1, input1State
from .input2 import input2, input2State
from .choice import choice, choiceState
from .buy import buy, buyState
from .lease import lease, leaseState
from .scam import scam, scamState


app = rx.App()
app.add_page(home, route="/")
app.add_page(input1, route="/input1")
app.add_page(input2, route="/input2")
app.add_page(choice, route="/choice", on_load=choiceState.get_vars)
app.add_page(buy, route="/buy", on_load=buyState.get_var)
app.add_page(lease, route="/lease", on_load=leaseState.get_var)
app.add_page(scam, route="/scam", on_load=scamState.get_var)