from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, Field, field_validator

PROFILES_FOLDER = Path('Profiles').resolve()

class Settings(BaseModel):
    use_hardware_encoding: Optional[bool] = Field(True, alias='use hardware encoding')
    use_hardware_decoding: Optional[bool] = Field(True, alias='use hardware decoding')
    detect_hdr: Optional[bool] = Field(True, alias='detect HDR')
    """If HDR is present in the video track, preserve it by switching to the 10-bit or 12-bit profile, whichever is used by the source. HDR tonemapping and dealing with Dolby Vision is far beyond the scope of this project."""


class General(BaseModel):
    preset: Optional[str] = ''
    """Use this preset for all unset settings."""

class Audio(BaseModel):
    tracks: Optional[list[int]] = []
    """If set to all or unset, all tracks are used."""

    passthru_tracks_when_able: Optional[bool] = Field(True, alias='passthru tracks when able')
    """If the track's codec supports passthrough, and it isn't in the blacklist, pass it through with HandBrake's `copy` mode."""
    
    encoder_blacklist: Optional[list[str]] = Field([], alias='encoder blacklist')
    """
    If any track uses one of these codecs, they will be re-encoded with the fallback codec.

    Allowed codecs: av_aac, aac, ac3, eac3, truehd, mp3, opus, vorbis, flac16, flac24, alac16, alac24

    If unset, no codecs are blacklisted.
    """

    encoder_fallback: Optional[str] = Field('aac', alias='encoder fallback')
    """If unset, aac is used."""

    mixdown: Optional[bool] = False


    @field_validator('tracks', mode='before')
    @classmethod
    def tracks_coerce_all_to_empty_list(cls, value: Any) -> Any:
        return [] if value == 'all' else value
    

class Video(BaseModel):
    codec: Optional[str] = 'x265'
    """
    Set allowed encoder (codec and target, i.e. software/hardware), which preferred one on top. Hardware-specific encoder (such as those using NVENC) are automatically used, if available and enabled. If HDR is detected (10-bit or 12-bit), the corresponding encoder will be used.
    
    If unset, the x265 is used.
    """

    fps: Optional[int] = -1
    """Set video framerate. Setting to "source" will have BatchCode detect the source file's framerate and tell HandBrake to use that."""

    peak_bitrate: Optional[int] = Field(-1, alias='peak bitrate')

    @field_validator('fps', mode='before')
    @classmethod
    def fps_coerce_source_to_illegal_fps_number(cls, value: Any) -> Any:
        return -1 if value == 'source' else value
    

class Profile(BaseModel):
    settings: Optional[Settings]
    general: Optional[General]
    audio: Optional[Audio]
    video: Optional[Video]

    @classmethod
    def load(cls, profile_name: str):
        default = _load_profile_raw('Default')
        profile = _load_profile_raw(profile_name)

        combined = _combine_dicts(default, profile)

        return cls.model_validate(combined)




def _combine_dicts(
        parent_dict: dict[str, Any],
        additional_dict: dict[str, Any],
    ) -> dict[str, Any]:
    for k,v in additional_dict.items():
        if (
            isinstance(v, dict)
            and parent_dict.get(k, {})
        ):
            v = _combine_dicts(parent_dict[k], v)
        parent_dict[k] = v

    return parent_dict


def _load_profile_raw(profile_name: str) -> dict[str, Any]:
    """Load the profile settings file directly, without dealing with defaults or validation."""
    with open(PROFILES_FOLDER / f'{profile_name}.yml', 'r') as f:
        return yaml.safe_load(f)


# with open('Profiles/Default.yml', 'r') as f:
#     profile = Profile.model_validate(yaml.safe_load(f))
#     print(profile)

if __name__ == '__main__':
    profile = Profile.load('1080p')
    print(profile)