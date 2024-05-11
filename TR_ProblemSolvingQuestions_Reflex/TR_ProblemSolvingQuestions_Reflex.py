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
        # id=f"{id}",
        name=f"{name}",
        color_scheme="amber",
        radius="medium",
        required=True,
        size="3",
        # value=id.text,
        # on_change=TextAreasState.set_text,
    )


# ===================================================================
# STATE of the APP
# ===================================================================
class TextAreasState(rx.State):
    """The app state."""

    problem_text: str = ""
    question_1_text: str = ""
    question_2_text: str = ""
    question_3_text: str = ""
    question_4_text: str = ""
    question_5_text: str = ""

    def set_text_problem_text(self, new_text: str):
        self.problem_text = new_text

    def set_text_question_1_text(self, new_text: str):
        self.question_1_text = new_text

    def set_text_question_2_text(self, new_text: str):
        self.question_2_text = new_text

    def set_text_question_3_text(self, new_text: str):
        self.question_3_text = new_text

    def set_text_question_4_text(self, new_text: str):
        self.question_4_text = new_text

    def set_text_question_5_text(self, new_text: str):
        self.question_5_text = new_text


# ===================================================================
# "/" HOME Page
# ===================================================================


def home() -> rx.Component:
    return rx.flex(
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
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="6",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# PROBLEM Page
# ===================================================================
def problem() -> rx.Component:
    return rx.flex(
        rx.heading(
            "What is the problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        # user_answer_entry(id="problem", name="problem"),
        rx.text_area(
            value=TextAreasState.problem_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_problem_text,
        ),
        next_button(goto="question-1"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Question 1 Page
# ===================================================================
def question_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            rx.text("I.", color_scheme="red"),
            "What is great about this problem?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.text_area(
            value=TextAreasState.question_1_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_question_1_text,
        ),
        next_button(goto="question-2"),
        previous_button(goto="problem"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Question 2 Page
# ===================================================================
def question_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            rx.text("II.", color_scheme="red"),
            "What is not perfect yet?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.text_area(
            value=TextAreasState.question_2_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_question_2_text,
        ),
        next_button(goto="question-3"),
        previous_button(goto="question-1"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Question 3 Page
# ===================================================================
def question_3() -> rx.Component:
    return rx.flex(
        rx.heading(
            rx.text("III.", color_scheme="red"),
            "What am I willing to do to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.text_area(
            value=TextAreasState.question_3_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_question_3_text,
        ),
        next_button(goto="question-4"),
        previous_button(goto="question-2"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Question 4 Page
# ===================================================================
def question_4() -> rx.Component:
    return rx.flex(
        rx.heading(
            rx.text("IV.", color_scheme="red"),
            "What am I willing to no longer do in order to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.text_area(
            value=TextAreasState.question_4_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_question_4_text,
        ),
        next_button(goto="question-5"),
        previous_button(goto="question-3"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Question 5 Page
# ===================================================================
def question_5() -> rx.Component:
    return rx.flex(
        rx.heading(
            rx.text("V.", color_scheme="red"),
            "How can I enjoy the process while I do what is necessary to make it the way I want it?",
            size="8",
            color_scheme="amber",
            align="center",
        ),
        rx.text_area(
            value=TextAreasState.question_5_text,  # Bind the text area value to the state variable
            on_change=TextAreasState.set_text_question_5_text,
        ),
        next_button(goto="summary"),
        previous_button(goto="question-4"),
        # -----------------
        # flex properties
        # -----------------
        direction="column",
        spacing="4",
        justify_content="center",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


# ===================================================================
# Summary Page
# ===================================================================
def summary() -> rx.Component:
    return rx.flex(
        rx.heading(
            "SUMMARY",
            size="8",
            color_scheme="bronze",
            align="center",
        ),
        # ====== PROBLEMS AND ANSWERS =======
        rx.markdown("# PROBLEM:", class_name="text-red-800"),
        rx.text(TextAreasState.problem_text),
        rx.markdown(
            "### What is great about this problem?:", class_name="text-amber-600"
        ),
        rx.text(TextAreasState.question_1_text),
        rx.markdown("### What is not perfect yet?:", class_name="text-amber-600"),
        rx.text(TextAreasState.question_2_text),
        rx.markdown(
            "### What am I willing to do to make it the way I want it?:",
            class_name="text-amber-600",
        ),
        rx.text(TextAreasState.question_3_text),
        rx.markdown(
            "### What am I willing to no longer do in order to make it the way I want it?:",
            class_name="text-amber-600",
        ),
        rx.text(TextAreasState.question_4_text),
        rx.markdown(
            "### How can I enjoy the process while I do what is necessary to make it the way I want it?:",
            class_name="text-amber-600",
        ),
        rx.text(TextAreasState.question_5_text),
        # ====== Buttons =======
        previous_button(goto="question-5"),
        rx.button(
            "Save answers",
            size="2",
            color_scheme="blue",
            # on_click=...,
        ),
        # ====== FLEX PROPERTIES =======
        direction="column",
        spacing="3",
        justify_content="center",
        class_name="p-10",
        align_items="center",
        height="100vh",  # Use viewport height to fill the screen vertically
        width="100vw",
    )


app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        radius="large",
        accent_color="gold",
    )
)
app.add_page(home, "/")
app.add_page(problem, "/problem")
app.add_page(question_1, "/question-1")
app.add_page(question_2, "/question-2")
app.add_page(question_3, "/question-3")
app.add_page(question_4, "/question-4")
app.add_page(question_5, "/question-5")
app.add_page(summary, "/summary")
