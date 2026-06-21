from patterns.structural.decorator.pattern import EmailNotifier, SlackDecorator, SMSDecorator


def test_base_notifier() -> None:
    """Verifies standard EmailNotifier output."""
    notifier = EmailNotifier()
    assert notifier.send("Hello") == "Sending Email: Hello"


def test_single_decorator() -> None:
    """Verifies that wrapping with SMSDecorator adds SMS notification."""
    notifier = EmailNotifier()
    sms_notifier = SMSDecorator(notifier)

    assert sms_notifier.send("Hello") == "Sending Email: Hello and Sending SMS: Hello"


def test_nested_decorators() -> None:
    """Verifies multiple stacked decorators (SMS + Slack)."""
    notifier = EmailNotifier()
    sms_notifier = SMSDecorator(notifier)
    slack_sms_notifier = SlackDecorator(sms_notifier)

    expected = "Sending Email: Hello and Sending SMS: Hello and Sending Slack: Hello"
    assert slack_sms_notifier.send("Hello") == expected
