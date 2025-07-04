from __future__ import annotations
import logging
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from cimgraph.data_profile.identity import Identity, stereotype
from cimgraph.data_profile.units import CIMUnit, UnitSymbol, UnitMultiplier
_log = logging.getLogger(__name__)
'''
Annotated CIMantic Graphs data profile for DiagramLayout
Generated by CIMTool http://cimtool.org
'''

class CIMStereotype(Enum):
    Attribute = "Attribute"
    ByReference = "ByReference"
    CIMDatatype = "CIMDatatype"
    Concrete = "Concrete"
    Primitive = "Primitive"
    enumeration = "enumeration"
    profcim = "profcim"

BASE_URI = 'http://www.ucaiug.org/gmdm_diagram_layout#'
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
    
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class DiagramObjectGluePoint(Identity):
    '''
    This is used for grouping diagram object points from different diagram
    objects that are considered to be glued together in a diagram even if they
    are not at the exact same coordinates.
    '''

    DiagramObjectPoints: list[DiagramObjectPoint] = field(
        default_factory=list,
        metadata={
        'type': 'ByReference',
        'minOccurs': '1',
        'maxOccurs': 'unbounded',
        'inverse': 'DiagramObjectPoint.DiagramObjectGluePoint',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram object glue point is associated with 2 or more object points
    that are considered to be 'glued' together.
    '''
    
@stereotype(CIMStereotype.ByReference)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class DiagramObjectPoint(Identity):
    '''
    A point in a given space defined by 3 coordinates and associated to a diagram
    object. The coordinates may be positive or negative as the origin does
    not have to be in the corner of a diagram.
    '''

    DiagramObjectGluePoint: Optional[DiagramObjectGluePoint] = field(
        default=None,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': '1',
        'inverse': 'DiagramObjectGluePoint.DiagramObjectPoints',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The 'glue' point to which this point is associated.
    '''
    
    sequenceNumber: Optional[int] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The sequence position of the point, used for defining the order of
    points for diagram objects acting as a polyline or polygon with more
    than one point. The attribute shall be a positive value.
    '''
    
    xPosition: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The X coordinate of this point.
    '''
    
    yPosition: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The Y coordinate of this point.
    '''
    
    zPosition: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The Z coordinate of this point.
    '''
    
    DiagramObject: Optional[DiagramObject] = field(
        default=None,
        metadata={
        'type': 'ByReference',
        'minOccurs': '1',
        'maxOccurs': '1',
        'inverse': 'DiagramObject.DiagramObjectPoints',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The diagram object with which the points are associated.
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
    
@stereotype(CIMStereotype.ByReference)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class Diagram(IdentifiedObject):
    '''
    The diagram being exchanged. The coordinate system is a standard Cartesian
    coordinate system and the orientation attribute defines the orientation.
    The initial view related attributes can be used to specify an initial view
    with the x,y coordinates of the diagonal points.
    '''

    DiagramElements: list[DiagramObject] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'DiagramObject.Diagram',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram is made up of multiple diagram objects.
    '''
    
    x1InitialView: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    X coordinate of the first corner of the initial view.
    '''
    
    x2InitialView: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    X coordinate of the second corner of the initial view.
    '''
    
    y1InitialView: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Y coordinate of the first corner of the initial view.
    '''
    
    y2InitialView: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Y coordinate of the second corner of the initial view.
    '''
    
    orientation: Optional[ OrientationKind ] = field(
        default=None,
        metadata={
        'type': 'enumeration Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Coordinate system orientation of the diagram. A positive orientation
    gives standard "right-hand" orientation, with negative orientation
    indicating a "left-hand" orientation. For 2D diagrams, a positive orientation
    will result in X values increasing from left to right and Y values
    increasing from bottom to top. A negative orientation gives the "left-hand"
    orientation (favoured by computer graphics displays) with X values
    increasing from left to right and Y values increasing from top to bottom.
    '''
    
    DiagramStyle: Optional[DiagramStyle] = field(
        default=None,
        metadata={
        'type': 'ByReference',
        'minOccurs': '0',
        'maxOccurs': '1',
        'inverse': 'DiagramStyle.Diagram',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A Diagram may have a DiagramStyle.
    '''
    
@stereotype(CIMStereotype.ByReference)
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class DiagramObject(IdentifiedObject):
    '''
    An object that defines one or more points in a given space. This object
    can be associated with anything that specializes IdentifiedObject. For
    single line diagrams such objects typically include such items as analog
    values, breakers, disconnectors, power transformers, and transmission lines.
    '''

    DiagramObjectPoints: list[DiagramObjectPoint] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'DiagramObjectPoint.DiagramObject',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram object can have 0 or more points to reflect its layout position,
    routing (for polylines) or boundary (for polygons).
    '''
    
    VisibilityLayers: list[VisibilityLayer] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'VisibilityLayer.VisibleObjects',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram object can be part of multiple visibility layers.
    '''
    
    drawingOrder: Optional[int] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The drawing order of this element. The higher the number, the later
    the element is drawn in sequence. This is used to ensure that elements
    that overlap are rendered in the correct order.
    '''
    
    isPolygon: Optional[bool] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Defines whether or not the diagram objects points define the boundaries
    of a polygon or the routing of a polyline. If this value is true then
    a receiving application should consider the first and last points to
    be connected.
    '''
    
    offsetX: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The offset in the X direction. This is used for defining the offset
    from centre for rendering an icon (the default is that a single point
    specifies the centre of the icon).
    The offset is in per-unit with 0 indicating there is no offset from
    the horizontal centre of the icon. -0.5 indicates it is offset by 50%
    to the left and 0.5 indicates an offset of 50% to the right.
    '''
    
    offsetY: Optional[float] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The offset in the Y direction. This is used for defining the offset
    from centre for rendering an icon (the default is that a single point
    specifies the centre of the icon).
    The offset is in per-unit with 0 indicating there is no offset from
    the vertical centre of the icon. The offset direction is dependent
    on the orientation of the diagram, with -0.5 and 0.5 indicating an
    offset of +/- 50% on the vertical axis.
    '''
    
    rotation: Optional[ float | AngleDegrees ] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    Sets the angle of rotation of the diagram object. Zero degrees is pointing
    to the top of the diagram. Rotation is clockwise. DiagramObject.rotation=0
    has the following meaning: The connection point of an element which
    has one terminal is pointing to the top side of the diagram. The connection
    point "From side" of an element which has more than one terminal is
    pointing to the top side of the diagram.
    DiagramObject.rotation=90 has the following meaning: The connection
    point of an element which has one terminal is pointing to the right
    hand side of the diagram. The connection point "From side" of an element
    which has more than one terminal is pointing to the right hand side
    of the diagram.
    '''
    
    Diagram: Optional[Diagram] = field(
        default=None,
        metadata={
        'type': 'ByReference',
        'minOccurs': '1',
        'maxOccurs': '1',
        'inverse': 'Diagram.DiagramElements',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram object is part of a diagram.
    '''
    
    DiagramObjectStyle: Optional[DiagramObjectStyle] = field(
        default=None,
        metadata={
        'type': 'ByReference',
        'minOccurs': '1',
        'maxOccurs': '1',
        'inverse': 'DiagramObjectStyle.StyledObjects',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A diagram object has a style associated that provides a reference for
    the style used in the originating system.
    '''
    
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class TextDiagramObject(DiagramObject):
    '''
    A diagram object for placing free-text or text derived from an associated
    domain object.
    '''

    text: Optional[str] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '1',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The text that is displayed by this text diagram object.
    '''
    
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class DiagramObjectStyle(IdentifiedObject):
    '''
    A reference to a style used by the originating system for a diagram object.
    A diagram object style describes information such as line thickness, shape
    such as circle or rectangle etc, and colour.
    '''

    StyledObjects: list[DiagramObject] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'DiagramObject.DiagramObjectStyle',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A style can be assigned to multiple diagram objects.
    '''
    
@stereotype(CIMStereotype.Concrete)
@stereotype(CIMStereotype.ByReference)
@dataclass(repr=False)
class DiagramStyle(IdentifiedObject):
    '''
    The diagram style refers to a style used by the originating system for
    a diagram. A diagram style describes information such as schematic, geographic,
    etc.
    '''

    Diagram: list[Diagram] = field(
        default_factory=list,
        metadata={
        'type': 'Association',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'Diagram.DiagramStyle',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A DiagramStyle can be used by many Diagrams.
    '''
    
@stereotype(CIMStereotype.Concrete)
@dataclass(repr=False)
class VisibilityLayer(IdentifiedObject):
    '''
    Layers are typically used for grouping diagram objects according to themes
    and scales. Themes are used to display or hide certain information (e.g.,
    lakes, borders), while scales are used for hiding or displaying information
    depending on the current zoom level (hide text when it is too small to
    be read, or when it exceeds the screen size). This is also called de-cluttering.
    CIM based graphics exchange supports an m:n relationship between diagram
    objects and layers. The importing system shall convert an m:n case into
    an appropriate 1:n representation if the importing system does not support
    m:n.
    '''

    drawingOrder: Optional[int] = field(
        default=None,
        metadata={
        'type': 'Attribute',
        'minOccurs': '0',
        'maxOccurs': '1',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    The drawing order for this layer. The higher the number, the later
    the layer and the objects within it are rendered.
    '''
    
    VisibleObjects: list[DiagramObject] = field(
        default_factory=list,
        metadata={
        'type': 'ByReference',
        'minOccurs': '0',
        'maxOccurs': 'unbounded',
        'inverse': 'DiagramObject.VisibilityLayers',
        'namespace': 'http://iec.ch/TC57/CIM101#',
        })
    '''
    A visibility layer can contain one or more diagram objects.
    '''
    
@stereotype(CIMStereotype.enumeration)
@stereotype(CIMStereotype.Attribute)
class OrientationKind(Enum):
    '''
    The orientation of the coordinate system with respect to top, left, and
    the coordinate number system.
    '''

    negative = 'negative'
    '''
    For 2D diagrams, a negative orientation gives the left-hand orientation
    (favoured by computer graphics displays) with X values increasing from
    left to right and Y values increasing from top to bottom. This is also
    known as a left hand orientation.
    '''
    
    positive = 'positive'
    '''
    For 2D diagrams, a positive orientation will result in X values increasing
    from left to right and Y values increasing from bottom to top. This
    is also known as a right hand orientation.
    '''
    
@stereotype(CIMStereotype.CIMDatatype)
@dataclass(repr=False)
class AngleDegrees(CIMUnit):
    '''
    Measurement of angle in degrees.
    '''

    value: float = field(default=None)
    multiplier: UnitMultiplier = field(default=UnitMultiplier.none)
    @property # read-only
    def unit(self):
        return UnitSymbol.deg
    def __init__(self, value, input_unit: str='deg', input_multiplier: str=None):
        self.__pint__(value=value, input_unit=input_unit, input_multiplier=input_multiplier)

