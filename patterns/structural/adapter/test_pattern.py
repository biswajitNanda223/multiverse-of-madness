from patterns.structural.adapter.pattern import Adaptee, Adapter, Target


def test_target_default_behavior() -> None:
    """Verifies that the standard Target works normally."""
    target = Target()
    assert target.request() == "Target: The default target's behavior."


def test_adaptee_raw_behavior() -> None:
    """Verifies that the Adaptee returns raw reversed content."""
    adaptee = Adaptee()
    assert (
        adaptee.specific_request() == ".retpada na sdeen sihT .roivaheb eetpada laicepS"
    )


def test_adapter_translation() -> None:
    """Verifies that the Adapter correctly wraps and translates the Adaptee output."""
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    expected = "Adapter: (TRANSLATED) Special adaptee behavior. This needs an adapter."
    assert adapter.request() == expected
