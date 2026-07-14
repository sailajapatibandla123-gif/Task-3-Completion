import reflex as rx


class AuthState(rx.State):
    is_authenticated: bool = False
    auth_mode: str = "login"
    user_name: str = "Alex Morgan"
    user_email: str = "alex@codealpha.tech"
    user_role: str = "Product Lead"
    error_message: str = ""

    @rx.event
    def set_mode(self, mode: str):
        self.auth_mode = mode
        self.error_message = ""

    @rx.event
    def login(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or "@" not in email:
            self.error_message = "Please enter a valid email address."
            return
        if len(password) < 4:
            self.error_message = "Password must be at least 4 characters."
            return
        self.user_email = email
        display = email.split("@")[0].replace(".", " ").title()
        self.user_name = display if display else "Team Member"
        self.error_message = ""
        self.is_authenticated = True
        return rx.toast(f"Welcome back, {self.user_name}!")

    @rx.event
    def register(self, form_data: dict):
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        confirm = form_data.get("confirm", "").strip()
        role = form_data.get("role", "Team Member").strip() or "Team Member"
        if not name:
            self.error_message = "Please enter your full name."
            return
        if not email or "@" not in email:
            self.error_message = "Please enter a valid email address."
            return
        if len(password) < 4:
            self.error_message = "Password must be at least 4 characters."
            return
        if password != confirm:
            self.error_message = "Passwords do not match."
            return
        self.user_name = name
        self.user_email = email
        self.user_role = role
        self.error_message = ""
        self.is_authenticated = True
        return rx.toast(f"Account created — welcome to CodeAlpha, {name}!")

    @rx.event
    def demo_login(self):
        self.user_name = "Alex Morgan"
        self.user_email = "alex@codealpha.tech"
        self.user_role = "Product Lead"
        self.error_message = ""
        self.is_authenticated = True
        return rx.toast("Signed in as Alex Morgan (demo)")

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.error_message = ""
        self.auth_mode = "login"
        return rx.toast("You've been signed out.")
