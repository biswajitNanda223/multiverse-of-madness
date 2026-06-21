from patterns.behavioral.observer.pattern import NewsPublisher, NewsSubscriber


def test_observer_subscription_flow() -> None:
    """Verifies standard subscription, notification, and unsubscription logic."""
    publisher = NewsPublisher()

    sub1 = NewsSubscriber("Alice")
    sub2 = NewsSubscriber("Bob")

    publisher.attach(sub1)
    publisher.attach(sub2)

    # Publish news -> both notified
    updates = publisher.publish_news("Breaking News: AI takes over!")
    assert len(updates) == 2
    assert updates[0] == "Subscriber Alice notified: 'Breaking News: AI takes over!'"
    assert updates[1] == "Subscriber Bob notified: 'Breaking News: AI takes over!'"

    # Detach Alice
    publisher.detach(sub1)

    # Publish news again -> only Bob notified
    updates2 = publisher.publish_news("Weather report: It's sunny.")
    assert len(updates2) == 1
    assert updates2[0] == "Subscriber Bob notified: 'Weather report: It's sunny.'"
