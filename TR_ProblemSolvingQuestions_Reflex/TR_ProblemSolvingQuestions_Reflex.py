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
        rx.button("Next Question", on_click=lambda: rx.redirect("/question-1")),
        direction="column",
        spacing="4",
    )


def question_1() -> rx.Component:
    return rx.center(
        rx.heading(
            "Question 1",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.button("Next Question", on_click=lambda: rx.redirect("/question-1")),
        direction="column",
        spacing="4",
    )


app = rx.App()
app.add_page(home, "/")
app.add_page(problem, "/problem")
app.add_page(question_1, "/question-1")
