from abc import ABC, abstractmethod


# Implementation Interface
class Device(ABC):
    """The Implementation declares the interface for all concrete devices."""

    @abstractmethod
    def is_enabled(self) -> bool:
        """Checks if the device is powered on."""
        pass

    @abstractmethod
    def enable(self) -> None:
        """Powers on the device."""
        pass

    @abstractmethod
    def disable(self) -> None:
        """Powers off the device."""
        pass

    @abstractmethod
    def get_volume(self) -> int:
        """Gets current volume."""
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        """Sets volume percentage (0 to 100)."""
        pass


# Concrete Implementations
class Radio(Device):
    """Concrete Implementation for a Radio device."""

    def __init__(self) -> None:
        self._enabled = False
        self._volume = 30

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        self._volume = max(0, min(100, percent))


class TV(Device):
    """Concrete Implementation for a TV device."""

    def __init__(self) -> None:
        self._enabled = False
        self._volume = 50

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        self._volume = max(0, min(100, percent))


# Abstraction
class RemoteControl:
    """The Abstraction provides high-level control logic and delegates to a Device."""

    def __init__(self, device: Device) -> None:
        """Initializes the RemoteControl.

        Args:
            device: The Device implementation instance to control.
        """
        self.device = device

    def toggle_power(self) -> str:
        """Toggles the power state of the device."""
        if self.device.is_enabled():
            self.device.disable()
            return "Power toggled: Device is now OFF"
        else:
            self.device.enable()
            return "Power toggled: Device is now ON"

    def volume_down(self) -> str:
        """Decreases volume by 10%."""
        current = self.device.get_volume()
        self.device.set_volume(current - 10)
        return f"Volume decreased to {self.device.get_volume()}"

    def volume_up(self) -> str:
        """Increases volume by 10%."""
        current = self.device.get_volume()
        self.device.set_volume(current + 10)
        return f"Volume increased to {self.device.get_volume()}"


# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    """A Refined Abstraction that adds new capabilities like muting."""

    def mute(self) -> str:
        """Mutes the device volume completely (0%)."""
        self.device.set_volume(0)
        return "Device muted"
