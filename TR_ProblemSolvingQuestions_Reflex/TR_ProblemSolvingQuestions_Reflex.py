"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx


# BUTTONS
def next_button(goto):
    return (
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect(f"/{goto}"),
        ),
    )


def previous_button(goto):
    return (
        rx.button(
            "Previous Question",
            size="2",
            color_scheme="red",
            on_click=lambda: rx.redirect(f"/{goto}"),
        ),
    )


def user_answer_entry(
    id,
    name,
):
    return rx.text_area(
        placeholder="Enter answer...",
        id=f"{id}",
        name=f"{name}",
        color_scheme="amber",
        radius="medium",
        required=True,
        size="3",
    )


# ===================================================================
# STATE of the APP
# ===================================================================
class State(rx.State):
    """The app state."""

    problem_text: str = ""


# ===================================================================
# "/" HOME Page
# ===================================================================


def home() -> rx.Component:
    return rx.center(
        rx.heading(
            "Problem Solving Questions",
            size="9",
            color_scheme="amber",
            align="center",
        ),
        rx.heading("by Tony Robbins", size="5", color_scheme="bronze", align="center"),
        rx.image(
            src="Tony Robbins.jpg",
            width="200px",
            height="auto",
            border_radius="15px 50px",
        ),
        rx.button(
            rx.icon(tag="notebook-pen"),
            "Start",
            on_click=lambda: rx.redirect("/problem"),
            color_scheme="amber",
            size="3",
        ),
        rx.link("Made by Gero Zayas", href="https://www.gerozayas.com"),
        direction="column",
        spacing="6",
    )


# ===================================================================
# PROBLEM Page
# ===================================================================
def problem() -> rx.Component:
    return rx.center(
        rx.heading(
            "What is the problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="problem", name="problem"),
        next_button(goto="question-1"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Question 1 Page
# ===================================================================
def question_1() -> rx.Component:
    return rx.center(
        rx.heading(
            rx.text("I.", color_scheme="red"),
            "What is great about this problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="question_1", name="question_1"),
        next_button(goto="question-2"),
        previous_button(goto="problem"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Question 2 Page
# ===================================================================
def question_2() -> rx.Component:
    return rx.center(
        rx.heading(
            rx.text("II.", color_scheme="red"),
            "What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="question_2", name="question_2"),
        next_button(goto="question-3"),
        previous_button(goto="question-1"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Question 3 Page
# ===================================================================
def question_3() -> rx.Component:
    return rx.center(
        rx.heading(
            rx.text("III.", color_scheme="red"),
            "What am I willing to do to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="question_3", name="question_3"),
        next_button(goto="question-4"),
        previous_button(goto="question-2"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Question 4 Page
# ===================================================================
def question_4() -> rx.Component:
    return rx.center(
        rx.heading(
            rx.text("IV.", color_scheme="red"),
            "What am I willing to no longer do in order to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="question_4", name="question_4"),
        next_button(goto="question-5"),
        previous_button(goto="question-3"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Question 5 Page
# ===================================================================
def question_5() -> rx.Component:
    return rx.center(
        rx.heading(
            rx.text("V.", color_scheme="red"),
            "How can I enjoy the process while I do what is necessary to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        user_answer_entry(id="question_5", name="question_5"),
        next_button(goto="summary"),
        previous_button(goto="question-4"),
        direction="column",
        spacing="4",
    )


# ===================================================================
# Summary Page
# ===================================================================
def summary() -> rx.Component:
    return rx.center(
        rx.heading(
            "SUMMARY",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        previous_button(goto="question-5"),
        direction="column",
        spacing="4",
    )


app = rx.App()
app.add_page(home, "/")
app.add_page(problem, "/problem")
app.add_page(question_1, "/question-1")
app.add_page(question_2, "/question-2")
app.add_page(question_3, "/question-3")
app.add_page(question_4, "/question-4")
app.add_page(question_5, "/question-5")
app.add_page(summary, "/summary")
