from patterns.structural.bridge.pattern import (
    TV,
    AdvancedRemoteControl,
    Radio,
    RemoteControl,
)


def test_standard_remote_with_tv() -> None:
    """Verifies that the standard remote control works on a TV device."""
    tv = TV()
    remote = RemoteControl(tv)

    assert not tv.is_enabled()
    assert remote.toggle_power() == "Power toggled: Device is now ON"
    assert tv.is_enabled()

    assert tv.get_volume() == 50
    assert remote.volume_up() == "Volume increased to 60"
    assert tv.get_volume() == 60

    assert remote.volume_down() == "Volume decreased to 50"
    assert tv.get_volume() == 50


def test_advanced_remote_with_radio() -> None:
    """Verifies that the advanced remote control works on a Radio device."""
    radio = Radio()
    remote = AdvancedRemoteControl(radio)

    assert not radio.is_enabled()
    assert remote.toggle_power() == "Power toggled: Device is now ON"
    assert radio.is_enabled()

    assert radio.get_volume() == 30
    assert remote.mute() == "Device muted"
    assert radio.get_volume() == 0
