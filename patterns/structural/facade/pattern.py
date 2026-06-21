from typing import Union


class VideoFile:
    """Subsystem class representing a video file."""

    def __init__(self, filename: str) -> None:
        self.filename = filename


class OggCompressionCodec:
    """Subsystem class for OGG codec."""

    def __init__(self) -> None:
        self.codec_type = "ogg"


class MPEG4CompressionCodec:
    """Subsystem class for MP4 codec."""

    def __init__(self) -> None:
        self.codec_type = "mp4"


class CodecFactory:
    """Subsystem class to identify codecs."""

    @staticmethod
    def extract(file: VideoFile) -> str:
        """Extracts codec details based on file format extension."""
        if file.filename.endswith(".mp4"):
            return "mp4"
        return "ogg"


class BitrateReader:
    """Subsystem class for reading and converting video byte buffers."""

    @staticmethod
    def read(file: VideoFile, source_codec: str) -> str:
        return f"Buffer({file.filename}, source: {source_codec})"

    @staticmethod
    def convert(buffer: str, dest_codec_type: str) -> str:
        return f"Converted({buffer}) to {dest_codec_type}"


class AudioMixer:
    """Subsystem class for adjusting audio syncs and overlays."""

    def fix(self, result: str) -> str:
        return f"{result} with mixed audio"


# Facade
class VideoConverterFacade:
    """Facade class wrapping the complex video conversion subsystem pipeline."""

    def convert_video(self, filename: str, format: str) -> str:
        """Converts a video file to the target format (mp4/ogg) using the internal subsystem.

        Args:
            filename: The name of the input video file.
            format: Target format (mp4 or ogg).

        Returns:
            The final confirmation message and status string of the processed video.
        """
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)

        destination_codec: Union[MPEG4CompressionCodec, OggCompressionCodec]
        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(file, source_codec)
        converted_buffer = BitrateReader.convert(buffer, destination_codec.codec_type)
        final_video = AudioMixer().fix(converted_buffer)

        return f"VideoConverterFacade: conversion completed. {final_video}"
