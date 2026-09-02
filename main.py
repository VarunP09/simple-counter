from drafter import *
from dataclasses import dataclass


set_website_title("Counter")

set_site_information(
    author="Varun Pappu",
    description="A simple counter",
    sources="Thanks to the Drafter docs",
    planning="N/A",
    links=["https://github.com/your-username/your-repository"]
)

set_website_framed(False)

@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    return Page(state, [
        "Current count: " + str(state.count) + "\n",
        Button("+1", "increment"),
        Button("-1", "decrement"),
        Button("+5", "plusFive"),
        Button("Reset", "reset_count")
    ])


@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)

@route
def decrement(state: State) -> Page:
    if(state.count > 0):
        state.count = state.count - 1
    return index(state)

@route
def plusFive(state: State) -> Page:
    state.count = state.count + 5
    return index(state)


@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)


assert_state(increment(State(0)), State(1))
assert_state(reset_count(State(7)), State(0))
assert_has(index(State(3)), "Current count: 3")

hide_debug_information()

start_server(State(5))
