from patterns.structural.facade.pattern import VideoConverterFacade


def test_convert_to_mp4() -> None:
    """Verifies that the facade handles conversion from ogg to mp4."""
    facade = VideoConverterFacade()
    result = facade.convert_video("funny_cats.ogg", "mp4")

    expected = (
        "VideoConverterFacade: conversion completed. "
        "Converted(Buffer(funny_cats.ogg, source: ogg)) to mp4 with mixed audio"
    )
    assert result == expected


def test_convert_to_ogg() -> None:
    """Verifies that the facade handles conversion from mp4 to ogg."""
    facade = VideoConverterFacade()
    result = facade.convert_video("movie.mp4", "ogg")

    expected = (
        "VideoConverterFacade: conversion completed. "
        "Converted(Buffer(movie.mp4, source: mp4)) to ogg with mixed audio"
    )
    assert result == expected
