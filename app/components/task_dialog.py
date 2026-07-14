import reflex as rx
from app.states.workspace_state import WorkspaceState, ChecklistItem, Comment


PRIORITIES = ["Low", "Medium", "High"]
STATUSES = ["To Do", "In Progress", "Review", "Done"]


def priority_pill(priority: rx.Var) -> rx.Component:
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


def checklist_row(item: ChecklistItem) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.cond(
                item["done"],
                rx.icon(
                    "square_check_big", class_name="h-4 w-4 text-indigo-600"
                ),
                rx.icon("square", class_name="h-4 w-4 text-gray-400"),
            ),
            on_click=WorkspaceState.toggle_checklist_item(
                WorkspaceState.selected_task_id, item["id"]
            ),
            class_name="shrink-0",
            type="button",
        ),
        rx.el.p(
            item["text"],
            class_name=rx.cond(
                item["done"],
                "text-sm text-gray-400 line-through flex-1",
                "text-sm text-gray-800 flex-1",
            ),
        ),
        rx.el.button(
            rx.icon("trash-2", class_name="h-3.5 w-3.5"),
            on_click=WorkspaceState.delete_checklist_item(
                WorkspaceState.selected_task_id, item["id"]
            ),
            class_name="text-gray-300 hover:text-rose-500 opacity-0 group-hover:opacity-100 transition-opacity",
            type="button",
        ),
        class_name="group flex items-center gap-2.5 py-2 px-2 rounded-md hover:bg-gray-50",
    )


def comment_row(c: Comment) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="https://api.dicebear.com/9.x/notionists/svg?seed="
            + c["author_id"],
            class_name="h-8 w-8 rounded-full bg-gray-100 shrink-0",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    WorkspaceState.user_map[c["author_id"]],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(c["timestamp"], class_name="text-xs text-gray-400"),
                class_name="flex items-center gap-2",
            ),
            rx.el.p(
                c["text"],
                class_name="text-sm text-gray-700 mt-1 leading-relaxed",
            ),
            class_name="flex-1 bg-gray-50 rounded-lg px-3 py-2",
        ),
        class_name="flex items-start gap-3",
    )


def field_label(text: str) -> rx.Component:
    return rx.el.label(
        text,
        class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5 block",
    )


def edit_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            field_label("Title"),
            rx.el.input(
                name="title",
                default_value=WorkspaceState.selected_task["title"],
                key=WorkspaceState.selected_task_id + "-title",
                placeholder="Task title",
                class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm font-medium text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent bg-white",
                required=True,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            field_label("Description"),
            rx.el.textarea(
                name="description",
                default_value=WorkspaceState.selected_task["description"],
                key=WorkspaceState.selected_task_id + "-desc",
                placeholder="Add a description...",
                rows="3",
                class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent bg-white resize-none",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.div(
                field_label("Status"),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            WorkspaceState.columns,
                            lambda s: rx.el.option(s, value=s),
                        ),
                        name="status",
                        default_value=WorkspaceState.selected_task["status"],
                        key=WorkspaceState.selected_task_id + "-status",
                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500",
                    ),
                    rx.icon(
                        "chevron-down",
                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                    ),
                    class_name="relative",
                ),
            ),
            rx.el.div(
                field_label("Priority"),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            PRIORITIES, lambda p: rx.el.option(p, value=p)
                        ),
                        name="priority",
                        default_value=WorkspaceState.selected_task["priority"],
                        key=WorkspaceState.selected_task_id + "-priority",
                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500",
                    ),
                    rx.icon(
                        "chevron-down",
                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                    ),
                    class_name="relative",
                ),
            ),
            rx.el.div(
                field_label("Due Date"),
                rx.el.input(
                    type="date",
                    name="due_date",
                    default_value=WorkspaceState.selected_task["due_date"],
                    key=WorkspaceState.selected_task_id + "-date",
                    class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500",
                ),
            ),
            rx.el.div(
                field_label("Assignee"),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            WorkspaceState.users,
                            lambda u: rx.el.option(u["name"], value=u["id"]),
                        ),
                        name="assignee_id",
                        default_value=WorkspaceState.selected_task[
                            "assignee_id"
                        ],
                        key=WorkspaceState.selected_task_id + "-assignee",
                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500",
                    ),
                    rx.icon(
                        "chevron-down",
                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                    ),
                    class_name="relative",
                ),
            ),
            class_name="grid grid-cols-2 gap-3 mb-4",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("trash-2", class_name="h-4 w-4"),
                "Delete",
                type="button",
                on_click=WorkspaceState.delete_task(
                    WorkspaceState.selected_task_id
                ),
                class_name="flex items-center gap-2 px-3 py-2 rounded-lg border border-rose-200 text-rose-600 text-sm font-medium hover:bg-rose-50",
            ),
            rx.el.button(
                rx.icon("save", class_name="h-4 w-4"),
                "Save changes",
                type="submit",
                class_name="flex items-center gap-2 px-4 py-2 rounded-lg bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700 ml-auto",
            ),
            class_name="flex items-center gap-2",
        ),
        on_submit=WorkspaceState.save_task_edits,
        reset_on_submit=False,
        class_name="bg-white",
    )


def checklist_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("list_checks", class_name="h-4 w-4 text-gray-500"),
            rx.el.h3(
                "Checklist", class_name="text-sm font-semibold text-gray-900"
            ),
            rx.el.span(
                WorkspaceState.selected_task["progress"].to_string() + "%",
                class_name="text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md ml-auto",
            ),
            class_name="flex items-center gap-2 mb-2",
        ),
        rx.el.div(
            rx.el.div(
                class_name="h-full bg-indigo-500 rounded-full transition-all",
                style={
                    "width": WorkspaceState.selected_task[
                        "progress"
                    ].to_string()
                    + "%"
                },
            ),
            class_name="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden mb-3",
        ),
        rx.cond(
            WorkspaceState.selected_task_checklist.length() > 0,
            rx.el.div(
                rx.foreach(
                    WorkspaceState.selected_task_checklist, checklist_row
                ),
                class_name="flex flex-col",
            ),
            rx.el.p(
                "No checklist items yet. Break the work down below.",
                class_name="text-sm text-gray-400 italic py-2 px-2",
            ),
        ),
        rx.el.form(
            rx.el.input(
                name="checklist_text",
                placeholder="Add a checklist item...",
                class_name="flex-1 px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500",
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                type="submit",
                class_name="px-3 py-2 rounded-lg bg-gray-900 text-white text-sm font-medium hover:bg-gray-800",
            ),
            on_submit=WorkspaceState.add_checklist_item,
            reset_on_submit=True,
            class_name="flex items-center gap-2 mt-2",
        ),
        class_name="border-t border-gray-100 pt-4 mt-4",
    )


def comments_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("message_square", class_name="h-4 w-4 text-gray-500"),
            rx.el.h3(
                "Comments", class_name="text-sm font-semibold text-gray-900"
            ),
            rx.el.span(
                WorkspaceState.selected_task_comments.length().to_string(),
                class_name="text-xs font-semibold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full ml-auto",
            ),
            class_name="flex items-center gap-2 mb-3",
        ),
        rx.cond(
            WorkspaceState.selected_task_comments.length() > 0,
            rx.el.div(
                rx.foreach(WorkspaceState.selected_task_comments, comment_row),
                class_name="flex flex-col gap-3 mb-3",
            ),
            rx.el.p(
                "No comments yet. Kick off the discussion below.",
                class_name="text-sm text-gray-400 italic py-2",
            ),
        ),
        rx.el.form(
            rx.el.img(
                src="https://api.dicebear.com/9.x/notionists/svg?seed=alex",
                class_name="h-8 w-8 rounded-full bg-gray-100 shrink-0",
            ),
            rx.el.div(
                rx.el.textarea(
                    name="comment",
                    placeholder="Write a comment...",
                    rows="2",
                    class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500 resize-none",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("send", class_name="h-4 w-4"),
                        "Post comment",
                        type="submit",
                        class_name="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700 ml-auto",
                    ),
                    class_name="flex items-center mt-2",
                ),
                class_name="flex-1",
            ),
            on_submit=WorkspaceState.add_comment,
            reset_on_submit=True,
            class_name="flex items-start gap-3",
        ),
        class_name="border-t border-gray-100 pt-4 mt-4",
    )


def task_meta() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("folder", class_name="h-3.5 w-3.5 text-gray-400"),
            rx.el.span(
                WorkspaceState.selected_task_project_name,
                class_name="text-xs text-gray-600 font-medium",
            ),
            class_name="flex items-center gap-1.5",
        ),
        rx.el.span("•", class_name="text-gray-300"),
        priority_pill(WorkspaceState.selected_task["priority"]),
        rx.el.span("•", class_name="text-gray-300"),
        rx.el.div(
            rx.icon("calendar", class_name="h-3.5 w-3.5 text-gray-400"),
            rx.el.span(
                rx.cond(
                    WorkspaceState.selected_task["due_date"] != "",
                    WorkspaceState.selected_task["due_date"],
                    "No due date",
                ),
                class_name="text-xs text-gray-600",
            ),
            class_name="flex items-center gap-1.5",
        ),
        rx.el.span("•", class_name="text-gray-300"),
        rx.el.div(
            rx.el.img(
                src="https://api.dicebear.com/9.x/notionists/svg?seed="
                + WorkspaceState.selected_task["assignee_id"],
                class_name="h-5 w-5 rounded-full bg-gray-100",
            ),
            rx.el.span(
                WorkspaceState.selected_task_assignee_name,
                class_name="text-xs text-gray-700 font-medium",
            ),
            class_name="flex items-center gap-1.5",
        ),
        class_name="flex items-center gap-2 flex-wrap",
    )


def task_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/40 backdrop-blur-sm z-40",
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                WorkspaceState.selected_task["status"],
                                class_name="text-xs font-semibold px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 border border-indigo-100",
                            ),
                            rx.radix.primitives.dialog.title(
                                WorkspaceState.selected_task["title"],
                                class_name="text-xl font-bold text-gray-900 mt-2",
                            ),
                            rx.el.div(task_meta(), class_name="mt-2"),
                            class_name="flex-1",
                        ),
                        rx.radix.primitives.dialog.close(
                            rx.el.button(
                                rx.icon("x", class_name="h-4 w-4"),
                                class_name="p-2 rounded-lg text-gray-400 hover:bg-gray-100 hover:text-gray-700",
                                type="button",
                            ),
                        ),
                        class_name="flex items-start gap-3 p-6 border-b border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.div(
                            edit_form(),
                            checklist_section(),
                            comments_section(),
                            class_name="p-6",
                        ),
                        class_name="max-h-[70vh] overflow-y-auto",
                    ),
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-2xl w-full max-w-2xl z-50 border border-gray-200",
            ),
        ),
        open=WorkspaceState.show_task_dialog,
        on_open_change=WorkspaceState.toggle_task_dialog,
    )


def new_task_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/40 backdrop-blur-sm z-40",
            ),
            rx.radix.primitives.dialog.content(
                rx.el.form(
                    rx.el.div(
                        rx.radix.primitives.dialog.title(
                            "Create new task",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            "Assign work to your team and keep momentum moving.",
                            class_name="text-sm text-gray-500 mt-1",
                        ),
                        class_name="p-6 border-b border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.div(
                            field_label("Title *"),
                            rx.el.input(
                                name="title",
                                placeholder="e.g. Design onboarding flow",
                                required=True,
                                class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            field_label("Description"),
                            rx.el.textarea(
                                name="description",
                                placeholder="What needs to happen?",
                                rows="3",
                                class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500 resize-none",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                field_label("Project"),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            WorkspaceState.projects,
                                            lambda p: rx.el.option(
                                                p["name"], value=p["id"]
                                            ),
                                        ),
                                        name="project_id",
                                        default_value=WorkspaceState.current_project_id,
                                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            rx.el.div(
                                field_label("Status"),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            STATUSES,
                                            lambda s: rx.el.option(s, value=s),
                                        ),
                                        name="status",
                                        default_value="To Do",
                                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            rx.el.div(
                                field_label("Priority"),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            PRIORITIES,
                                            lambda p: rx.el.option(p, value=p),
                                        ),
                                        name="priority",
                                        default_value="Medium",
                                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            rx.el.div(
                                field_label("Assignee"),
                                rx.el.div(
                                    rx.el.select(
                                        rx.foreach(
                                            WorkspaceState.users,
                                            lambda u: rx.el.option(
                                                u["name"], value=u["id"]
                                            ),
                                        ),
                                        name="assignee_id",
                                        default_value="u1",
                                        class_name="w-full px-3 py-2 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        class_name="absolute right-2 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                                    ),
                                    class_name="relative",
                                ),
                            ),
                            rx.el.div(
                                field_label("Due Date"),
                                rx.el.input(
                                    type="date",
                                    name="due_date",
                                    class_name="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white",
                                ),
                                class_name="col-span-2",
                            ),
                            class_name="grid grid-cols-2 gap-3 mb-4",
                        ),
                        class_name="p-6",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.close(
                            rx.el.button(
                                "Cancel",
                                type="button",
                                class_name="px-4 py-2 rounded-lg border border-gray-200 text-gray-700 text-sm font-medium hover:bg-gray-50",
                            ),
                        ),
                        rx.el.button(
                            rx.icon("plus", class_name="h-4 w-4"),
                            "Create task",
                            type="submit",
                            class_name="flex items-center gap-2 px-4 py-2 rounded-lg bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700",
                        ),
                        class_name="flex items-center justify-end gap-2 p-4 border-t border-gray-100 bg-gray-50/50 rounded-b-xl",
                    ),
                    on_submit=WorkspaceState.add_task,
                    reset_on_submit=True,
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-2xl w-full max-w-lg z-50 border border-gray-200",
            ),
        ),
        open=WorkspaceState.show_new_task_dialog,
        on_open_change=WorkspaceState.toggle_new_task_dialog,
    )
