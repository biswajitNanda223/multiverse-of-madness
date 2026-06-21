from patterns.structural.proxy.pattern import CachedYouTubeClass, ThirdPartyYouTubeClass


def test_proxy_caching() -> None:
    """Verifies that the proxy caches results and prevents redundant service queries."""
    service = ThirdPartyYouTubeClass()
    proxy = CachedYouTubeClass(service)

    # First call: query service
    info1 = proxy.get_video_info("vid1")
    assert service.info_count == 1
    assert "vid1" in info1

    # Second call: fetch from cache
    info2 = proxy.get_video_info("vid1")
    assert service.info_count == 1  # count has not increased
    assert info1 == info2

    # Download test
    d1 = proxy.download_video("vid1")
    assert service.download_count == 1
    assert "vid1" in d1

    d2 = proxy.download_video("vid1")
    assert service.download_count == 1  # count has not increased
    assert d1 == d2
