import reflex as rx
from app.states.workspace_state import WorkspaceState


def status_chart() -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.recharts.graphing_tooltip(),
        rx.recharts.bar(
            data_key="count",
            fill="#6366f1",
            radius=6,
        ),
        rx.recharts.x_axis(
            data_key="status",
            tick_line=False,
            axis_line=False,
            custom_attrs={"fontSize": "11px"},
        ),
        rx.recharts.y_axis(
            tick_line=False,
            axis_line=False,
            custom_attrs={"fontSize": "11px"},
        ),
        data=WorkspaceState.status_distribution,
        width="100%",
        height=220,
        margin={"top": 10, "right": 10, "left": -20, "bottom": 0},
    )


def weekly_chart() -> rx.Component:
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.recharts.graphing_tooltip(),
        rx.recharts.area(
            data_key="completed",
            stroke="#10b981",
            fill="#10b981",
            fill_opacity=0.2,
            type_="monotone",
        ),
        rx.recharts.area(
            data_key="created",
            stroke="#6366f1",
            fill="#6366f1",
            fill_opacity=0.15,
            type_="monotone",
        ),
        rx.recharts.x_axis(
            data_key="day",
            tick_line=False,
            axis_line=False,
            custom_attrs={"fontSize": "11px"},
        ),
        rx.recharts.y_axis(
            tick_line=False,
            axis_line=False,
            custom_attrs={"fontSize": "11px"},
        ),
        data=WorkspaceState.weekly_activity,
        width="100%",
        height=220,
        margin={"top": 10, "right": 10, "left": -20, "bottom": 0},
    )


def priority_row(p: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                class_name="h-2.5 w-2.5 rounded-full",
                style={"background-color": p["fill"]},
            ),
            rx.el.p(
                p["priority"],
                class_name="text-sm font-medium text-gray-800",
            ),
            class_name="flex items-center gap-2",
        ),
        rx.el.p(
            p["count"].to_string() + " tasks",
            class_name="text-sm font-semibold text-gray-900 ml-auto",
        ),
        class_name="flex items-center gap-2 py-2",
    )


def deadline_row(t: dict) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.p(
                t["title"],
                class_name="text-sm font-semibold text-gray-900 truncate",
            ),
            rx.el.div(
                rx.icon("calendar", class_name="h-3 w-3 text-gray-400"),
                rx.el.span(t["due_date"], class_name="text-xs text-gray-500"),
                rx.el.span("•", class_name="text-gray-300"),
                rx.el.span(
                    t["priority"],
                    class_name=rx.match(
                        t["priority"],
                        ("High", "text-xs font-semibold text-rose-600"),
                        ("Medium", "text-xs font-semibold text-amber-600"),
                        ("Low", "text-xs font-semibold text-emerald-600"),
                        "text-xs text-gray-500",
                    ),
                ),
                class_name="flex items-center gap-1.5 mt-1",
            ),
            class_name="flex-1 min-w-0 text-left",
        ),
        rx.el.img(
            src="https://api.dicebear.com/9.x/notionists/svg?seed="
            + t["assignee_id"],
            class_name="h-7 w-7 rounded-full bg-gray-100 shrink-0",
        ),
        type="button",
        on_click=WorkspaceState.open_task(t["id"]),
        class_name="w-full flex items-center gap-3 p-2.5 rounded-lg border border-gray-100 hover:border-indigo-200 hover:bg-indigo-50/30 transition-colors",
    )


def analytics_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Tasks by Status",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.p(
                    "Distribution across the workflow",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
                class_name="mb-3",
            ),
            status_chart(),
            class_name="bg-white border border-gray-200 rounded-xl p-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Weekly Activity",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.p(
                    "Tasks created vs completed",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
                class_name="mb-3",
            ),
            weekly_chart(),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        class_name="h-2 w-2 rounded-full bg-emerald-500"
                    ),
                    rx.el.span("Completed", class_name="text-xs text-gray-600"),
                    class_name="flex items-center gap-1.5",
                ),
                rx.el.div(
                    rx.el.span(class_name="h-2 w-2 rounded-full bg-indigo-500"),
                    rx.el.span("Created", class_name="text-xs text-gray-600"),
                    class_name="flex items-center gap-1.5",
                ),
                class_name="flex items-center gap-4 mt-2",
            ),
            class_name="bg-white border border-gray-200 rounded-xl p-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Priority Mix",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.p(
                    "How urgent is the current pipeline",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
                class_name="mb-2",
            ),
            rx.el.div(
                rx.foreach(WorkspaceState.priority_distribution, priority_row),
                class_name="divide-y divide-gray-100",
            ),
            class_name="bg-white border border-gray-200 rounded-xl p-6",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mt-4",
    )


def upcoming_deadlines_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Upcoming Deadlines",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.p(
                    "Next tasks due across your workspace",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
            ),
            rx.icon(
                "calendar_clock", class_name="h-5 w-5 text-indigo-500 ml-auto"
            ),
            class_name="flex items-start mb-4",
        ),
        rx.cond(
            WorkspaceState.upcoming_deadlines.length() > 0,
            rx.el.div(
                rx.foreach(WorkspaceState.upcoming_deadlines, deadline_row),
                class_name="flex flex-col gap-2",
            ),
            rx.el.p(
                "No upcoming deadlines. Nice work!",
                class_name="text-sm text-gray-400",
            ),
        ),
        class_name="bg-white border border-gray-200 rounded-xl p-6",
    )
