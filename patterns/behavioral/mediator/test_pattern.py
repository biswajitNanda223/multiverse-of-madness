from patterns.behavioral.mediator.pattern import AuthenticationMediator, Button, TextBox


def test_independent_components() -> None:
    """Verifies default behavior of components without a mediator."""
    button = Button()
    textbox = TextBox()

    assert button.click() == "Button clicked."
    assert textbox.set_text("Hello") == "TextBox set to 'Hello'."


def test_mediator_validation_flow() -> None:
    """Verifies that the mediator blocks logins with empty textboxes and allows valid ones."""
    button = Button()
    textbox = TextBox()
    mediator = AuthenticationMediator(button, textbox)

    # Click with empty TextBox -> fails validation
    res1 = button.click()
    assert "Button clicked." in res1
    assert "Mediator: Validation failed. Textbox is empty." in res1

    # Edit TextBox -> triggers update notify
    res2 = textbox.set_text("john_doe")
    assert "TextBox set to 'john_doe'." in res2
    assert "Mediator: Input changed. Validation status reset." in res2

    # Click with valid TextBox -> logs in
    res3 = button.click()
    assert "Button clicked." in res3
    assert "Mediator: Logging in user with input 'john_doe'." in res3
