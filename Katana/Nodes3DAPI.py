
def ActivatePort():
    """
    Activates the given port for the given graph state, registering the given
    potential Op change callback in the registry of callbacks to be called
    when the port's potential Ops change.
    
    @type port: C{NodegraphAPI.Port}
    @type graphState: C{NodegraphAPI.GraphState} or C{None}
    @type potentialOpChangeCallback: C{callable} or C{None}
    @type getOpFunction: C{callable} or C{None}
    @param port: The port to activate.
    @param graphState: The graph state for which to activate the given port, or
    C{None} to activate the given port for all graph states.
    @param potentialOpChangeCallback: The callback to register for the given
    port.
    @param getOpFunction: An optional callback which should return the Op for
    the given port.
    """
    pass
    
    

def ApplyImplicitResolverOps():
    """ None """
    pass
    
    

def ApplyOp():
    """ None """
    pass
    
    

def BuildAttrListFromDynamicParameterGroup():
    """  """
    pass
    
    

def CancelAllRenders():
    """ None """
    pass
    
    

def CancelRender():
    """ None """
    pass
    
    

def CreateClient():
    """ None """
    pass
    
    

def DeactivatePort():
    """
    Deactivates the given port for the given graph state, removing the given
    potential Op change callback from the registry of callbacks to be called
    when the port's potential Ops change.
    
    @type port: C{NodegraphAPI.Port}
    @type graphState: C{NodegraphAPI.GraphState} or C{None}
    @type potentialOpChangeCallback: C{callable} or C{None}
    @param port: The port to deactivate.
    @param graphState: The graph state for which to deactivate the given port.
    @param potentialOpChangeCallback: The callback to deregister for the given
    port.
    """
    pass
    
    

def DefaultDAPCookOrder():
    """  """
    pass
    
    

def Get3DPortFromNode():
    """ None """
    pass
    
    

def GetExtraParameterValueSourceNodePorts():
    """
    @type node: C{NodegraphAPI.Node}
    @rtype: C{list} of C{NodegraphAPI.Port}
    @param node: The node for which the output ports on the extra parameter
    value source nodes should be returned.
    @return: A list of the first (index 0) output ports on each of the extra
    parameter value source nodes for the given target node.
    @see: L{GetExtraParameterValueSourceNodes()}
    """
    pass
    
    

def GetExtraParameterValueSourceNodes():
    """
    @type node: C{NodegraphAPI.Node}
    @rtype: C{list} of C{NodegraphAPI.Node}
    @param node: The node whose extra parameter value source nodes should be
    returned.
    @return: The list of extra parameter value source nodes for the given node.
    The source nodes will have been set on the given node using
    C{SetExtraParameterValueSourceNodes()}.
    @see: L{SetExtraParameterValueSourceNodes()}
    """
    pass
    
    

def GetGeometryProducer():
    """ Get the L{GeometryProducer} from a L{Node3D}.  The new producer
    will be located at the root location.
    
    Returns C{None} in the case of an error.
    
    @param node: A L{Node3D} or Render node.
    @type node: L{Node}
    @param graphState: GraphState (or None, or float frame time)
    @type graphState: C{GraphState}
    @rtype: L{GeometryProducer}
    @see: L{GetRenderProducer}
    """
    pass
    
    

def GetOp():
    """ Get the Geolib3 Op for a L{Node3D}.
    
    Returns C{None} in the case of an error.
    
    @param node: A L{Node3D} or Render node.
    @type node: L{Node}
    @param graphState: The graph state or frame number
    @type graphState: C{NodegraphAPI.GraphState} or C{float}
    @rtype: Geolib3 Op
    @see: L{GetRenderOp}
    """
    pass
    
    

def GetOpChain():
    """
    @type node: L{Node}
    @type graphState: C{GraphState}
    @type portIndex: C{int}
    @rtype: C{list} of Geolib3 Op or C{None}
    @param node: L{Node3D}
    @param graphState: Graph state in which to fetch the Op chain for the given
    node.
    @param portIndex: The index of the output port of the node for which to
    fetch the Op chain.
    @return: A list of Ops in the Op chain for this node.
    @see: L{GetOp}
    """
    pass
    
    

def GetRegisteredImplicitResolvers():
    """ None """
    pass
    
    

def GetRenderCommandLine():
    """ None """
    pass
    
    

def GetRenderOp():
    """ None """
    pass
    
    

def GetRenderProducer():
    """ Get the renderable L{GeometryProducer} from a L{Node3D}.  The new producer
    will be located at the root location.
    
    The renderable producer has additional operations applied that
    resolve necessary attributes on the producer. This includes
    things like texture, material, and constraint resolution.
    
    Returns C{None} in the case of an error.
    
    @param node: A L{Node3D} or Render node.
    @type node: L{Node}
    @param graphState: GraphState (or None, or float frame time)
    @type graphState: C{GraphState}
    @rtype: L{GeometryProducer}
    @see: L{GetGeometryProducer}
    """
    pass
    
    

def GetRenderTerminalOps():
    """ None """
    pass
    
    

def GetRenderThreads():
    """ None """
    pass
    
    

def GetRuntime():
    """ None """
    pass
    
    

class ImplicitResolverStage(ImplicitResolverStage):
    """ None """

class IncomingSceneOpDelegate(object):
    """ None """
    
    def buildIncomingSceneOp(self):
        """ None """
        pass
        
        

def IsProcessing():
    """ None """
    pass
    
    

def ManualUpdate():
    """ None """
    pass
    
    

class Node3D(NodeGeolib3):
    """ Base class for all 3D Python nodes """
    
    def validateConnection(self):
        """
        Given a producer port from another node and a consumer port on this node
        checks if an eventual connection between these two ports would be valid.
        The default behaviour is that all connections are considered valid, but
        this can be overridden in sub-classes.
        An error message should be appended to the end of the errorMessages
        list.
        
        @type errorMessages: C{list} or C{None}
        @param errorMessages: [out] A list to which any error messages will be
        appended, or C{None} to use Katana's logging system for logging any
        error messages.
        """
        pass
        
        
    
    def require3DInput(self):
        """ None """
        pass
        
        
    
    def _getInternalProducer(self):
        """ None """
        pass
        
        
    
    def getPortsWithInvalidConnections(self):
        """
        Returns all the input (consumer) ports with invalid connections.
        The check is done using validateConnection() on every input port
        with an existing connection.
        """
        pass
        
        
    
    def getAll3DInputs(self):
        """ None """
        pass
        
        
    
    def _getInvalidConnectionsErrorMessage(self):
        """
        Helper function that given a list of input ports with invalid
        connections returns an appropriate error message
        """
        pass
        
        
    
    def _getGeometryProducer(self):
        """ None """
        pass
        
        

class NodeTypeBuilder(object):
    """
    Class used for defining Node3D node types via an abstracted interface.
    """
    
    def setBuildOpChainFnc(self):
        """
        Registers the function to be used for building the node's Op chain.
        
        @type fnc: C{callable} which takes two parameters of type
        C{Node3D.Node3D} and
        C{Nodes3DAPI.NodeTypeBuilder.OpChainInterface}
        """
        pass
        
        
    
    def setAppendToParametersOpChainFnc(self):
        """
        Allows users of NodeTypeBuilder to modify the standard Op chain with
        additional Ops (and their arguments) to influence the appearance
        of values in parameters of an edited node.
        
        @type fnc: C{callable} which takes a parameter of type
        C{Nodes3DAPI.NodeTypeBuilder.ParametersOpChainInterface}
        """
        pass
        
        
    
    def addTransformParameters(self):
        """
        Adds the transform group attribute to the given group builder. Useful
        to expose a transform parameter in the node's parameter interface.
        
        @type gb: C{FnAttribute.GroupBuilder}
        @param gb: The group builder to which add the transform group
        attribute.
        """
        pass
        
        
    
    def addMakeInteractiveParameter(self):
        """
        Adds the 'makeInteractive' attribute to the given group builder.
        Useful to expose the 'makeInteractive' parameter in the node's
        parameter interface.
        
        @type gb: C{FnAttribute.GroupBuilder}
        @param gb: The group builder to which the 'makeInteractive'
        attribute should be added.
        """
        pass
        
        
    
    def addTimingParameters(self):
        """
        Adds the timing group attribute to the given group builder. Useful to
        expose a timing parameter in the node's parameter interface.
        
        @type gb: C{FnAttribute.GroupBuilder}
        @param gb: The group builder to which add the timing group attribute.
        """
        pass
        
        
    
    def setInputPortNames(self):
        """
        Defines the names and order of input ports to be created on node
        initialization. By default, newly created types have no input ports.
        
        @type names: C{sequence} of C{str}
        @param names: A list of names
        """
        pass
        
        
    
    def setGenericAssignRoots(self):
        """
        Sets the parameter and attribute name to be used as roots by the
        GenericAssign mechanism.
        
        @type paramRoot: C{str}
        @type attrRoot: C{str}
        @param paramRoot: The name of a group parameter in the hierarchy of
        parameters on a node under which child parameters should show
        values from the incoming scene, in the form of //Enableable
        Parameter Groups//.
        @param attrRoot: The name of a group attribute that is the target for
        attributes that correspond to //Enableable Parameter Groups// under
        the group parameter specified by C{paramRoot}.
        """
        pass
        
        
    
    def setAddParameterHintsFnc(self):
        """
        Defines an optional callback function which allows a node to
        add additional parameter hints when a new parameter is added.
        
        The function should have a signature matching:
        addCustomParameterHints(self, attrName, inputDict)
        
        It does not return anything.
        
        @type fnc: C{callable}
        """
        pass
        
        
    
    def classmethod(self, function):
        """ classmethod(function) -> method
        
        Convert a function to be a class method.
        
        A class method receives the class as implicit first argument,
        just like an instance method receives the instance.
        To declare a class method, use this idiom:
        
        class C:
        def f(cls, arg1, arg2, ...): ...
        f = classmethod(f)
        
        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()).  The instance is ignored except for its class.
        If a class method is called for a derived class, the derived class
        object is passed as the implied first argument.
        
        Class methods are different than C++ or Java static methods.
        If you want those, see the staticmethod builtin. """
        pass
        
        
    
    def setOutputPortNames(self):
        """
        Defines the names and order of output ports to be created on node
        initialization. By default, newly created types have a single output
        port named 'out'.
        
        @type names: C{sequence} of C{str}
        @param names: A list of names
        """
        pass
        
        
    
    def setHintsForNode(self):
        """
        Sets the hint dictionary used for the node type itself. This is most
        useful for setting "help" text.
        
        @type hints: C{dict}
        """
        pass
        
        
    
    def setCustomMethod(self):
        """
        Allows specification of custom methods on the resulting node type.
        If the name is not valid or clashes with an existing member function
        on the base class, an exception will be thrown during build.
        
        @type fncName: C{str}
        @type fnc: C{callable}
        """
        pass
        
        
    
    def setHintsForParameter(self):
        """
        Sets the hint dictionary for a given parameter path relative to the
        node's top-level parameter group.
        
        @type paramPath: C{str}
        @type hints: C{dict}
        """
        pass
        
        
    
    def setParametersTemplateAttr(self):
        """
        Defines the parameter layout of the node using a C{GroupAttribute} as
        a template. Single-element C{FloatAttribute}, C{IntAttribute} and
        C{DoubleAttribute} children are converted to number parameters.
        Single-element C{StringAttribute} children are converted to string
        parameters. Multi-element attrs are created as array parameters of
        equivalent type. If forceArrayNames is specified, single-element attrs
        at the matching relative attribute paths will be created as
        equivalent array parameters. Child GroupAttributes are created as
        group parameters.
        
        @type groupAttr: C{FnAttribute.GroupAttribute}
        @type forceArrayNames: C{sequence} of C{str}
        """
        pass
        
        
    
    def addInteractiveTransformCallbacks(self):
        """
        Sets up the callbacks to interactively modify the 'transform' parameter
        exposed by the node. If the node doesn't have a 'transform' parameter,
        it will be created.
        
        @type gb: C{FnAttribute.GroupBuilder}
        @param gb: The group builder to which add the transform group attribute
        if not already available.
        """
        pass
        
        
    
    def setNodeTypeVersion(self):
        """
        Setting this allows you to tag node instances with a version so that
        you can provide upgrade paths at katana document parse time. The
        value defaults to 1 if not set. As only one plug-in can register a
        node type of a given name, the version of the registered type is
        considered current for document update purposes. This value is
        recorded in the node's XML representation as a "nodetypeversion"
        attribute.
        """
        pass
        
        
    
    def setGetScenegraphLocationFnc(self):
        """
        Defines an optional callback function which allows a node to
        partipate in widgets and parameter expressions
        
        The function should have a signature matching:
        getScenegraphLocation(node, frameTime)
        
        It should return a single C{str} value in the form of a scenegraph
        location path. It is allowed to inspect but not mutate its parameters
        to do so.
        
        @type fnc: C{callable}
        """
        pass
        
        
    
    def setIsHiddenFromMenus(self):
        """
        Allows you to specify whether the created node type should be
        hidden from UI menus.
        
        @type state: C{bool}
        """
        pass
        
        
    
    def setNodeTypeVersionUpdateFnc(self):
        """
        Calling this allows you to register a version upgrade function to the
        specified version from earlier versions. These functions are called
        during katana document parse and have this signature:
        
        upgradeFnc(nodeElement)
        
        The node element is an instance of PyXmlIO.Element and can be
        queried and manipulated with the NodegraphAPI.Xio module.
        
        When parsing the document (prior to instantiating nodes), these scripts
        are run in sequence for the relevant version range. That range is
        defined by versions greater than document's recorded version (via
        the "nodetypeversion" element attribute) and less than or equal to the
        current registered version.
        """
        pass
        
        
    
    def build(self):
        """
        Commits the definitions and registers as a node type. This should be
        called only once.
        """
        pass
        
        
    
    def setBuildParametersFnc(self):
        """
        Defines an optional callback function which has an opportunity to
        procedurally create parameters on the newly created node instance.
        This is called following the conversion of values provided by
        C{setParametersTemplateAttr}.
        
        The function should have a signature matching:
        buildParameters(node)
        
        Its return value (if any) is discarded.
        
        @type fnc: C{callable}
        """
        pass
        
        

class OutgoingAttributesDelegate(object):
    """ None """
    
    def buildOutgoingAttributes(self):
        """ None """
        pass
        
        

def RegisterImplicitResolver():
    """ None """
    pass
    
    

def RegisterIncomingSceneOpDelegate():
    """ None """
    pass
    
    

def RegisterOutgoingAttributesDelegate():
    """ None """
    pass
    
    

class RenderNode(object):
    """
    This constructor is called from buildCommandLineInfoPythonWrapper() in
    NODES2D/src/glue/PyNode2D.cpp. This in turn is called from functions in
    NODES2D/src/IO/CommandLine.cpp to construct CommandLineInfoPtr objects.
    
    To add arguments to this constructor, you also need to modify
    buildCommandLIneInfoPythonWrapper.
    """
    
    def getCleanupFiles(self):
        """ None """
        pass
        
        
    
    def loadOutputsInMonitor(self):
        """ None """
        pass
        
        
    
    def __processMergeOutputs(self):
        """ None """
        pass
        
        
    
    def __addRenderOutputEnabledStatesToRecipe(self):
        """ None """
        pass
        
        
    
    def getDataWindow(self):
        """ None """
        pass
        
        
    
    def getPackageString(self):
        """ None """
        pass
        
        
    
    def __buildCommandLines(self):
        """ None """
        pass
        
        
    
    def getPostCommands(self):
        """ None """
        pass
        
        
    
    def getImageFiles(self):
        """ None """
        pass
        
        
    
    def __addRenderTargetLocationsToRecipe(self):
        """ None """
        pass
        
        
    
    def getRenderFinishedFilename(self):
        """ None """
        pass
        
        
    
    def __processOutputs(self):
        """ None """
        pass
        
        
    
    def __processPreScriptOutput(self):
        """ None """
        pass
        
        
    
    def __getAttrValueOrEmptyString(self):
        """ None """
        pass
        
        
    
    def getConvertFiles(self):
        """ None """
        pass
        
        
    
    def __processScriptOutput(self):
        """ None """
        pass
        
        
    
    def getCommandLines(self):
        """ None """
        pass
        
        
    
    def __addTempFileInformationToRecipe(self):
        """ None """
        pass
        
        
    
    def getPreCommands(self):
        """ None """
        pass
        
        
    
    def finalizeSetup(self):
        """ None """
        pass
        
        
    
    def getCopyFiles(self):
        """ None """
        pass
        
        
    
    def getCacheID(self):
        """ None """
        pass
        
        
    
    def getDisplayWindow(self):
        """ None """
        pass
        
        
    
    def getRendererString(self):
        """ None """
        pass
        
        

def RenderNode3D():
    """ None """
    pass
    
    

def SetExtraParameterValueSourceNodes():
    """
    Sets the extra parameter value source nodes for the given node to refer to
    the given source nodes. This allows the given node to use the scene graph
    produced by the given source nodes as the value source of its own
    GenericAssign parameters. The scene graph of the given source nodes is
    internally merged with the given node's scene graph. The given source nodes
    needn't to be connected to the target node.
    
    The names of the extra parameter value source nodes are stored on a
    parameter on the node, so will be saved with the Katana document.
    
    @type node: C{NodegraphAPI.Node}
    @type sourceNodes: C{list} of C{NodegraphAPI.Node}
    @param node: The target node.
    @param sourceNodes: The list of source nodes.
    @see: L{GetExtraParameterValueSourceNodes()}
    """
    pass
    
    

def SetRenderThreads():
    """ None """
    pass
    
    

def SignalRender():
    """ None """
    pass
    
    
