class Target:
    """The Target defines the domain-specific interface used by the client code."""

    def request(self) -> str:
        """Standard request handler."""
        return "Target: The default target's behavior."


class Adaptee:
    """The Adaptee contains useful behavior, but its interface is incompatible.

    It returns data in an reversed format, for example.
    """

    def specific_request(self) -> str:
        """Returns data in an incompatible reversed format."""
        return ".retpada na sdeen sihT .roivaheb eetpada laicepS"


class Adapter(Target):
    """The Adapter makes the Adaptee's interface compatible with the Target's."""

    def __init__(self, adaptee: Adaptee) -> None:
        """Initializes the adapter with a specific adaptee.

        Args:
            adaptee: The Adaptee instance.
        """
        self.adaptee = adaptee

    def request(self) -> str:
        """Adapts the specific_request to a standard interface by reversing the text."""
        raw_result = self.adaptee.specific_request()
        # Reverse the string to make it readable
        readable_result = raw_result[::-1]
        return f"Adapter: (TRANSLATED) {readable_result}"
