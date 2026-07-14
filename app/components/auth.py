import reflex as rx
from app.states.auth_state import AuthState


def feature_bullet(icon: str, title: str, desc: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-4 w-4 text-white"),
            class_name="h-8 w-8 rounded-lg bg-white/20 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-semibold text-white"),
            rx.el.p(desc, class_name="text-xs text-indigo-100 mt-0.5"),
        ),
        class_name="flex items-start gap-3",
    )


def brand_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("square_kanban", class_name="h-6 w-6 text-white"),
                class_name="h-11 w-11 rounded-xl bg-white/15 border border-white/20 flex items-center justify-center",
            ),
            rx.el.div(
                rx.el.p(
                    "CodeAlpha",
                    class_name="text-base font-semibold text-white",
                ),
                rx.el.p("Project Hub", class_name="text-xs text-indigo-100"),
            ),
            class_name="flex items-center gap-3",
        ),
        rx.el.div(
            rx.el.h2(
                "Plan work. Ship projects. Together.",
                class_name="text-3xl font-bold text-white leading-tight",
            ),
            rx.el.p(
                "A collaborative workspace for teams to organize projects, assign tasks, and communicate in one focused place — built for the CodeAlpha internship program.",
                class_name="text-sm text-indigo-100 mt-3 leading-relaxed",
            ),
            class_name="mt-16",
        ),
        rx.el.div(
            feature_bullet(
                "square_kanban",
                "Visual Kanban boards",
                "Move tasks across To Do, In Progress, Review, and Done.",
            ),
            feature_bullet(
                "users",
                "Real team collaboration",
                "Assign work, comment on tasks, and track workload.",
            ),
            feature_bullet(
                "bell",
                "Smart notifications",
                "Get pinged for assignments, mentions, and deadlines.",
            ),
            feature_bullet(
                "chart_no_axes_column",
                "Live analytics",
                "Monitor progress across every active project.",
            ),
            class_name="flex flex-col gap-4 mt-10",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    ["alex", "priya", "diego", "mei"],
                    lambda s: rx.el.img(
                        src="https://api.dicebear.com/9.x/notionists/svg?seed="
                        + s,
                        class_name="h-8 w-8 rounded-full bg-white/20 border-2 border-indigo-600 -ml-2 first:ml-0",
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.p(
                "Trusted by 200+ CodeAlpha interns",
                class_name="text-xs text-indigo-100 ml-1",
            ),
            class_name="flex items-center gap-3 mt-10",
        ),
        class_name="hidden lg:flex flex-col justify-between p-10 bg-gradient-to-br from-indigo-600 via-indigo-700 to-purple-700 w-1/2 min-h-screen relative overflow-hidden",
    )


def field(
    label: str, name: str, type_: str = "text", placeholder: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="text-xs font-semibold text-gray-600 uppercase tracking-wider mb-1.5 block",
        ),
        rx.el.input(
            name=name,
            type=type_,
            placeholder=placeholder,
            required=True,
            class_name="w-full px-3 py-2.5 border border-gray-200 rounded-lg text-sm text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
        ),
    )


def login_form() -> rx.Component:
    return rx.el.form(
        field("Email", "email", "email", "you@codealpha.tech"),
        rx.el.div(class_name="h-3"),
        field("Password", "password", "password", "••••••••"),
        rx.el.div(
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    default_checked=True,
                    class_name="h-3.5 w-3.5 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500",
                ),
                rx.el.span("Remember me", class_name="text-xs text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            rx.el.a(
                "Forgot password?",
                href="#",
                class_name="text-xs font-medium text-indigo-600 hover:text-indigo-700",
            ),
            class_name="flex items-center justify-between mt-3",
        ),
        rx.cond(
            AuthState.error_message != "",
            rx.el.div(
                rx.icon(
                    "triangle_alert",
                    class_name="h-4 w-4 text-rose-500 shrink-0",
                ),
                rx.el.p(
                    AuthState.error_message,
                    class_name="text-sm text-rose-700",
                ),
                class_name="flex items-center gap-2 mt-4 p-3 rounded-lg bg-rose-50 border border-rose-100",
            ),
            rx.fragment(),
        ),
        rx.el.button(
            "Sign in",
            type="submit",
            class_name="w-full mt-5 px-4 py-2.5 rounded-lg bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700 transition-colors",
        ),
        rx.el.button(
            rx.icon("zap", class_name="h-4 w-4"),
            "Continue with demo account",
            type="button",
            on_click=AuthState.demo_login,
            class_name="w-full mt-2 flex items-center justify-center gap-2 px-4 py-2.5 rounded-lg bg-white border border-gray-200 text-gray-700 text-sm font-semibold hover:bg-gray-50",
        ),
        rx.el.p(
            "Don't have an account? ",
            rx.el.button(
                "Sign up",
                type="button",
                on_click=AuthState.set_mode("register"),
                class_name="text-indigo-600 hover:text-indigo-700 font-semibold",
            ),
            class_name="text-sm text-gray-500 text-center mt-6",
        ),
        on_submit=AuthState.login,
        reset_on_submit=False,
    )


def register_form() -> rx.Component:
    return rx.el.form(
        field("Full name", "name", "text", "Jamie Rivera"),
        rx.el.div(class_name="h-3"),
        field("Email", "email", "email", "you@codealpha.tech"),
        rx.el.div(class_name="h-3"),
        rx.el.div(
            rx.el.label(
                "Role",
                class_name="text-xs font-semibold text-gray-600 uppercase tracking-wider mb-1.5 block",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("Product Lead", value="Product Lead"),
                    rx.el.option(
                        "Frontend Engineer", value="Frontend Engineer"
                    ),
                    rx.el.option("Backend Engineer", value="Backend Engineer"),
                    rx.el.option("UX Designer", value="UX Designer"),
                    rx.el.option("QA Engineer", value="QA Engineer"),
                    rx.el.option("DevOps", value="DevOps"),
                    name="role",
                    default_value="Frontend Engineer",
                    class_name="w-full px-3 py-2.5 pr-8 border border-gray-200 rounded-lg text-sm text-gray-800 bg-white appearance-none cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                ),
                class_name="relative",
            ),
        ),
        rx.el.div(class_name="h-3"),
        field("Password", "password", "password", "At least 4 characters"),
        rx.el.div(class_name="h-3"),
        field("Confirm password", "confirm", "password", "Repeat password"),
        rx.cond(
            AuthState.error_message != "",
            rx.el.div(
                rx.icon(
                    "triangle_alert",
                    class_name="h-4 w-4 text-rose-500 shrink-0",
                ),
                rx.el.p(
                    AuthState.error_message,
                    class_name="text-sm text-rose-700",
                ),
                class_name="flex items-center gap-2 mt-4 p-3 rounded-lg bg-rose-50 border border-rose-100",
            ),
            rx.fragment(),
        ),
        rx.el.button(
            "Create account",
            type="submit",
            class_name="w-full mt-5 px-4 py-2.5 rounded-lg bg-indigo-600 text-white text-sm font-semibold hover:bg-indigo-700 transition-colors",
        ),
        rx.el.p(
            "Already have an account? ",
            rx.el.button(
                "Sign in",
                type="button",
                on_click=AuthState.set_mode("login"),
                class_name="text-indigo-600 hover:text-indigo-700 font-semibold",
            ),
            class_name="text-sm text-gray-500 text-center mt-6",
        ),
        on_submit=AuthState.register,
        reset_on_submit=False,
    )


def auth_page() -> rx.Component:
    return rx.el.div(
        brand_panel(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "square_kanban", class_name="h-5 w-5 text-white"
                        ),
                        class_name="h-10 w-10 rounded-lg bg-indigo-600 flex items-center justify-center lg:hidden",
                    ),
                    rx.el.div(
                        rx.el.h1(
                            rx.cond(
                                AuthState.auth_mode == "login",
                                "Welcome back",
                                "Create your account",
                            ),
                            class_name="text-2xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            rx.cond(
                                AuthState.auth_mode == "login",
                                "Sign in to your CodeAlpha workspace to continue.",
                                "Join the CodeAlpha workspace and start collaborating.",
                            ),
                            class_name="text-sm text-gray-500 mt-1",
                        ),
                        class_name="mt-4 lg:mt-0",
                    ),
                    class_name="mb-6",
                ),
                rx.cond(
                    AuthState.auth_mode == "login",
                    login_form(),
                    register_form(),
                ),
                class_name="w-full max-w-md",
            ),
            rx.el.p(
                "© 2025 CodeAlpha • Internship Portfolio Project",
                class_name="text-xs text-gray-400 mt-10",
            ),
            class_name="flex flex-col items-center justify-center flex-1 p-6 lg:p-10 min-h-screen bg-white",
        ),
        class_name="flex min-h-screen w-full font-['Inter'] bg-white",
    )
