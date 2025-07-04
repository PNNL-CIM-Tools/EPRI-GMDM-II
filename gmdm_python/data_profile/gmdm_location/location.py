from __future__ import annotations
import logging
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from cimgraph.data_profile.identity import Identity, stereotype
from cimgraph.data_profile.units import CIMUnit, UnitSymbol, UnitMultiplier
_log = logging.getLogger(__name__)
'''
Annotated CIMantic Graphs data profile for GeoLocation
Generated by CIMTool http://cimtool.org
'''

class CIMStereotype(Enum):
    Attribute = "Attribute"
    ByReference = "ByReference"
    Concrete = "Concrete"
    Description = "Description"
    GB = "GB"
    NC = "NC"
    OfAggregate = "OfAggregate"
    Primitive = "Primitive"
    ShadowExtension = "ShadowExtension"
    profcim = "profcim"

BASE_URI = 'http://www.ucaiug.org/gmdm_location#'
ONTOLOGY_URI = 'http://iec.ch/TC57/CIM101#'

@dataclass(repr=False)
class Identity(Identity):
    '''
    This is a root class to provide common identification for all classes.
    '''

    identifier: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A universally unique object identifier. Used to uniquely identify persistent
    objects between CIM messages.
    '''
    
@dataclass(repr=False)
class GeometricElement(Identity):
    '''
    Exists solely as the parent of the separate geometry types (Point, Line,
    Circle, Polygon) in order to create an xsd Choice between the types.
    '''

@stereotype(CIMStereotype.ShadowExtension)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class PositionPoint(GeometricElement):
    '''
    Set of spatial coordinates that determine a point, defined in the coordinate
    system specified in 'Location.CoordinateSystem'. Use a single position
    point instance to describe a point-oriented location. Use a sequence of
    position points to describe a line-oriented object (physical location of
    non-point oriented objects like cables or lines), or area of an object
    (like a substation or a geographical zone - in this case, have first and
    last position point with the same values).
    '''

    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://epri.com/gmdm#',
        })
    '''
    '''
    
    xPosition: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    X axis position.
    '''
    
    yPosition: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Y axis position.
    '''
    
    zPosition: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    (if applicable) Z axis position.
    '''
    
    Location: Optional[Location] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'inverse': 'Location.PositionPoints',
        'namespace': 'http://epri.com/gmdm#',
        })
    '''
    '''
    
@dataclass(repr=False)
class IdentifiedObject(Identity):
    '''
    This is a class that provides common identification for all classes needing
    identification and naming attributes.
    '''

    mRID: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Master resource identifier issued by a model authority. The mRID is
    unique within an exchange context. Global uniqueness is easily achieved
    by using a UUID, as specified in IETF RFC 4122, for the mRID. The use
    of UUID is strongly recommended.
    For CIMXML data files in RDF syntax conforming to IEC 61970-552, the
    mRID is mapped to rdf:ID or rdf:about attributes that identify CIM
    object elements.
    '''
    
    description: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The description is a free human readable text describing or naming
    the object. It may be non unique and may not correlate to a naming
    hierarchy.
    '''
    
    name: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The name is any free human readable and possibly non unique text naming
    the object.
    '''
    
@dataclass(repr=False)
class CoordinateSystem(IdentifiedObject):
    '''
    Coordinate reference system.
    '''

    Location: list[Location] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'Location.CoordinateSystem',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    All locations described with position points in this coordinate system.
    '''
    
@dataclass(repr=False)
class Location(IdentifiedObject):
    '''
    The place, scene, or point of something where someone or something has
    been, is, and/or will be at a given moment in time. It can be defined with
    one or more position points (coordinates) in a given coordinate system.
    '''

    PositionPoints: list[PositionPoint] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'PositionPoint.Location',
        'namespace': 'http://epri.com/gmdm#',
        })
    '''
    '''
    
    PowerSystemResources: list[PowerSystemResource] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'PowerSystemResource.Location',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    All power system resources at this location.
    '''
    
    CoordinateSystem: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'inverse': 'CoordinateSystem.Location',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Coordinate system used to describe position points of this location.
    '''
    
@dataclass(repr=False)
class PowerSystemResource(IdentifiedObject):
    '''
    A power system resource (PSR) can be an item of equipment such as a switch,
    an equipment container containing many individual items of equipment such
    as a substation, or an organisational entity such as sub-control area.
    Power system resources can have measurements associated.
    '''

    Location: Optional[Location] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'inverse': 'Location.PowerSystemResources',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Location of this power system resource.
    '''
    
@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class ACLineSegmentPhase(PowerSystemResource):
    '''
    A line segment phase represents one phase (or optionally the neutral) of
    an alternating current line segment.
    Under most circumstances there is not a line segment phase for the neutral.
    However, if a wire assembly is being used and it does not specify phase,
    a line segment phase must exist for each position in the assembly (including
    the neutral).
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class EnergyConsumerPhase(PowerSystemResource):
    '''
    A single phase of an energy consumer.
    '''

@dataclass(repr=False)
class Equipment(PowerSystemResource):
    '''
    The parts of a power system that are physical devices, electronic or mechanical.
    '''

@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class ConductingEquipment(Equipment):
    '''
    The parts of the AC power system that are designed to carry current or
    that are conductively connected through terminals.
    '''

@dataclass(repr=False)
class Conductor(ConductingEquipment):
    '''
    Combination of conducting material with consistent electrical characteristics,
    building a single electrical system, used to carry current between points
    in the power system.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class ACLineSegment(Conductor):
    '''
    A line segment is a conductor or combination of conductors, with consistent
    electrical characteristics along its length, building a single electrical
    system that carries alternating current between two points in the power
    system.
    The BaseVoltage at the two ends of a line segment shall have the same BaseVoltage.nominalVoltage.
    However, boundary lines may have slightly different BaseVoltage.nominalVoltages
    and variation is allowed. Larger voltage difference in general requires
    use of an equivalent branch.
    Line segment impedances can be either directly described in electrical
    terms or physical line detail can be provided from which impedances can
    be calculated.
    <b>Directly described impedances</b>
    For symmetrical, transposed three phase line segments, it is sufficient
    to use attributes of the line segment, which describe impedances and admittances
    for the entire length of the line segment. Additionally, line segment impedances
    can be computed by using line segment length and associated per length
    impedances.
    Unbalanced modeling of impedances is supported by the per length phase
    impedance matrix (PerLengthPhaseImpedance) in conjunction with phase-to-sequence
    number mapping supplied by either ACLineSegmentPhase or WirePosition. The
    sequence numbers are referenced by the row and column attributes of the
    per length phase impedance matrix. This method enables single-phase and
    two-phase line segments, and transpositions of phases, to be described
    using the same per length phase impedance matrix. The length of the line
    segment is used in the computation of total impedance values for the line
    segment.
    <b>Line detail characteristics</b>
    There are three approaches to providing line detail and all use WireAssembly
    to supply line positions:
    <ul>
    <li>Option 1 - WireAssembly supplies only line positions. ACLineSegmentPhase
    points to wire type and intraphase spacing and supplies the phase-to-sequence
    number mapping.</li>
    <li>Option 2 - WireAssembly supplies line position and, for each position,
    also supplies wire type and intraphase spacing. ACLineSegmentPhase supplies
    the phase-to-sequence number mapping.</li>
    <li>Option 3 - WireAssembly supplies line position and, for each position,
    also supplies wire type and intraphase spacing and phase. WireAssembly
    therefore supplies the phase-to-sequence number mapping and ACLineSegmentPhase
    is not needed.</li>
    </ul>
    '''

@dataclass(repr=False)
class Connector(ConductingEquipment):
    '''
    A conductor, or group of conductors, with negligible impedance, that serve
    to connect other conducting equipment within a single substation and are
    modelled with a single logical terminal.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class BusbarSection(Connector):
    '''
    A conductor, or group of conductors, with negligible impedance, that serve
    to connect other conducting equipment within a single substation. The BusbarSection
    class is intended to represent physical parts of bus bars no matter how
    that bus bar is constructed.
    Voltage measurements are typically obtained from voltage transformers that
    are connected to busbar sections. A bus bar section may have many physical
    terminals but for analysis is modelled with exactly one logical terminal.
    '''

@dataclass(repr=False)
class EnergyConnection(ConductingEquipment):
    '''
    A connection of energy generation or consumption on the power system model.
    '''

@stereotype(CIMStereotype.NC)
@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class EnergyConsumer(EnergyConnection):
    '''
    Generic user of energy - a point of consumption on the power system model.
    EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning
    only if there is no LoadResponseCharacteristic associated with EnergyConsumer
    or if LoadResponseCharacteristic.exponentModel is set to False.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class EnergySource(EnergyConnection):
    '''
    A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    '''

@dataclass(repr=False)
class RegulatingCondEq(EnergyConnection):
    '''
    A type of conducting equipment that can regulate a quantity (i.e. voltage
    or flow) at a specific point in the network.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class PowerElectronicsConnection(RegulatingCondEq):
    '''
    A connection to the AC network for energy production or consumption that
    uses power electronics rather than rotating machines.
    '''

@dataclass(repr=False)
class RotatingMachine(RegulatingCondEq):
    '''
    A rotating machine which may be used as a generator or motor.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class AsynchronousMachine(RotatingMachine):
    '''
    A rotating machine whose shaft rotates asynchronously with the electrical
    field. Also known as an induction machine with no external connection to
    the rotor windings, e.g. squirrel-cage induction machine.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class SynchronousMachine(RotatingMachine):
    '''
    An electromechanical device that operates with shaft rotating synchronously
    with the network. It is a single machine operating either as a generator
    or synchronous condenser or pump.
    '''

@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class ShuntCompensator(RegulatingCondEq):
    '''
    A shunt capacitor or reactor or switchable bank of shunt capacitors or
    reactors. A section of a shunt compensator is an individual capacitor or
    reactor. A negative value for bPerSection indicates that the compensator
    is a reactor. ShuntCompensator is a single terminal device. Ground is implied.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class LinearShuntCompensator(ShuntCompensator):
    '''
    A linear shunt compensator has banks or sections with equal admittance
    values.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class PowerTransformer(ConductingEquipment):
    '''
    An electrical device consisting of two or more coupled windings, with or
    without a magnetic core, for introducing mutual coupling between electric
    circuits. Transformers can be used to control voltage and phase shift (active
    power flow).
    A power transformer may be composed of separate transformer tanks that
    need not be identical.
    A power transformer can be modelled with or without tanks and is intended
    for use in both balanced and unbalanced representations. A power transformer
    typically has two terminals, but may have one (grounding), three or more
    terminals.
    The inherited association ConductingEquipment.BaseVoltage should not be
    used. The association from TransformerEnd to BaseVoltage should be used
    instead.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class SeriesCompensator(ConductingEquipment):
    '''
    A Series Compensator is a series capacitor or reactor or an AC transmission
    line without charging susceptance. It is a two terminal device.
    '''

@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class Switch(ConductingEquipment):
    '''
    A generic device designed to close, or open, or both, one or more electric
    circuits. All switches are two terminal devices including grounding switches.
    The ACDCTerminal.connected at the two sides of the switch shall not be
    considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen
    and .locked are relevant.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Disconnector(Switch):
    '''
    A mechanical switching device which provides, in the open position, an
    isolating distance in accordance with specified requirements.
    A disconnector is capable of opening and closing a circuit when either
    negligible current is broken or made, or when no significant change in
    the voltage across the terminals of each of the poles of the disconnector
    occurs. It is also capable of carrying currents under normal circuit conditions
    and carrying for a specified time currents under abnormal conditions such
    as those of short circuit.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Fuse(Switch):
    '''
    An overcurrent protective device with a circuit opening fusible part that
    is heated and severed by the passage of overcurrent through it. A fuse
    is considered a switching device because it breaks current.
    '''

@stereotype(CIMStereotype.GB)
@dataclass(repr=False)
class ProtectedSwitch(Switch):
    '''
    A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Breaker(ProtectedSwitch):
    '''
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal circuit conditions and also making, carrying for
    a specified time, and breaking currents under specified abnormal circuit
    conditions e.g. those of short circuit.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class LoadBreakSwitch(ProtectedSwitch):
    '''
    A mechanical switching device capable of making, carrying, and breaking
    currents under normal operating conditions.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Recloser(ProtectedSwitch):
    '''
    Pole-mounted fault interrupter with built-in phase and ground relays, current
    transformer (CT), and supplemental controls.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Sectionaliser(Switch):
    '''
    Automatic switch that will lock open to isolate a faulted section. It may,
    or may not, have load breaking capability. Its primary purpose is to provide
    fault sectionalising at locations where the fault current is either too
    high, or too low, for proper coordination of fuses.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class TransformerTank(Equipment):
    '''
    An assembly of two or more coupled windings that transform electrical power
    between voltage levels. These windings are bound on a common core and placed
    in the same tank. Transformer tank can be used to model both single-phase
    and 3-phase transformers.
    '''

@stereotype(CIMStereotype.OfAggregate)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class EquipmentContainer(PowerSystemResource):
    '''
    A modelling construct to provide a root class for containing equipment.
    '''

@stereotype(CIMStereotype.OfAggregate)
@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class Feeder(EquipmentContainer):
    '''
    A collection of equipment for organizational purposes, used for grouping
    distribution resources.
    The organization a feeder does not necessarily reflect connectivity or
    current operation state.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Line(EquipmentContainer):
    '''
    Contains equipment beyond a substation belonging to a power transmission
    line.
    '''

@stereotype(CIMStereotype.OfAggregate)
@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class Substation(EquipmentContainer):
    '''
    A collection of equipment for purposes other than generation or utilization,
    through which electric energy in bulk is passed for the purposes of switching
    or modifying its characteristics.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class PowerElectronicsConnectionPhase(PowerSystemResource):
    '''
    A single phase of a power electronics connection.
    '''

@dataclass(repr=False)
class ShuntCompensatorPhase(PowerSystemResource):
    '''
    Single phase of a multi-phase shunt compensator when its attributes might
    be different per phase.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class LinearShuntCompensatorPhase(ShuntCompensatorPhase):
    '''
    A per phase linear shunt compensator has banks or sections with equal admittance
    values.
    '''

@stereotype(CIMStereotype.Description)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class SwitchPhase(PowerSystemResource):
    '''
    Single phase of a multi-phase switch when its attributes might be different
    per phase.
    '''

