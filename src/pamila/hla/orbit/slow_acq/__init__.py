from . import acquire, library_output, plot
from ....hla import _get_flow, _get_flow_names, extract_hla_path
from ....machine import Machine

FLOW_DEFS = {
    "library": [acquire.Stage, library_output.Stage],
    "standalone": [acquire.Stage, plot.Stage],
}


def get_flow_names():
    return _get_flow_names(FLOW_DEFS)


def get_flow(flow_type: str, machine: Machine):
    # For each machine, need different default options. (No need to separate for
    # different machine modes)

    hla_name = extract_hla_path(__name__)

    return _get_flow(hla_name, flow_type, machine, FLOW_DEFS)
