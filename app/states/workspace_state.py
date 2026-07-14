import reflex as rx
from typing import TypedDict


class User(TypedDict):
    id: str
    name: str
    email: str
    role: str
    avatar_seed: str


class Comment(TypedDict):
    id: str
    task_id: str
    author_id: str
    text: str
    timestamp: str


class ChecklistItem(TypedDict):
    id: str
    text: str
    done: bool


class Task(TypedDict):
    id: str
    project_id: str
    title: str
    description: str
    status: str
    priority: str
    due_date: str
    assignee_id: str
    progress: int
    tags: list[str]


class Project(TypedDict):
    id: str
    name: str
    description: str
    color: str
    member_ids: list[str]


class Activity(TypedDict):
    id: str
    user_id: str
    action: str
    target: str
    timestamp: str


class Notification(TypedDict):
    id: str
    icon: str
    category: str
    title: str
    detail: str
    timestamp: str
    read: bool
    task_id: str
    project_id: str


USERS: list[User] = [
    {
        "id": "u1",
        "name": "Alex Morgan",
        "email": "alex@codealpha.tech",
        "role": "Product Lead",
        "avatar_seed": "alex",
    },
    {
        "id": "u2",
        "name": "Priya Shah",
        "email": "priya@codealpha.tech",
        "role": "Frontend Engineer",
        "avatar_seed": "priya",
    },
    {
        "id": "u3",
        "name": "Diego Santos",
        "email": "diego@codealpha.tech",
        "role": "Backend Engineer",
        "avatar_seed": "diego",
    },
    {
        "id": "u4",
        "name": "Mei Chen",
        "email": "mei@codealpha.tech",
        "role": "UX Designer",
        "avatar_seed": "mei",
    },
    {
        "id": "u5",
        "name": "Jordan Blake",
        "email": "jordan@codealpha.tech",
        "role": "QA Engineer",
        "avatar_seed": "jordan",
    },
    {
        "id": "u6",
        "name": "Sara Ahmed",
        "email": "sara@codealpha.tech",
        "role": "DevOps",
        "avatar_seed": "sara",
    },
]

PROJECTS: list[Project] = [
    {
        "id": "p1",
        "name": "Atlas Web Platform",
        "description": "Customer-facing marketing site with CMS integration.",
        "color": "bg-indigo-500",
        "member_ids": ["u1", "u2", "u4", "u6"],
    },
    {
        "id": "p2",
        "name": "Mobile Companion App",
        "description": "iOS & Android companion app for Atlas users.",
        "color": "bg-emerald-500",
        "member_ids": ["u1", "u3", "u5"],
    },
    {
        "id": "p3",
        "name": "Internal Analytics",
        "description": "Dashboards, reporting, and KPI tracking pipeline.",
        "color": "bg-amber-500",
        "member_ids": ["u2", "u3", "u6"],
    },
]

TASKS: list[Task] = [
    {
        "id": "t1",
        "project_id": "p1",
        "title": "Design homepage hero section",
        "description": "Redesign the landing page hero with new brand illustrations and CTAs.",
        "status": "In Progress",
        "priority": "High",
        "due_date": "2025-02-14",
        "assignee_id": "u4",
        "progress": 60,
        "tags": ["design", "frontend"],
    },
    {
        "id": "t2",
        "project_id": "p1",
        "title": "Set up CMS content models",
        "description": "Configure content types, fields, and preview environments in the CMS.",
        "status": "To Do",
        "priority": "Medium",
        "due_date": "2025-02-20",
        "assignee_id": "u2",
        "progress": 0,
        "tags": ["cms", "backend"],
    },
    {
        "id": "t3",
        "project_id": "p1",
        "title": "Implement responsive navigation",
        "description": "Build accessible mobile-first navigation with dropdowns.",
        "status": "In Progress",
        "priority": "High",
        "due_date": "2025-02-16",
        "assignee_id": "u2",
        "progress": 40,
        "tags": ["frontend"],
    },
    {
        "id": "t4",
        "project_id": "p1",
        "title": "SEO audit and metadata pass",
        "description": "Complete a full SEO audit and update metadata across pages.",
        "status": "Review",
        "priority": "Medium",
        "due_date": "2025-02-10",
        "assignee_id": "u1",
        "progress": 85,
        "tags": ["seo"],
    },
    {
        "id": "t5",
        "project_id": "p1",
        "title": "Launch checklist",
        "description": "Compile a pre-launch checklist covering QA, analytics, and rollback.",
        "status": "Done",
        "priority": "Low",
        "due_date": "2025-01-28",
        "assignee_id": "u1",
        "progress": 100,
        "tags": ["launch"],
    },
    {
        "id": "t6",
        "project_id": "p1",
        "title": "Integrate analytics events",
        "description": "Wire up product analytics events for key funnel steps.",
        "status": "To Do",
        "priority": "High",
        "due_date": "2025-02-22",
        "assignee_id": "u6",
        "progress": 0,
        "tags": ["analytics"],
    },
    {
        "id": "t7",
        "project_id": "p1",
        "title": "Accessibility review",
        "description": "Run axe-core audit and fix issues.",
        "status": "Review",
        "priority": "High",
        "due_date": "2025-02-12",
        "assignee_id": "u4",
        "progress": 70,
        "tags": ["a11y"],
    },
    {
        "id": "t8",
        "project_id": "p2",
        "title": "Push notifications MVP",
        "description": "Implement push notifications for task assignments and mentions.",
        "status": "In Progress",
        "priority": "High",
        "due_date": "2025-02-18",
        "assignee_id": "u3",
        "progress": 50,
        "tags": ["mobile", "backend"],
    },
    {
        "id": "t9",
        "project_id": "p2",
        "title": "Offline mode caching",
        "description": "Cache recent projects and tasks for offline access.",
        "status": "To Do",
        "priority": "Medium",
        "due_date": "2025-03-01",
        "assignee_id": "u3",
        "progress": 0,
        "tags": ["mobile"],
    },
    {
        "id": "t10",
        "project_id": "p2",
        "title": "App store screenshots",
        "description": "Produce updated marketing screenshots for iOS and Android stores.",
        "status": "Done",
        "priority": "Low",
        "due_date": "2025-01-30",
        "assignee_id": "u5",
        "progress": 100,
        "tags": ["marketing"],
    },
    {
        "id": "t11",
        "project_id": "p3",
        "title": "KPI definitions workshop",
        "description": "Align on North Star metrics and KPI definitions across teams.",
        "status": "Done",
        "priority": "Medium",
        "due_date": "2025-01-25",
        "assignee_id": "u1",
        "progress": 100,
        "tags": ["strategy"],
    },
    {
        "id": "t12",
        "project_id": "p3",
        "title": "Data pipeline hardening",
        "description": "Add retries, monitoring, and alerts to the ETL pipelines.",
        "status": "In Progress",
        "priority": "High",
        "due_date": "2025-02-15",
        "assignee_id": "u6",
        "progress": 35,
        "tags": ["data"],
    },
    {
        "id": "t13",
        "project_id": "p3",
        "title": "Executive dashboard v2",
        "description": "Ship the redesigned executive dashboard with drill-downs.",
        "status": "Review",
        "priority": "High",
        "due_date": "2025-02-11",
        "assignee_id": "u2",
        "progress": 80,
        "tags": ["dashboard"],
    },
]

COMMENTS: list[Comment] = [
    {
        "id": "c1",
        "task_id": "t1",
        "author_id": "u1",
        "text": "Love the new direction — can we try a lighter background variant?",
        "timestamp": "2h ago",
    },
    {
        "id": "c2",
        "task_id": "t1",
        "author_id": "u4",
        "text": "Sure, pushing an update shortly with two variants.",
        "timestamp": "1h ago",
    },
    {
        "id": "c3",
        "task_id": "t3",
        "author_id": "u2",
        "text": "Mobile menu animation is now smoother on low-end devices.",
        "timestamp": "4h ago",
    },
    {
        "id": "c4",
        "task_id": "t8",
        "author_id": "u3",
        "text": "Backend endpoints are ready, integrating into the mobile client now.",
        "timestamp": "yesterday",
    },
    {
        "id": "c5",
        "task_id": "t12",
        "author_id": "u6",
        "text": "Added Prometheus alerts for pipeline lag over 10 minutes.",
        "timestamp": "yesterday",
    },
]

ACTIVITIES: list[Activity] = [
    {
        "id": "a1",
        "user_id": "u4",
        "action": "updated task",
        "target": "Design homepage hero section",
        "timestamp": "2 min ago",
    },
    {
        "id": "a2",
        "user_id": "u2",
        "action": "moved to Review",
        "target": "Executive dashboard v2",
        "timestamp": "18 min ago",
    },
    {
        "id": "a3",
        "user_id": "u1",
        "action": "commented on",
        "target": "Design homepage hero section",
        "timestamp": "1 hr ago",
    },
    {
        "id": "a4",
        "user_id": "u3",
        "action": "completed task",
        "target": "Push notifications API",
        "timestamp": "3 hr ago",
    },
    {
        "id": "a5",
        "user_id": "u6",
        "action": "created task",
        "target": "Data pipeline hardening",
        "timestamp": "yesterday",
    },
    {
        "id": "a6",
        "user_id": "u5",
        "action": "assigned",
        "target": "App store screenshots",
        "timestamp": "2 days ago",
    },
]


DEFAULT_CHECKLISTS: dict[str, list[ChecklistItem]] = {
    "t1": [
        {"id": "ck1", "text": "Sketch three hero variants", "done": True},
        {"id": "ck2", "text": "Review with brand team", "done": True},
        {"id": "ck3", "text": "Ship final Figma handoff", "done": False},
        {"id": "ck4", "text": "Implement responsive states", "done": False},
    ],
    "t3": [
        {"id": "ck5", "text": "Build mobile drawer", "done": True},
        {"id": "ck6", "text": "Wire keyboard navigation", "done": False},
        {"id": "ck7", "text": "Add focus states", "done": False},
    ],
    "t8": [
        {"id": "ck8", "text": "Design permission prompts", "done": True},
        {"id": "ck9", "text": "Wire APNs / FCM", "done": True},
        {"id": "ck10", "text": "Deep-link into tasks", "done": False},
    ],
    "t12": [
        {"id": "ck11", "text": "Add pipeline retries", "done": True},
        {"id": "ck12", "text": "Instrument alerts", "done": False},
        {"id": "ck13", "text": "Backfill missing runs", "done": False},
    ],
    "t13": [
        {"id": "ck14", "text": "Refactor query layer", "done": True},
        {"id": "ck15", "text": "New KPI tiles", "done": True},
        {"id": "ck16", "text": "Drill-down modals", "done": False},
    ],
}


DEFAULT_NOTIFICATIONS: list[Notification] = [
    {
        "id": "n1",
        "icon": "user-plus",
        "category": "assignment",
        "title": "Mei Chen assigned you a task",
        "detail": "Design homepage hero section — due Feb 14",
        "timestamp": "2 min ago",
        "read": False,
        "task_id": "t1",
        "project_id": "p1",
    },
    {
        "id": "n2",
        "icon": "message_square",
        "category": "comment",
        "title": "Priya Shah commented on your task",
        "detail": '"Mobile menu animation is now smoother on low-end devices."',
        "timestamp": "18 min ago",
        "read": False,
        "task_id": "t3",
        "project_id": "p1",
    },
    {
        "id": "n3",
        "icon": "clock",
        "category": "deadline",
        "title": "Deadline approaching",
        "detail": "SEO audit and metadata pass is due in 2 days.",
        "timestamp": "1 hr ago",
        "read": False,
        "task_id": "t4",
        "project_id": "p1",
    },
    {
        "id": "n4",
        "icon": "folder-plus",
        "category": "project",
        "title": "Sara Ahmed added you to a project",
        "detail": "Internal Analytics — you can now view and comment.",
        "timestamp": "3 hr ago",
        "read": True,
        "task_id": "",
        "project_id": "p3",
    },
    {
        "id": "n5",
        "icon": "circle_check",
        "category": "project",
        "title": "Diego Santos completed a task",
        "detail": "Push notifications API is now marked Done.",
        "timestamp": "yesterday",
        "read": True,
        "task_id": "t8",
        "project_id": "p2",
    },
    {
        "id": "n6",
        "icon": "triangle_alert",
        "category": "deadline",
        "title": "Overdue high-priority task",
        "detail": "Data pipeline hardening is past its target date.",
        "timestamp": "yesterday",
        "read": True,
        "task_id": "t12",
        "project_id": "p3",
    },
]


class WorkspaceState(rx.State):
    users: list[User] = USERS
    projects: list[Project] = PROJECTS
    tasks: list[Task] = TASKS
    comments: list[Comment] = COMMENTS
    activities: list[Activity] = ACTIVITIES
    checklists: dict[str, list[ChecklistItem]] = DEFAULT_CHECKLISTS
    notifications: list[Notification] = DEFAULT_NOTIFICATIONS

    current_project_id: str = "p1"
    columns: list[str] = ["To Do", "In Progress", "Review", "Done"]

    selected_task_id: str = ""
    show_task_dialog: bool = False
    show_new_task_dialog: bool = False
    show_notifications: bool = False
    show_mobile_sidebar: bool = False
    new_comment_text: str = ""
    new_checklist_text: str = ""
    task_filter: str = "All"
    notification_filter: str = "All"
    is_loading: bool = False

    @rx.var
    def current_project(self) -> Project:
        for p in self.projects:
            if p["id"] == self.current_project_id:
                return p
        return self.projects[0]

    @rx.var
    def current_project_tasks(self) -> list[Task]:
        return [
            t for t in self.tasks if t["project_id"] == self.current_project_id
        ]

    @rx.var
    def todo_tasks(self) -> list[Task]:
        return [
            t for t in self.filtered_project_tasks if t["status"] == "To Do"
        ]

    @rx.var
    def in_progress_tasks(self) -> list[Task]:
        return [
            t
            for t in self.filtered_project_tasks
            if t["status"] == "In Progress"
        ]

    @rx.var
    def review_tasks(self) -> list[Task]:
        return [
            t for t in self.filtered_project_tasks if t["status"] == "Review"
        ]

    @rx.var
    def done_tasks(self) -> list[Task]:
        return [t for t in self.filtered_project_tasks if t["status"] == "Done"]

    @rx.var
    def total_tasks(self) -> int:
        return len(self.tasks)

    @rx.var
    def completed_tasks(self) -> int:
        return len([t for t in self.tasks if t["status"] == "Done"])

    @rx.var
    def in_progress_count(self) -> int:
        return len([t for t in self.tasks if t["status"] == "In Progress"])

    @rx.var
    def overdue_count(self) -> int:
        return len(
            [
                t
                for t in self.tasks
                if t["priority"] == "High" and t["status"] != "Done"
            ]
        )

    @rx.var
    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0
        return round(self.completed_tasks / len(self.tasks) * 100, 1)

    @rx.var
    def team_size(self) -> int:
        return len(self.users)

    @rx.var
    def project_task_counts(self) -> list[dict[str, str | int]]:
        result: list[dict[str, str | int]] = []
        for p in self.projects:
            proj_tasks = [t for t in self.tasks if t["project_id"] == p["id"]]
            done = len([t for t in proj_tasks if t["status"] == "Done"])
            total = len(proj_tasks)
            pct = int(done / total * 100) if total else 0
            result.append(
                {
                    "id": p["id"],
                    "name": p["name"],
                    "color": p["color"],
                    "done": done,
                    "total": total,
                    "pct": pct,
                }
            )
        return result

    @rx.var
    def user_map(self) -> dict[str, str]:
        return {u["id"]: u["name"] for u in self.users}

    @rx.event
    def select_project(self, project_id: str):
        self.current_project_id = project_id

    @rx.event
    def move_task(self, task_id: str, new_status: str):
        for i, t in enumerate(self.tasks):
            if t["id"] == task_id:
                self.tasks[i] = {**t, "status": new_status}
                break

    @rx.var
    def selected_task(self) -> Task:
        for t in self.tasks:
            if t["id"] == self.selected_task_id:
                return t
        return {
            "id": "",
            "project_id": "",
            "title": "",
            "description": "",
            "status": "To Do",
            "priority": "Medium",
            "due_date": "",
            "assignee_id": "u1",
            "progress": 0,
            "tags": [],
        }

    @rx.var
    def selected_task_comments(self) -> list[Comment]:
        return [
            c for c in self.comments if c["task_id"] == self.selected_task_id
        ]

    @rx.var
    def selected_task_checklist(self) -> list[ChecklistItem]:
        return self.checklists.get(self.selected_task_id, [])

    @rx.var
    def selected_task_assignee_name(self) -> str:
        return self.user_map.get(
            self.selected_task["assignee_id"], "Unassigned"
        )

    @rx.var
    def selected_task_project_name(self) -> str:
        for p in self.projects:
            if p["id"] == self.selected_task["project_id"]:
                return p["name"]
        return ""

    @rx.var
    def workload(self) -> list[dict[str, str | int]]:
        counts: dict[str, dict[str, int]] = {}
        for u in self.users:
            counts[u["id"]] = {
                "total": 0,
                "in_progress": 0,
                "done": 0,
                "high": 0,
            }
        for t in self.tasks:
            uid = t["assignee_id"]
            if uid in counts:
                counts[uid]["total"] += 1
                if t["status"] == "In Progress":
                    counts[uid]["in_progress"] += 1
                if t["status"] == "Done":
                    counts[uid]["done"] += 1
                if t["priority"] == "High" and t["status"] != "Done":
                    counts[uid]["high"] += 1
        result: list[dict[str, str | int]] = []
        for u in self.users:
            c = counts[u["id"]]
            active = c["total"] - c["done"]
            capacity = 8
            pct = min(int(active / capacity * 100), 100) if capacity else 0
            result.append(
                {
                    "id": u["id"],
                    "name": u["name"],
                    "role": u["role"],
                    "avatar_seed": u["avatar_seed"],
                    "total": c["total"],
                    "in_progress": c["in_progress"],
                    "done": c["done"],
                    "high": c["high"],
                    "active": active,
                    "pct": pct,
                }
            )
        return result

    @rx.var
    def filtered_project_tasks(self) -> list[Task]:
        if self.task_filter == "All":
            return self.current_project_tasks
        if self.task_filter in ("High", "Medium", "Low"):
            return [
                t
                for t in self.current_project_tasks
                if t["priority"] == self.task_filter
            ]
        return self.current_project_tasks

    @rx.event
    def set_task_filter(self, value: str):
        self.task_filter = value

    @rx.event
    def open_task(self, task_id: str):
        exists = any(t["id"] == task_id for t in self.tasks)
        if not exists:
            return rx.toast("This task could not be found")
        self.selected_task_id = task_id
        self.new_comment_text = ""
        self.new_checklist_text = ""
        self.show_task_dialog = True

    @rx.event
    def close_task(self):
        self.show_task_dialog = False
        self.new_comment_text = ""
        self.new_checklist_text = ""

    @rx.event
    def toggle_task_dialog(self, value: bool):
        self.show_task_dialog = value

    @rx.event
    def open_new_task(self):
        self.show_new_task_dialog = True

    @rx.event
    def toggle_new_task_dialog(self, value: bool):
        self.show_new_task_dialog = value

    @rx.event
    def set_new_comment(self, value: str):
        self.new_comment_text = value

    @rx.event
    def set_new_checklist(self, value: str):
        self.new_checklist_text = value

    def _add_activity(self, action: str, target: str):
        import uuid

        self.activities.insert(
            0,
            {
                "id": str(uuid.uuid4())[:6],
                "user_id": "u1",
                "action": action,
                "target": target,
                "timestamp": "just now",
            },
        )

    def _add_notification(
        self,
        icon: str,
        category: str,
        title: str,
        detail: str,
        task_id: str = "",
        project_id: str = "",
    ):
        import uuid

        self.notifications.insert(
            0,
            {
                "id": str(uuid.uuid4())[:6],
                "icon": icon,
                "category": category,
                "title": title,
                "detail": detail,
                "timestamp": "just now",
                "read": False,
                "task_id": task_id,
                "project_id": project_id,
            },
        )

    @rx.var
    def unread_notifications_count(self) -> int:
        return len([n for n in self.notifications if not n["read"]])

    @rx.var
    def filtered_notifications(self) -> list[Notification]:
        if self.notification_filter == "All":
            return self.notifications
        if self.notification_filter == "Unread":
            return [n for n in self.notifications if not n["read"]]
        return [
            n
            for n in self.notifications
            if n["category"] == self.notification_filter.lower()
        ]

    @rx.var
    def status_distribution(self) -> list[dict[str, str | int]]:
        result: list[dict[str, str | int]] = []
        colors = {
            "To Do": "#94a3b8",
            "In Progress": "#f59e0b",
            "Review": "#6366f1",
            "Done": "#10b981",
        }
        for status in self.columns:
            count = len([t for t in self.tasks if t["status"] == status])
            result.append(
                {"status": status, "count": count, "fill": colors[status]}
            )
        return result

    @rx.var
    def priority_distribution(self) -> list[dict[str, str | int]]:
        result: list[dict[str, str | int]] = []
        colors = {"High": "#f43f5e", "Medium": "#f59e0b", "Low": "#10b981"}
        for pri in ["High", "Medium", "Low"]:
            count = len([t for t in self.tasks if t["priority"] == pri])
            result.append(
                {"priority": pri, "count": count, "fill": colors[pri]}
            )
        return result

    @rx.var
    def weekly_activity(self) -> list[dict[str, str | int]]:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        completed = [3, 5, 4, 7, 6, 2, 4]
        created = [4, 6, 5, 5, 8, 3, 5]
        return [
            {"day": d, "completed": c, "created": cr}
            for d, c, cr in zip(days, completed, created)
        ]

    @rx.var
    def upcoming_deadlines(self) -> list[Task]:
        pending = [
            t
            for t in self.tasks
            if t["status"] != "Done" and t["due_date"] != ""
        ]
        return sorted(pending, key=lambda t: t["due_date"])[:5]

    @rx.event
    def toggle_notifications(self):
        self.show_notifications = not self.show_notifications

    @rx.event
    def close_notifications(self):
        self.show_notifications = False

    @rx.event
    def toggle_mobile_sidebar(self):
        self.show_mobile_sidebar = not self.show_mobile_sidebar

    @rx.event
    def close_mobile_sidebar(self):
        self.show_mobile_sidebar = False

    @rx.event
    def set_notification_filter(self, value: str):
        self.notification_filter = value

    @rx.event
    def mark_notification_read(self, notif_id: str):
        for i, n in enumerate(self.notifications):
            if n["id"] == notif_id:
                self.notifications[i] = {**n, "read": True}
                break

    @rx.event
    def mark_all_read(self):
        self.notifications = [{**n, "read": True} for n in self.notifications]
        return rx.toast("All notifications marked as read")

    @rx.event
    def clear_notifications(self):
        self.notifications = []
        return rx.toast("Notifications cleared")

    @rx.event
    def open_notification(self, notif_id: str):
        target_task = ""
        target_project = ""
        for i, n in enumerate(self.notifications):
            if n["id"] == notif_id:
                self.notifications[i] = {**n, "read": True}
                target_task = n["task_id"]
                target_project = n["project_id"]
                break
        self.show_notifications = False
        if target_task:
            exists = any(t["id"] == target_task for t in self.tasks)
            if exists:
                if target_project:
                    self.current_project_id = target_project
                self.selected_task_id = target_task
                self.show_task_dialog = True
                return
        if target_project:
            self.current_project_id = target_project
            return rx.redirect(f"/board/{target_project}")

    @rx.event
    def add_comment(self, form_data: dict):
        text = form_data.get("comment", "").strip()
        if not text:
            return rx.toast("Please write a comment before posting")
        if not self.selected_task_id:
            return rx.toast("Open a task before commenting")
        import uuid

        target_task_id = self.selected_task_id
        target_title = ""
        for t in self.tasks:
            if t["id"] == target_task_id:
                target_title = t["title"]
                break
        if not target_title:
            return rx.toast("This task no longer exists")
        self.comments.append(
            {
                "id": str(uuid.uuid4())[:6],
                "task_id": target_task_id,
                "author_id": "u1",
                "text": text,
                "timestamp": "just now",
            }
        )
        self._add_activity("commented on", target_title)
        self._add_notification(
            "message_square",
            "comment",
            "You commented on a task",
            f'{target_title} — "{text[:60]}"',
            target_task_id,
            "",
        )
        self.new_comment_text = ""

    @rx.event
    def add_checklist_item(self, form_data: dict):
        text = form_data.get("checklist_text", "").strip()
        if not text:
            return rx.toast("Add some text for the checklist item")
        if not self.selected_task_id:
            return rx.toast("Open a task to add checklist items")
        import uuid

        item: ChecklistItem = {
            "id": str(uuid.uuid4())[:6],
            "text": text,
            "done": False,
        }
        items = list(self.checklists.get(self.selected_task_id, []))
        items.append(item)
        self.checklists[self.selected_task_id] = items
        if items:
            done_count = len([i for i in items if i["done"]])
            pct = int(done_count / len(items) * 100)
            for i, t in enumerate(self.tasks):
                if t["id"] == self.selected_task_id:
                    self.tasks[i] = {**t, "progress": pct}
                    break
        self.new_checklist_text = ""

    @rx.event
    def toggle_checklist_item(self, task_id: str, item_id: str):
        items = self.checklists.get(task_id, [])
        new_items: list[ChecklistItem] = []
        for it in items:
            if it["id"] == item_id:
                new_items.append(
                    {"id": it["id"], "text": it["text"], "done": not it["done"]}
                )
            else:
                new_items.append(it)
        self.checklists[task_id] = new_items
        if new_items:
            done_count = len([i for i in new_items if i["done"]])
            pct = int(done_count / len(new_items) * 100)
            for i, t in enumerate(self.tasks):
                if t["id"] == task_id:
                    self.tasks[i] = {**t, "progress": pct}
                    break

    @rx.event
    def delete_checklist_item(self, task_id: str, item_id: str):
        items = self.checklists.get(task_id, [])
        self.checklists[task_id] = [i for i in items if i["id"] != item_id]

    @rx.event
    def update_task_status(self, task_id: str, new_status: str):
        for i, t in enumerate(self.tasks):
            if t["id"] == task_id:
                old = t["status"]
                self.tasks[i] = {**t, "status": new_status}
                if old != new_status:
                    self._add_activity(f"moved to {new_status}", t["title"])
                break

    @rx.event
    def update_task_priority(self, task_id: str, priority: str):
        for i, t in enumerate(self.tasks):
            if t["id"] == task_id:
                self.tasks[i] = {**t, "priority": priority}
                break

    @rx.event
    def update_task_assignee(self, task_id: str, assignee_id: str):
        for i, t in enumerate(self.tasks):
            if t["id"] == task_id:
                self.tasks[i] = {**t, "assignee_id": assignee_id}
                break

    @rx.event
    def save_task_edits(self, form_data: dict):
        title = form_data.get("title", "").strip()
        if not title:
            return rx.toast("Title cannot be empty")
        if not self.selected_task_id:
            return rx.toast("No task is currently open")
        updated = False
        for i, t in enumerate(self.tasks):
            if t["id"] == self.selected_task_id:
                self.tasks[i] = {
                    **t,
                    "title": title,
                    "description": form_data.get(
                        "description", t["description"]
                    ),
                    "priority": form_data.get("priority", t["priority"]),
                    "status": form_data.get("status", t["status"]),
                    "due_date": form_data.get("due_date", t["due_date"]),
                    assignee_id: form_data.get("assignee_id", t["assignee_id"]),
                }
                updated = True
                break
        if not updated:
            return rx.toast("This task could not be found")
        self._add_activity("updated task", title)
        self._add_notification(
            "pencil",
            "project",
            "Task updated",
            f"{title} was updated with new details.",
            self.selected_task_id,
            "",
        )
        return rx.toast(f"Saved '{title}'")

    @rx.event
    def delete_task(self, task_id: str):
        title = ""
        for t in self.tasks:
            if t["id"] == task_id:
                title = t["title"]
                break
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.comments = [c for c in self.comments if c["task_id"] != task_id]
        self.show_task_dialog = False
        if title:
            self._add_activity("deleted task", title)
            return rx.toast(f"Deleted '{title}'")

    @rx.event
    def add_task(self, form_data: dict):
        title = form_data.get("title", "").strip()
        if not title:
            return rx.toast("Please provide a task title")
        import uuid

        status = form_data.get("status", "To Do") or "To Do"
        if status not in self.columns:
            status = "To Do"
        priority = form_data.get("priority", "Medium") or "Medium"
        if priority not in ("Low", "Medium", "High"):
            priority = "Medium"
        new_task: Task = {
            "id": str(uuid.uuid4())[:8],
            "project_id": form_data.get("project_id", self.current_project_id)
            or self.current_project_id,
            "title": title,
            "description": form_data.get("description", ""),
            "status": status,
            "priority": priority,
            "due_date": form_data.get("due_date", ""),
            "assignee_id": form_data.get("assignee_id", "u1") or "u1",
            progress: 0,
            tags: [],
        }
        self.tasks.append(new_task)
        self._add_activity("created task", title)
        assignee_name = self.user_map.get(new_task["assignee_id"], "Team")
        self._add_notification(
            "user-plus",
            "assignment",
            f"Task assigned to {assignee_name}",
            f"{title} — priority {new_task['priority']}",
            new_task["id"],
            new_task["project_id"],
        )
        self.show_new_task_dialog = False
        return rx.toast(f"Task '{title}' created")
