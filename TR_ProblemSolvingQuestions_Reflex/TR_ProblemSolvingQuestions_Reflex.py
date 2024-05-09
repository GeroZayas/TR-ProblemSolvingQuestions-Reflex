"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx


class State(rx.State):
    """The app state."""


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


def problem() -> rx.Component:
    return rx.center(
        rx.heading(
            "What is the problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/question-1"),
        ),
        direction="column",
        spacing="4",
    )


def question_1() -> rx.Component:
    return rx.center(
        rx.heading(
            "I. What is great about this problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/question-2"),
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/problem"),
        ),
        direction="column",
        spacing="4",
    )


def question_2() -> rx.Component:
    return rx.center(
        rx.heading(
            "II. What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/question-3"),
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/question-1"),
        ),
        direction="column",
        spacing="4",
    )


def question_3() -> rx.Component:
    return rx.center(
        rx.heading(
            "II. What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/question-4"),
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/question-2"),
        ),
        direction="column",
        spacing="4",
    )


def question_4() -> rx.Component:
    return rx.center(
        rx.heading(
            "II. What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/question-5"),
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/question-3"),
        ),
        direction="column",
        spacing="4",
    )


def question_5() -> rx.Component:
    return rx.center(
        rx.heading(
            "II. What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Next Question",
            size="3",
            color_scheme="amber",
            on_click=lambda: rx.redirect("/summary"),
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/question-4"),
        ),
        direction="column",
        spacing="4",
    )


def summary() -> rx.Component:
    return rx.center(
        rx.heading(
            "SUMMARY",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button(
            "Previous Question",
            color_scheme="mint",
            on_click=lambda: rx.redirect("/question-5"),
        ),
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
