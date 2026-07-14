import reflex as rx
from app.states.workspace_state import WorkspaceState, Task
from app.components.task_dialog import task_dialog, new_task_dialog


def priority_badge(priority: rx.Var) -> rx.Component:
    return rx.el.span(
        priority,
        class_name=rx.match(
            priority,
            (
                "High",
                "text-xs font-semibold px-2 py-0.5 rounded-md bg-rose-50 text-rose-700 border border-rose-100",
            ),
            (
                "Medium",
                "text-xs font-semibold px-2 py-0.5 rounded-md bg-amber-50 text-amber-700 border border-amber-100",
            ),
            (
                "Low",
                "text-xs font-semibold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-100",
            ),
            "text-xs font-semibold px-2 py-0.5 rounded-md bg-gray-100 text-gray-700",
        ),
    )


def task_tag(tag: rx.Var) -> rx.Component:
    return rx.el.span(
        "#" + tag,
        class_name="text-xs font-medium px-2 py-0.5 rounded-md bg-gray-100 text-gray-600",
    )


def task_card(task: Task) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            priority_badge(task["priority"]),
            rx.el.button(
                rx.icon("ellipsis", class_name="h-4 w-4"),
                class_name="text-gray-400 hover:text-gray-600 ml-auto",
                type="button",
            ),
            class_name="flex items-center gap-2 mb-2",
        ),
        rx.el.p(
            task["title"],
            class_name="text-sm font-semibold text-gray-900 leading-snug",
        ),
        rx.el.p(
            task["description"],
            class_name="text-xs text-gray-500 mt-1 line-clamp-2",
        ),
        rx.el.div(
            rx.foreach(task["tags"], task_tag),
            class_name="flex flex-wrap gap-1.5 mt-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-indigo-500 rounded-full",
                    style={"width": task["progress"].to_string() + "%"},
                ),
                class_name="h-1 w-full bg-gray-100 rounded-full overflow-hidden",
            ),
            rx.el.p(
                task["progress"].to_string() + "%",
                class_name="text-xs font-medium text-gray-500 mt-1",
            ),
            class_name="mt-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("calendar", class_name="h-3.5 w-3.5 text-gray-400"),
                rx.el.span(
                    task["due_date"], class_name="text-xs text-gray-500"
                ),
                class_name="flex items-center gap-1.5",
            ),
            rx.el.img(
                src="https://api.dicebear.com/9.x/notionists/svg?seed="
                + task["assignee_id"],
                class_name="h-6 w-6 rounded-full bg-gray-100 ml-auto",
            ),
            class_name="flex items-center gap-2 mt-3 pt-3 border-t border-gray-100",
        ),
        on_click=WorkspaceState.open_task(task["id"]),
        class_name="bg-white border border-gray-200 rounded-lg p-3.5 hover:border-indigo-300 hover:shadow-sm transition-all cursor-pointer",
    )


def column(
    title: str, count: rx.Var, dot_color: str, tasks: rx.Var
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(class_name=f"h-2 w-2 rounded-full {dot_color}"),
                rx.el.h3(
                    title, class_name="text-sm font-semibold text-gray-900"
                ),
                rx.el.span(
                    count,
                    class_name="text-xs font-semibold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                class_name="text-gray-400 hover:text-indigo-600 ml-auto",
            ),
            class_name="flex items-center gap-2 mb-3 px-1",
        ),
        rx.cond(
            tasks.length() > 0,
            rx.el.div(
                rx.foreach(tasks, task_card),
                class_name="flex flex-col gap-2.5",
            ),
            rx.el.div(
                rx.icon("inbox", class_name="h-6 w-6 text-gray-300 mb-2"),
                rx.el.p(
                    "No tasks here yet",
                    class_name="text-sm text-gray-400 font-medium",
                ),
                rx.el.p(
                    "Drop tasks into this column",
                    class_name="text-xs text-gray-400 mt-0.5",
                ),
                class_name="flex flex-col items-center justify-center py-10 border-2 border-dashed border-gray-200 rounded-lg",
            ),
        ),
        class_name="bg-gray-50/70 border border-gray-200 rounded-xl p-3 min-h-[400px]",
    )


def board_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    class_name=WorkspaceState.current_project["color"]
                    + " h-3 w-3 rounded-full"
                ),
                rx.el.h1(
                    WorkspaceState.current_project["name"],
                    class_name="text-2xl font-bold text-gray-900",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.p(
                WorkspaceState.current_project["description"],
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    WorkspaceState.current_project["member_ids"],
                    lambda uid: rx.el.img(
                        src="https://api.dicebear.com/9.x/notionists/svg?seed="
                        + uid,
                        class_name="h-8 w-8 rounded-full bg-white border-2 border-white -ml-2 first:ml-0",
                    ),
                ),
                class_name="flex items-center",
            ),
            filter_menu(),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                "New Task",
                on_click=WorkspaceState.open_new_task,
                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-indigo-600 text-white text-sm font-medium hover:bg-indigo-700",
                type="button",
            ),
            class_name="flex items-center gap-3",
        ),
        class_name="flex items-center justify-between mb-6 flex-wrap gap-3",
    )


def filter_button(label: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=WorkspaceState.set_task_filter(label),
        class_name=rx.cond(
            WorkspaceState.task_filter == label,
            "px-3 py-1.5 rounded-md bg-indigo-600 text-white text-xs font-semibold",
            "px-3 py-1.5 rounded-md bg-white border border-gray-200 text-gray-600 text-xs font-medium hover:bg-gray-50",
        ),
        type="button",
    )


def filter_menu() -> rx.Component:
    return rx.el.div(
        rx.icon("filter", class_name="h-4 w-4 text-gray-400"),
        filter_button("All"),
        filter_button("High"),
        filter_button("Medium"),
        filter_button("Low"),
        class_name="flex items-center gap-1.5",
    )


def project_tabs() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            WorkspaceState.projects,
            lambda p: rx.el.a(
                rx.el.span(class_name=p["color"] + " h-2 w-2 rounded-full"),
                p["name"],
                href="/board/" + p["id"],
                class_name=rx.cond(
                    p["id"] == WorkspaceState.current_project_id,
                    "flex items-center gap-2 px-4 py-2 rounded-lg bg-white border border-indigo-200 text-indigo-700 text-sm font-semibold shadow-sm",
                    "flex items-center gap-2 px-4 py-2 rounded-lg text-gray-600 hover:bg-white hover:text-gray-900 text-sm font-medium border border-transparent",
                ),
            ),
        ),
        class_name="flex items-center gap-2 mb-6 flex-wrap",
    )


def board() -> rx.Component:
    return rx.el.div(
        task_dialog(),
        new_task_dialog(),
        project_tabs(),
        board_header(),
        rx.el.div(
            column(
                "To Do",
                WorkspaceState.todo_tasks.length(),
                "bg-gray-400",
                WorkspaceState.todo_tasks,
            ),
            column(
                "In Progress",
                WorkspaceState.in_progress_tasks.length(),
                "bg-amber-500",
                WorkspaceState.in_progress_tasks,
            ),
            column(
                "Review",
                WorkspaceState.review_tasks.length(),
                "bg-indigo-500",
                WorkspaceState.review_tasks,
            ),
            column(
                "Done",
                WorkspaceState.done_tasks.length(),
                "bg-emerald-500",
                WorkspaceState.done_tasks,
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4",
        ),
        class_name="p-4 sm:p-6",
    )
