import reflex as rx
from app.states.workspace_state import WorkspaceState, Activity, User
from app.components.task_dialog import new_task_dialog
from app.components.analytics import analytics_section, upcoming_deadlines_card


def metric_card(
    icon: str, label: str, value: rx.Var | str, sub: str, color: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name="h-5 w-5"),
                class_name=f"h-10 w-10 rounded-lg flex items-center justify-center {color}",
            ),
            rx.el.span(sub, class_name="text-xs font-medium text-gray-500"),
            class_name="flex items-center justify-between",
        ),
        rx.el.p(value, class_name="text-3xl font-bold text-gray-900 mt-4"),
        rx.el.p(label, class_name="text-sm text-gray-500 mt-1"),
        class_name="bg-white border border-gray-200 rounded-xl p-5 hover:border-indigo-200 transition-colors",
    )


def quick_action(icon: str, label: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, class_name="h-4 w-4 text-indigo-600"),
            class_name="h-8 w-8 rounded-lg bg-indigo-50 flex items-center justify-center",
        ),
        rx.el.span(label, class_name="text-sm font-medium text-gray-800"),
        rx.icon("chevron-right", class_name="h-4 w-4 text-gray-400 ml-auto"),
        href=href,
        class_name="flex items-center gap-3 p-3 rounded-lg border border-gray-200 hover:border-indigo-300 hover:bg-indigo-50/30 transition-colors",
    )


def quick_action_button(icon: str, label: str, on_click) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.icon(icon, class_name="h-4 w-4 text-indigo-600"),
            class_name="h-8 w-8 rounded-lg bg-indigo-50 flex items-center justify-center",
        ),
        rx.el.span(label, class_name="text-sm font-medium text-gray-800"),
        rx.icon("chevron-right", class_name="h-4 w-4 text-gray-400 ml-auto"),
        on_click=on_click,
        type="button",
        class_name="w-full flex items-center gap-3 p-3 rounded-lg border border-gray-200 hover:border-indigo-300 hover:bg-indigo-50/30 transition-colors text-left",
    )


def activity_row(a: Activity) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="https://api.dicebear.com/9.x/notionists/svg?seed="
            + a["user_id"],
            class_name="h-9 w-9 rounded-full bg-gray-100 shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                rx.el.span(
                    WorkspaceState.user_map[a["user_id"]],
                    class_name="font-semibold text-gray-900",
                ),
                " ",
                rx.el.span(a["action"], class_name="text-gray-600"),
                " ",
                rx.el.span(
                    a["target"], class_name="font-medium text-indigo-600"
                ),
                class_name="text-sm",
            ),
            rx.el.p(a["timestamp"], class_name="text-xs text-gray-400 mt-0.5"),
        ),
        class_name="flex items-start gap-3 py-3",
    )


def project_progress_row(p: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    class_name=p["color"].to_string()
                    + " h-2.5 w-2.5 rounded-full"
                ),
                rx.el.p(
                    p["name"], class_name="text-sm font-semibold text-gray-900"
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.p(
                p["done"].to_string() + "/" + p["total"].to_string() + " tasks",
                class_name="text-xs text-gray-500",
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-full bg-indigo-600 rounded-full",
                style={"width": p["pct"].to_string() + "%"},
            ),
            class_name="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden",
        ),
        rx.el.p(
            p["pct"].to_string() + "% complete",
            class_name="text-xs text-gray-400 mt-2",
        ),
        href="/board/" + p["id"].to_string(),
        class_name="block p-4 rounded-lg border border-gray-200 hover:border-indigo-300 hover:bg-gray-50/50 transition-colors",
    )


def team_member(u: User) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="https://api.dicebear.com/9.x/notionists/svg?seed="
            + u["avatar_seed"],
            class_name="h-10 w-10 rounded-full bg-gray-100",
        ),
        rx.el.div(
            rx.el.p(
                u["name"], class_name="text-sm font-semibold text-gray-900"
            ),
            rx.el.p(u["role"], class_name="text-xs text-gray-500"),
        ),
        rx.el.div(
            rx.el.span(class_name="h-2 w-2 rounded-full bg-emerald-500"),
            class_name="ml-auto",
        ),
        class_name="flex items-center gap-3 py-2.5",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        new_task_dialog(),
        rx.el.div(
            metric_card(
                "circle_check",
                "Total Tasks",
                WorkspaceState.total_tasks,
                "All time",
                "bg-indigo-50 text-indigo-600",
            ),
            metric_card(
                "loader",
                "In Progress",
                WorkspaceState.in_progress_count,
                "Active",
                "bg-amber-50 text-amber-600",
            ),
            metric_card(
                "check",
                "Completed",
                WorkspaceState.completed_tasks,
                f"{WorkspaceState.completion_rate}% done",
                "bg-emerald-50 text-emerald-600",
            ),
            metric_card(
                "triangle_alert",
                "High Priority",
                WorkspaceState.overdue_count,
                "Needs attention",
                "bg-rose-50 text-rose-600",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Project Progress",
                            class_name="text-lg font-semibold text-gray-900",
                        ),
                        rx.el.p(
                            "Track completion across all active projects",
                            class_name="text-sm text-gray-500 mt-0.5",
                        ),
                    ),
                    rx.el.a(
                        "View all",
                        href="/",
                        class_name="text-sm font-medium text-indigo-600 hover:text-indigo-700",
                    ),
                    class_name="flex items-center justify-between mb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        WorkspaceState.project_task_counts, project_progress_row
                    ),
                    class_name="flex flex-col gap-3",
                ),
                class_name="bg-white border border-gray-200 rounded-xl p-6",
            ),
            rx.el.div(
                rx.el.h2(
                    "Quick Actions",
                    class_name="text-lg font-semibold text-gray-900 mb-4",
                ),
                rx.el.div(
                    rx.el.div(
                        quick_action_button(
                            "circle_plus",
                            "Create new task",
                            WorkspaceState.open_new_task,
                        ),
                        quick_action("folder-plus", "Start a project", "/team"),
                        quick_action("user-plus", "Invite teammate", "/team"),
                        quick_action("calendar", "Schedule meeting", "/team"),
                        class_name="flex flex-col gap-2",
                    ),
                    class_name="bg-white border border-gray-200 rounded-xl p-6",
                ),
                class_name="bg-white border border-gray-200 rounded-xl p-6",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mt-4",
            style={"grid-template-columns": "2fr 1fr"},
        ),
        analytics_section(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Recent Activity",
                            class_name="text-lg font-semibold text-gray-900",
                        ),
                        rx.el.p(
                            "Latest updates from your team",
                            class_name="text-sm text-gray-500 mt-0.5",
                        ),
                    ),
                    rx.el.span(
                        "Live",
                        class_name="text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-100 px-2 py-0.5 rounded-md ml-auto",
                    ),
                    class_name="flex items-start mb-2",
                ),
                rx.el.div(
                    rx.foreach(WorkspaceState.activities, activity_row),
                    class_name="divide-y divide-gray-100 max-h-96 overflow-y-auto",
                ),
                class_name="bg-white border border-gray-200 rounded-xl p-6",
            ),
            upcoming_deadlines_card(),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Team", class_name="text-lg font-semibold text-gray-900"
                ),
                rx.el.p(
                    f"{WorkspaceState.team_size} members online",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
                class_name="mb-2",
            ),
            rx.el.div(
                rx.foreach(WorkspaceState.users, team_member),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-6 divide-y divide-gray-100 sm:divide-y-0",
            ),
            class_name="bg-white border border-gray-200 rounded-xl p-6 mt-4",
        ),
        class_name="p-4 sm:p-6",
    )
