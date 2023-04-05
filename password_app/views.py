import string
import secrets
import pyperclip
from django.shortcuts import render


def password_generator_view(request):
    if request.method == "POST":
        length = request.POST.get("length") or 5
        nums = request.POST.get("nums") == "on"
        chars = request.POST.get("chars") == "on"

        # Generate a random password using the characters in the alphabet
        alphabet = string.ascii_letters
        if nums:
            alphabet += string.digits
        if chars:
            alphabet += string.punctuation

        secrets_password = "".join(secrets.choice(alphabet) for i in range(int(length)))

        # Check password strength and set alert message
        if len(secrets_password) >= 20 and any(
            c in string.punctuation for c in secrets_password
        ):
            alert_message = "Password Strength: Strong"
            alert_class = "alert-success"
        elif len(secrets_password) >= 10:
            alert_message = "Password Strength: Medium"
            alert_class = "alert-warning"
        else:
            alert_message = (
                "Password Strength: Weak. Please try again with more characters."
            )
            alert_class = "alert-danger"

        # Copy the password to the clipboard
        pyperclip.copy(secrets_password)

        return render(
            request,
            "pass_gen.html",
            {
                "password": secrets_password,
                "alert_message": alert_message,
                "alert_class": alert_class,
            },
        )

    return render(request, "pass_gen.html")
