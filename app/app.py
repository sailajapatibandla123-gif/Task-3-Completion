import reflex as rx
from app.states.workspace_state import WorkspaceState
from app.states.auth_state import AuthState
from app.components.sidebar import sidebar
from app.components.topbar import topbar
from app.components.dashboard import dashboard
from app.components.board import board
from app.components.team import team_page
from app.components.auth import auth_page


def shell(title: str, subtitle: str, content: rx.Component) -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        rx.el.div(
            sidebar(),
            rx.el.div(
                topbar(title, subtitle),
                content,
                class_name="flex-1 min-w-0",
            ),
            class_name="flex min-h-screen bg-gray-50 font-['Inter']",
        ),
        auth_page(),
    )


def index() -> rx.Component:
    return shell(
        "Workspace Overview",
        "Welcome back. Here's what's happening across your projects today.",
        dashboard(),
    )


def board_page() -> rx.Component:
    return shell(
        "Project Board",
        "Organize, assign, and track tasks in a visual Kanban workflow.",
        board(),
    )


def team() -> rx.Component:
    return shell(
        "Team & Projects",
        "Manage members, group projects, roles, and workload visibility.",
        team_page(),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    board_page,
    route="/board/[project_id]",
    on_load=WorkspaceState.select_project(
        rx.State.router.page.params["project_id"]
    ),
)
app.add_page(team, route="/team")
app.add_page(index, route="/")
