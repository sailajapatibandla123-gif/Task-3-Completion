import reflex as rx
from app.states.workspace_state import WorkspaceState, Project
from app.states.auth_state import AuthState


def nav_link(
    icon: str, label: str, href: str, active: bool = False
) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-4 w-4"),
        rx.el.span(label, class_name="text-sm font-medium"),
        href=href,
        on_click=WorkspaceState.close_mobile_sidebar,
        class_name="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-700 hover:bg-indigo-50 hover:text-indigo-700 transition-colors",
    )


def project_link(p: Project) -> rx.Component:
    return rx.el.a(
        rx.el.span(class_name=p["color"] + " h-2 w-2 rounded-full shrink-0"),
        rx.el.span(p["name"], class_name="text-sm font-medium truncate"),
        href=f"/board/{p['id']}",
        on_click=WorkspaceState.close_mobile_sidebar,
        class_name="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-gray-900 transition-colors",
    )


def _sidebar_body() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("square_kanban", class_name="h-5 w-5 text-white"),
                    class_name="h-9 w-9 rounded-lg bg-indigo-600 flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.p(
                        "CodeAlpha",
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p("Project Hub", class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3 px-4 py-5 border-b border-gray-200",
            ),
            rx.el.nav(
                rx.el.p(
                    "WORKSPACE",
                    class_name="text-xs font-semibold text-gray-400 tracking-wider px-3 mb-2",
                ),
                nav_link("layout-dashboard", "Dashboard", "/"),
                nav_link("square_check", "My Tasks", "/board/p1"),
                nav_link("users", "Team", "/team"),
                nav_link("bell", "Notifications", "/team"),
                nav_link("settings", "Settings", "/team"),
                class_name="flex flex-col gap-1 px-3 py-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "PROJECTS",
                        class_name="text-xs font-semibold text-gray-400 tracking-wider",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="h-3.5 w-3.5"),
                        class_name="text-gray-400 hover:text-indigo-600",
                    ),
                    class_name="flex items-center justify-between px-3 mb-2",
                ),
                rx.el.div(
                    rx.foreach(WorkspaceState.projects, project_link),
                    class_name="flex flex-col gap-1 px-3",
                ),
                class_name="py-4 border-t border-gray-200",
            ),
            class_name="flex flex-col flex-1 overflow-y-auto",
        ),
        rx.el.div(
            rx.el.img(
                src="https://api.dicebear.com/9.x/notionists/svg?seed="
                + AuthState.user_email,
                class_name="h-9 w-9 rounded-full bg-gray-100",
            ),
            rx.el.div(
                rx.el.p(
                    AuthState.user_name,
                    class_name="text-sm font-semibold text-gray-900 truncate",
                ),
                rx.el.p(
                    AuthState.user_role,
                    class_name="text-xs text-gray-500 truncate",
                ),
                class_name="min-w-0 flex-1",
            ),
            rx.el.button(
                rx.icon("log-out", class_name="h-4 w-4"),
                on_click=AuthState.logout,
                type="button",
                title="Sign out",
                class_name="p-1.5 rounded-md text-gray-400 hover:text-rose-600 hover:bg-rose-50",
            ),
            class_name="flex items-center gap-3 px-4 py-4 border-t border-gray-200",
        ),
        class_name="flex flex-col h-full w-full bg-white",
    )


def sidebar() -> rx.Component:
    return rx.fragment(
        rx.el.aside(
            _sidebar_body(),
            class_name="hidden lg:flex flex-col w-64 h-screen bg-white border-r border-gray-200 sticky top-0 shrink-0",
        ),
        rx.cond(
            WorkspaceState.show_mobile_sidebar,
            rx.el.div(
                rx.el.div(
                    on_click=WorkspaceState.close_mobile_sidebar,
                    class_name="fixed inset-0 bg-black/40 backdrop-blur-sm z-40 lg:hidden",
                ),
                rx.el.aside(
                    _sidebar_body(),
                    class_name="fixed left-0 top-0 flex flex-col w-64 h-screen bg-white border-r border-gray-200 z-50 lg:hidden shadow-xl",
                ),
            ),
            rx.fragment(),
        ),
    )
