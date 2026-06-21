from abc import ABC, abstractmethod
from typing import Dict


class ThirdPartyYouTubeLib(ABC):
    """The Service Interface defines operations that the service and proxy share."""

    @abstractmethod
    def get_video_info(self, video_id: str) -> str:
        """Retrieves video information."""
        pass

    @abstractmethod
    def download_video(self, video_id: str) -> str:
        """Downloads video bytes."""
        pass


class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    """The Real Service providing actual business logic execution."""

    def __init__(self) -> None:
        self.download_count = 0
        self.info_count = 0

    def get_video_info(self, video_id: str) -> str:
        self.info_count += 1
        return f"YouTube video info for: {video_id}"

    def download_video(self, video_id: str) -> str:
        self.download_count += 1
        return f"Downloading video bytes for: {video_id}"


class CachedYouTubeClass(ThirdPartyYouTubeLib):
    """The Proxy class wrapper providing caching capabilities."""

    def __init__(self, service: ThirdPartyYouTubeClass) -> None:
        """Initializes the proxy wrapper.

        Args:
            service: The real service instance.
        """
        self._service = service
        self._info_cache: Dict[str, str] = {}
        self._download_cache: Dict[str, str] = {}

    def get_video_info(self, video_id: str) -> str:
        """Caches and returns video info request results."""
        if video_id not in self._info_cache:
            self._info_cache[video_id] = self._service.get_video_info(video_id)
        return f"Proxy: {self._info_cache[video_id]} (Cache Hit)"

    def download_video(self, video_id: str) -> str:
        """Caches and returns video download request results."""
        if video_id not in self._download_cache:
            self._download_cache[video_id] = self._service.download_video(video_id)
        return f"Proxy: {self._download_cache[video_id]} (Cache Hit)"
