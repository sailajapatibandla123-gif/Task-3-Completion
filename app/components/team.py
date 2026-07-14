import reflex as rx
from app.states.workspace_state import WorkspaceState, Project


def workload_row(w: dict) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src="https://api.dicebear.com/9.x/notionists/svg?seed="
            + w["avatar_seed"].to_string(),
            class_name="h-11 w-11 rounded-full bg-gray-100 shrink-0",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    w["name"], class_name="text-sm font-semibold text-gray-900"
                ),
                rx.el.span(
                    w["role"],
                    class_name="text-xs text-gray-500 bg-gray-100 px-2 py-0.5 rounded-md",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name=rx.cond(
                            w["pct"].to(int) >= 80,
                            "h-full bg-rose-500 rounded-full",
                            rx.cond(
                                w["pct"].to(int) >= 50,
                                "h-full bg-amber-500 rounded-full",
                                "h-full bg-emerald-500 rounded-full",
                            ),
                        ),
                        style={"width": w["pct"].to_string() + "%"},
                    ),
                    class_name="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden",
                ),
                rx.el.div(
                    rx.el.span(
                        w["active"].to_string() + " active",
                        class_name="text-xs text-gray-600 font-medium",
                    ),
                    rx.el.span("•", class_name="text-gray-300 mx-1.5"),
                    rx.el.span(
                        w["in_progress"].to_string() + " in progress",
                        class_name="text-xs text-amber-600 font-medium",
                    ),
                    rx.el.span("•", class_name="text-gray-300 mx-1.5"),
                    rx.el.span(
                        w["done"].to_string() + " done",
                        class_name="text-xs text-emerald-600 font-medium",
                    ),
                    rx.el.span("•", class_name="text-gray-300 mx-1.5"),
                    rx.el.span(
                        w["high"].to_string() + " high priority",
                        class_name="text-xs text-rose-600 font-medium",
                    ),
                    class_name="flex items-center mt-1.5 flex-wrap",
                ),
                class_name="mt-2",
            ),
            class_name="flex-1 min-w-0",
        ),
        rx.el.div(
            rx.el.p(
                w["pct"].to_string() + "%",
                class_name="text-lg font-bold text-gray-900",
            ),
            rx.el.p("capacity", class_name="text-xs text-gray-400"),
            class_name="text-right shrink-0",
        ),
        class_name="flex items-center gap-4 p-4 border border-gray-200 rounded-xl bg-white hover:border-indigo-200 transition-colors",
    )


def project_card(p: Project) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.span(class_name=p["color"] + " h-2.5 w-2.5 rounded-full"),
            rx.el.h3(
                p["name"], class_name="text-sm font-semibold text-gray-900"
            ),
            class_name="flex items-center gap-2",
        ),
        rx.el.p(
            p["description"],
            class_name="text-xs text-gray-500 mt-1 line-clamp-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    p["member_ids"],
                    lambda uid: rx.el.img(
                        src="https://api.dicebear.com/9.x/notionists/svg?seed="
                        + uid,
                        class_name="h-7 w-7 rounded-full bg-gray-100 border-2 border-white -ml-2 first:ml-0",
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.span(
                p["member_ids"].length().to_string() + " members",
                class_name="text-xs text-gray-500 ml-auto",
            ),
            class_name="flex items-center mt-3 pt-3 border-t border-gray-100",
        ),
        href="/board/" + p["id"],
        class_name="block p-4 border border-gray-200 rounded-xl bg-white hover:border-indigo-300 transition-colors",
    )


def member_role_row(u: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.img(
                    src="https://api.dicebear.com/9.x/notionists/svg?seed="
                    + u["avatar_seed"],
                    class_name="h-8 w-8 rounded-full bg-gray-100",
                ),
                rx.el.div(
                    rx.el.p(
                        u["name"],
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p(u["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                u["role"],
                class_name="text-xs font-medium text-indigo-700 bg-indigo-50 px-2 py-1 rounded-md",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.span(class_name="h-2 w-2 rounded-full bg-emerald-500"),
                rx.el.span(
                    "Active", class_name="text-xs text-gray-600 font-medium"
                ),
                class_name="flex items-center gap-1.5",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("mail", class_name="h-3.5 w-3.5"),
                "Message",
                class_name="flex items-center gap-1.5 px-3 py-1.5 rounded-md border border-gray-200 text-xs font-medium text-gray-700 hover:bg-gray-50",
                type="button",
            ),
            class_name="px-4 py-3 text-right",
        ),
        class_name="border-t border-gray-100",
    )


def team_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Team Workload",
                    class_name="text-lg font-semibold text-gray-900",
                ),
                rx.el.p(
                    "See who's picking up what across every active project.",
                    class_name="text-sm text-gray-500 mt-0.5",
                ),
            ),
            rx.el.button(
                rx.icon("user-plus", class_name="h-4 w-4"),
                "Invite member",
                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-indigo-600 text-white text-sm font-medium hover:bg-indigo-700",
                type="button",
            ),
            class_name="flex items-start justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(WorkspaceState.workload, workload_row),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-3",
        ),
        rx.el.div(
            rx.el.h2(
                "Group Projects",
                class_name="text-lg font-semibold text-gray-900 mt-8 mb-1",
            ),
            rx.el.p(
                "Projects you and your team collaborate on.",
                class_name="text-sm text-gray-500 mb-4",
            ),
            rx.el.div(
                rx.foreach(WorkspaceState.projects, project_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3",
            ),
        ),
        rx.el.div(
            rx.el.h2(
                "Members & Roles",
                class_name="text-lg font-semibold text-gray-900 mt-8 mb-1",
            ),
            rx.el.p(
                "Manage roles, permissions, and access across the workspace.",
                class_name="text-sm text-gray-500 mb-4",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Member",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Role",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "",
                                class_name="px-4 py-3",
                            ),
                            class_name="bg-gray-50",
                        ),
                    ),
                    rx.el.tbody(
                        rx.foreach(WorkspaceState.users, member_role_row),
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="bg-white border border-gray-200 rounded-xl overflow-hidden",
            ),
        ),
        class_name="p-4 sm:p-6",
    )
