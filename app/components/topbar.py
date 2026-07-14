import reflex as rx
from app.states.workspace_state import WorkspaceState
from app.states.auth_state import AuthState
from app.components.notifications import notifications_panel


def topbar(title: str, subtitle: str) -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon("menu", class_name="h-5 w-5"),
                    on_click=WorkspaceState.toggle_mobile_sidebar,
                    type="button",
                    class_name="p-2 rounded-lg text-gray-600 hover:bg-gray-100 lg:hidden",
                ),
                rx.el.div(
                    rx.el.h1(
                        title,
                        class_name="text-xl sm:text-2xl font-bold text-gray-900 tracking-tight",
                    ),
                    rx.el.p(
                        subtitle,
                        class_name="text-xs sm:text-sm text-gray-500 mt-1 hidden sm:block",
                    ),
                    class_name="min-w-0",
                ),
                class_name="flex items-center gap-3 min-w-0",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="h-4 w-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2",
                    ),
                    rx.el.input(
                        placeholder="Search tasks, projects, people...",
                        class_name="pl-10 pr-4 py-2 w-72 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-gray-800",
                    ),
                    class_name="relative hidden xl:block",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("bell", class_name="h-4 w-4"),
                        rx.cond(
                            WorkspaceState.unread_notifications_count > 0,
                            rx.el.span(
                                WorkspaceState.unread_notifications_count.to_string(),
                                class_name="absolute -top-1 -right-1 h-4 min-w-4 px-1 rounded-full bg-rose-500 text-white text-[10px] font-bold flex items-center justify-center",
                            ),
                            rx.fragment(),
                        ),
                        on_click=WorkspaceState.toggle_notifications,
                        type="button",
                        class_name="relative p-2 rounded-lg bg-white border border-gray-200 text-gray-600 hover:bg-gray-50",
                    ),
                    notifications_panel(),
                    class_name="relative",
                ),
                rx.el.img(
                    src="https://api.dicebear.com/9.x/notionists/svg?seed="
                    + AuthState.user_email,
                    class_name="h-9 w-9 rounded-full bg-gray-100 shrink-0",
                ),
                class_name="flex items-center gap-2 sm:gap-3 shrink-0",
            ),
            class_name="flex items-center justify-between gap-3",
        ),
        class_name="bg-white border-b border-gray-200 px-4 sm:px-6 py-4 sm:py-5 sticky top-0 z-20",
    )
