import reflex as rx
from app.states.workspace_state import WorkspaceState, Notification


def notification_row(n: Notification) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.icon(n["icon"], class_name="h-4 w-4"),
            class_name=rx.match(
                n["category"],
                (
                    "assignment",
                    "h-9 w-9 rounded-lg flex items-center justify-center shrink-0 bg-indigo-50 text-indigo-600",
                ),
                (
                    "comment",
                    "h-9 w-9 rounded-lg flex items-center justify-center shrink-0 bg-blue-50 text-blue-600",
                ),
                (
                    "deadline",
                    "h-9 w-9 rounded-lg flex items-center justify-center shrink-0 bg-rose-50 text-rose-600",
                ),
                (
                    "project",
                    "h-9 w-9 rounded-lg flex items-center justify-center shrink-0 bg-emerald-50 text-emerald-600",
                ),
                "h-9 w-9 rounded-lg flex items-center justify-center shrink-0 bg-gray-100 text-gray-600",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    n["title"],
                    class_name=rx.cond(
                        n["read"],
                        "text-sm text-gray-700 font-medium",
                        "text-sm text-gray-900 font-semibold",
                    ),
                ),
                rx.cond(
                    n["read"],
                    rx.fragment(),
                    rx.el.span(
                        class_name="h-2 w-2 rounded-full bg-indigo-500 shrink-0 ml-2 mt-1.5"
                    ),
                ),
                class_name="flex items-start justify-between gap-2",
            ),
            rx.el.p(
                n["detail"],
                class_name="text-xs text-gray-500 mt-0.5 line-clamp-2 text-left",
            ),
            rx.el.p(
                n["timestamp"],
                class_name="text-xs text-gray-400 mt-1 text-left",
            ),
            class_name="flex-1 min-w-0 text-left",
        ),
        type="button",
        on_click=WorkspaceState.open_notification(n["id"]),
        class_name=rx.cond(
            n["read"],
            "w-full flex items-start gap-3 p-3 rounded-lg hover:bg-gray-50 transition-colors text-left",
            "w-full flex items-start gap-3 p-3 rounded-lg bg-indigo-50/40 hover:bg-indigo-50 transition-colors text-left",
        ),
    )


def notif_filter_pill(label: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=WorkspaceState.set_notification_filter(label),
        type="button",
        class_name=rx.cond(
            WorkspaceState.notification_filter == label,
            "px-2.5 py-1 rounded-md bg-indigo-600 text-white text-xs font-semibold",
            "px-2.5 py-1 rounded-md bg-gray-100 text-gray-600 text-xs font-medium hover:bg-gray-200",
        ),
    )


def notifications_panel() -> rx.Component:
    return rx.cond(
        WorkspaceState.show_notifications,
        rx.el.div(
            rx.el.div(
                on_click=WorkspaceState.close_notifications,
                class_name="fixed inset-0 z-30",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Notifications",
                            class_name="text-sm font-semibold text-gray-900",
                        ),
                        rx.el.span(
                            WorkspaceState.unread_notifications_count.to_string()
                            + " unread",
                            class_name="text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.button(
                        "Mark all read",
                        on_click=WorkspaceState.mark_all_read,
                        type="button",
                        class_name="text-xs font-medium text-indigo-600 hover:text-indigo-700",
                    ),
                    class_name="flex items-center justify-between px-4 py-3 border-b border-gray-100",
                ),
                rx.el.div(
                    notif_filter_pill("All"),
                    notif_filter_pill("Unread"),
                    notif_filter_pill("Assignment"),
                    notif_filter_pill("Comment"),
                    notif_filter_pill("Deadline"),
                    notif_filter_pill("Project"),
                    class_name="flex items-center gap-1.5 px-3 py-2 border-b border-gray-100 overflow-x-auto",
                ),
                rx.cond(
                    WorkspaceState.filtered_notifications.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            WorkspaceState.filtered_notifications,
                            notification_row,
                        ),
                        class_name="flex flex-col gap-1 p-2 max-h-96 overflow-y-auto",
                    ),
                    rx.el.div(
                        rx.icon(
                            "bell_off", class_name="h-8 w-8 text-gray-300 mb-2"
                        ),
                        rx.el.p(
                            "You're all caught up",
                            class_name="text-sm font-medium text-gray-500",
                        ),
                        rx.el.p(
                            "No notifications in this view",
                            class_name="text-xs text-gray-400 mt-0.5",
                        ),
                        class_name="flex flex-col items-center justify-center py-12 px-4",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        "Clear all",
                        on_click=WorkspaceState.clear_notifications,
                        type="button",
                        class_name="text-xs font-medium text-gray-500 hover:text-rose-600",
                    ),
                    rx.el.a(
                        "View activity log",
                        href="/",
                        on_click=WorkspaceState.close_notifications,
                        class_name="text-xs font-medium text-indigo-600 hover:text-indigo-700 ml-auto",
                    ),
                    class_name="flex items-center px-4 py-2.5 border-t border-gray-100 bg-gray-50/60 rounded-b-xl",
                ),
                class_name="absolute right-0 top-12 w-96 max-w-[calc(100vw-2rem)] bg-white border border-gray-200 rounded-xl shadow-lg z-40 overflow-hidden",
            ),
            class_name="relative",
        ),
        rx.fragment(),
    )
