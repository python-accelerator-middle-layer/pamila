from typing import Any, Dict, List, Literal, Union

from pydantic import BaseModel, Field

from ..device.simple import FixedWaitTime, SetpointReadbackDiffBase
from ..device.specs import FunctionSpec
from ..middle_layer import PvIdToReprMap
from ..utils import KeyValueTagList, SPositionList


class PamilaDeviceDefinition(BaseModel):
    type: str


class StandardReadbackDeviceDefinition(PamilaDeviceDefinition):
    type: str = "standard_RB"


class SetpointReadbackDiffDefinition(SetpointReadbackDiffBase):
    RB_channel: str


class StandardSetpointDeviceDefinition(PamilaDeviceDefinition):
    type: str = "standard_SP"
    set_wait_method: str = "fixed_wait_time"
    fixed_wait_time: FixedWaitTime = Field(default_factory=FixedWaitTime)
    SP_RB_diff: SetpointReadbackDiffDefinition | None = None


PamilaDeviceDefinitionUnion = Union[
    PamilaDeviceDefinition,
    StandardReadbackDeviceDefinition,
    StandardSetpointDeviceDefinition,
]


class MachineModeSpecContainer(BaseModel):
    LIVE: PamilaDeviceDefinitionUnion | None = None
    DT: PamilaDeviceDefinitionUnion | None = None
    SIM: PamilaDeviceDefinitionUnion | None = None


class GetPVMapping(BaseModel):
    input_pvs: List[str]
    conv_spec_name: str | None = None


class PutPVMapping(BaseModel):
    output_pvs: List[str]
    conv_spec_name: str | None = None
    aux_input_pvs: List[str] | None = None


class PVMapping(BaseModel):
    get: GetPVMapping
    put: PutPVMapping | None = Field(None)


class ChannelSpec(BaseModel):
    handle: Literal["SP", "RB"]
    HiLv_reprs: List[str]
    ext: PVMapping
    int: PVMapping
    pdev_def: MachineModeSpecContainer
    s_list_key: str = "element"


class _SPosLists(dict):
    def __init__(self):
        super().__init__()
        self["element"] = None


class PamilaElementDefinition(BaseModel):
    s_lists: Dict[str, SPositionList | None] = Field(default_factory=_SPosLists)
    tags: KeyValueTagList = Field(default_factory=KeyValueTagList)
    pvid_to_repr_map: PvIdToReprMap = Field(default_factory=PvIdToReprMap)
    repr_units: Dict[str, str] = Field(default_factory=dict)
    func_specs: Dict[str, FunctionSpec] = Field(default_factory=dict)
    channel_map: Dict[str, ChannelSpec] = Field(
        default_factory=dict
    )  # channel := (field/repr, handle)
