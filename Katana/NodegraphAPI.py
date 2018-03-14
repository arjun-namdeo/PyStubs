
def AddNodeFlavor():
    """ Tag a node type with a flavor.
    The flavor name is created if it has never been used.
    It is safe to tag the node multiple times with the same
    flavor, the tag is only recorded once. It is also safe
    to call this if the node type has never been registered.
    
    @param nodeType: C{str} of the node name
    @param flavor: C{str} of the flavor name
    """
    pass
    
    

def AreEventsEnabled():
    """ Returns whether nodegraph events are enabled.
    
    @attention: They always should be enabled!
    """
    pass
    
    

class AssetPublishing(object):
    """
    Class representing an asset publishing operation, storing details about an
    asset to publish, and allowing control over behavior of publishing assets
    with a set of flags.
    
    @cvar kAssetPublishingStarted: State indicating that the asset publishing
    operation has been started, but has not succeeded, failed, or been
    cancelled yet.
    @cvar kAssetPublishingSucceeded: State indicating that the asset publishing
    operation has succeeded. The name of the published file or asset can be
    obtained using L{getPublishedFilenameOrAssetID()}.
    @cvar kAssetPublishingCancelled: State indicating that the asset publishing
    operation has been cancelled.
    @cvar kAssetPublishingFailed: State indicating that the asset publishing
    operation has failed. Details about a possible error can be obtained
    using L{getErrorMessage()}.
    """
    
    def getFilenameOrAssetIdToPublish(self):
        """
        @rtype: C{str} or C{None}
        @return: The name of the file or the ID of the asset to publish, or
        C{None} if no filename or asset ID has been set.
        """
        pass
        
        
    
    def isErrorLoggingEnabled(self):
        """
        @rtype: C{bool}
        @return: C{True} if error messages are to be logged when publishing an
        asset fails, or C{False} to omit such messages.
        """
        pass
        
        
    
    def errorMessageDialogsEnabled(self):
        """
        @rtype: C{bool}
        @return: C{True} if error message dialogs are to be shown in case
        publishing an asset fails, or C{False} to omit those dialogs.
        """
        pass
        
        
    
    def setAssetType(self):
        """
        @type assetType: C{str} or C{None}
        @param assetType: The name of the type of asset to publish, or C{None}
        to reset the asset type.
        """
        pass
        
        
    
    def setNodeName(self):
        """
        @type nodeName: C{str} or C{None}
        @param nodeName: The name of the node from which to publish an asset,
        or C{None} to reset the node name.
        """
        pass
        
        
    
    def setSuccessLoggingEnabled(self):
        """
        Sets the flag that controls whether informational messages are logged
        when successfully publishing an asset.
        
        @type successLoggingEnabled: C{bool}
        @param successLoggingEnabled: C{True} if informational messages are to
        be logged when successfully publishing an asset, or C{False} to
        omit such messages.
        """
        pass
        
        
    
    def isOverwriteAssetEnabled(self):
        """
        @rtype: C{bool}
        @return: C{True} if an existing asset is to be overwritten without
        showing an asset browser dialog for the user to select an asset ID
        or filename, and without showing a confirmation dialog prior to
        overwriting the file, or C{False} to show both.
        """
        pass
        
        
    
    def setPublishedFilenameOrAssetID(self):
        """
        @type publishedFilenameOrAssetID: C{str} or C{None}
        @param publishedFilenameOrAssetID: The name of the published file or
        the ID of the published asset, or C{None} to reset the filename or
        asset ID of the published file or asset.
        """
        pass
        
        
    
    def getNodeName(self):
        """
        @rtype: C{str} or C{None}
        @return: The name of the node from which to publish an asset, or
        C{None} if no node name has been set.
        """
        pass
        
        
    
    def getState(self):
        """
        @rtype: C{int}
        @return: The state of the asset publishing operation represented by an
        instance of the AssetPublishing class.
        """
        pass
        
        
    
    def getErrorMessage(self):
        """
        @rtype: C{str} or C{None}
        @return: An error message describing why asset publishing has failed,
        or C{None} if no error message has been set.
        """
        pass
        
        
    
    def setOverwriteAssetEnabled(self):
        """
        Sets the flag that controls whether an existing asset is to be
        overwritten without showing dialogs for the user to select an asset ID
        or filename and to confirm the action.
        
        @type overwriteAssetEnabled: C{bool}
        @param overwriteAssetEnabled: C{True} if no asset browser dialog and no
        overwrite confirmation dialog is to be shown when publishing an
        asset, or C{False} to show both.
        """
        pass
        
        
    
    def setState(self):
        """
        @type state: C{int}
        @param state: The state of the asset publishing operation represented
        by an instance of the AssetPublishing class to set for the
        instance.
        """
        pass
        
        
    
    def isSuccessLoggingEnabled(self):
        """
        @rtype: C{bool}
        @return: C{True} if informational messages are to be logged when
        successfully publishing an asset, or C{False} to omit such
        messages.
        """
        pass
        
        
    
    def setErrorMessageDialogsEnabled(self):
        """
        Sets the flag that controls whether error message dialogs are to be
        shown in case publishing an asset fails.
        
        @type errorMessageDialogsEnabled: C{bool}
        @param errorMessageDialogsEnabled: C{True} if error dialogs are to be
        shown in case publishing an asset fails, or C{False} to omit those
        dialogs.
        """
        pass
        
        
    
    def getAssetType(self):
        """
        @rtype: C{str} or C{None}
        @return: The name of the type of asset to publish, or C{None} if no
        asset type has been set.
        """
        pass
        
        
    
    def setErrorMessage(self):
        """
        @type errorMessage: C{str} or C{None}
        @param errorMessage: An error message describing why asset publishing
        has failed, or C{None} to reset the error message.
        """
        pass
        
        
    
    def setFilenameOrAssetIdToPublish(self):
        """
        @type filenameOrAssetIdToPublish: C{str} or C{None}
        @param filenameOrAssetIdToPublish: The name of the file or the ID of
        the asset to publish, or C{None} to reset the filename or asset ID.
        """
        pass
        
        
    
    def setErrorLoggingEnabled(self):
        """
        Sets the flag that controls whether error messages are logged when
        publishing an asset fails.
        
        @type errorLoggingEnabled: C{bool}
        @param errorLoggingEnabled: C{True} if error messages are to be logged
        when publishing an asset fails, or C{False} to omit such messages.
        """
        pass
        
        
    
    def getPublishedFilenameOrAssetID(self):
        """
        @rtype: C{str} or C{None}
        @return: The name of the published file or the ID of the published
        asset, or C{None} if no filename or asset ID of a published file or
        asset has been set.
        """
        pass
        
        

def AsynchronousContext():
    """
    Context manager that undoes the effects of the L{SynchronousContext}
    context manager.
    When using the C{AsynchronousContext} context manager, users should
    explicitly process events when needed or otherwise be aware that
    correctness of the result is not guaranteed.
    """
    pass
    
    

def BuildNodegraphXmlIO():
    """ Build XmlIO element tree from node graph. This returns the top
    element encapsulated in a root katana element.
    """
    pass
    
    

def BuildNodesXmlIO():
    """ Build XmlIO element tree from a group of nodes. The nodes must
    all have the same parent node.
    """
    pass
    
    

def CalculateLiveGroupDepth():
    """
    @type liveGroupNode: C{NodegraphAPI.LiveGroupMixin} or C{NodegraphAPI.Node}
    @rtype: C{int}
    @param liveGroupNode: The node for which to calculate the depth in the
    LiveGroup nodes hierarchy.
    @return: The depth of the given LiveGroup node in the node graph taking
    into account LiveGroup nodes only. -1 if the given not is not a valid
    LiveGroup node.
    """
    pass
    
    

def CanBeDifferentFromSource():
    """
    @type liveGroupNode: L{LiveGroupMixin}
    @rtype: C{bool}
    @param liveGroupNode: The LiveGroup node to check.
    @return: C{True} if the given LiveGroup node has no source set for it, or
    if it can be different from a source that its parameters and contents
    are loaded from, otherwise C{False}.
    @raise TypeError: If the given object is not a LiveGroup node.
    """
    pass
    
    

def CheckNodeType():
    """ None """
    pass
    
    

def ClearFlavorNodes():
    """ Untag all nodes from the flavor.
    All nodes types previously tagged with the flavor or untagged.
    This is safe to call if the flavor has never been defined.
    
    @param flavor: C{str} of the flavor name
    """
    pass
    
    

def ConvertGroupToLiveGroup():
    """
    Converts a Group node to a LiveGroup node
    """
    pass
    
    

def CreateGroupParameter():
    """ None """
    pass
    
    

def CreateNode():
    """ Create a new node of the given type.
    If the parent argument is given, the node will be created
    inside that group.
    
    @return: The newly created node.
    @rtype: L{Node}
    @param type: Name of the node type.
    @type type: C{str}
    @param parent: Optional parent group.
    @type parent: L{GroupNode}
    @raise ValueError: Node type not registered.
    """
    pass
    
    

def CreateNumberParameter():
    """ None """
    pass
    
    

def CreateStringParameter():
    """ None """
    pass
    
    

def DeleteNodeShapeAttr():
    """ None """
    pass
    
    

def DeleteParameter():
    """ None """
    pass
    
    

def FCurveLookup():
    """ Lookup a curve held in an external filename or asset. The
    loaded curve will be cached. If frame is None, the current
    node graph time is used. The curveName argument is for the name
    of the curve to use.
    """
    pass
    
    

def GetAllActiveAttributeEditorNodes():
    """ None """
    pass
    
    

def GetAllEditedNodes():
    """ Get all nodes that are being edited.
    When nodes are edited their parameters are displayed in the
    user interface. There can be none or several nodes edited at
    once time.
    
    @rtype: C{list} of L{Node}
    """
    pass
    
    

def parameter_getAllExpressionedParameters(errorsOnly=False, noErrorsOnly=False):
    """ getAllExpressionedParameters(errorsOnly=False, noErrorsOnly=False) -> set(parameters)
    Get a set of all parameters with expressions.
    Note that expression's errors depend on their having been evaluated.
    @param errorsOnly: include only parameters with expressions with errors
    @param noErrorsOnly: include only parameters with expressions without errors
    (mutually exclusive with errorsOnly) """
    pass
    
    

def GetAllFlavors():
    """ Untag all nodes from the flavor.
    Get a list of all defined flavors
    
    @return: C{list}
    """
    pass
    
    

def GetAllFloatingNodes():
    """ Get a list of all nodes that are floating.
    When nodes are interactively created or moved, they become
    floating nodes. Floating nodes track with the mouse movement
    until they are placed.
    
    @rtype: C{list} of L{Node}
    """
    pass
    
    

def GetAllNodes():
    """ Get all the created nodes.
    Return all the nodes that have been created. An empty
    list means there are no nodes, but this is rare because
    of the root node.
    
    @return: All nodes
    @rtype: C{list} of L{Node}
    """
    pass
    
    

def GetAllNodesByType():
    """ Get all the nodes with the specified type.
    Return all the nodes that have been created. An empty
    list means there are no nodes, but this is rare because
    of the root node.
    
    @return: All nodes
    @rtype: C{list} of L{Node}
    """
    pass
    
    

def GetAllSelectedNodes():
    """ Get all the nodes that are currently selected.
    Interface operations that effect nodes will be applied
    to selected nodes. There can be any number of selected
    nodes at a time.
    
    @rtype: C{list} of L{Node}
    """
    pass
    
    

def GetAllSelectedNodesAndParent():
    """ Get the selected nodes inside a parent.
    Some interface options can only work on nodes inside a single
    parent. This convenience function helps to get the selected
    nodes, but fail if the selection crosses groups.
    
    @rtype: (C{list} of L{Node}, L{GroupNode})
    @raise ValueError: All selected nodes are not in the same group
    """
    pass
    
    

def GetAllThumbnailEnabledNodes():
    """ None """
    pass
    
    

def GetAutoKeyAll():
    """ True of auto keyframing is turned on.
    When autokeying is turned on, parameter value changes on
    parameters that are curves will be automatically keyed.
    Otherwise changes are applied to a temporary floating
    keyframe.
    
    @rtype: C{bool}
    """
    pass
    
    

def GetCurrentGraphState():
    """ Get the current graph state. Like GetCurrentTime(), but with all graph
    state information (such as variables)
    
    @return: GraphState
    """
    pass
    
    

def GetCurrentTime():
    """
    @rtype: C{number}
    @return: The current time on the timeline.
    @see: L{GetInTime()}, L{GetOutTime()}
    """
    pass
    
    

def GetExpressionGlobalValue():
    """ When L{Parameter} values are set to expression mode, they
    are evaluated inside a custom namespace. This function
    looks up a value in the namespace.
    
    @param name: Name of the new object.
    @type name: C{str}
    @raise KeyError: Name not found.
    """
    pass
    
    

def parameter_getExpressionReferences(limitingNodes=None, excludeSelfRefs=True):
    """ getExpressionReferences(limitingNodes=None, excludeSelfRefs=True) -> {node: set(nodes)}
    Get a map of all expressions references.
    Looks for getNode or getParam.
    @see getReferences(time)
    @param limitingNodes if not None, look only for expressions referencing nodes in the given set
    @param excludeSelfRefs whether to exclude references from a node to itself
    @return a map of nodes referenced each to set of nodes referencing """
    pass
    
    

def GetFlavorNodes():
    """ Get all node types tagged with a flavor.
    If the filterExists flag is passed as True, then only
    nodes types that have been registered will be returned.
    Otherwise node types may be returned that have been
    tagged but not defined.
    
    @param flavor: C{str}
    @param filterExists: C{bool}
    @return: C{list}
    """
    pass
    
    

def GetGraphState():
    """ Get the graph state for the specified time
    
    @type timeval: C{float}
    @rtype: C{GraphState}
    @param timeval: Specified time
    @return: the graphState
    """
    pass
    
    

def GetInTime():
    """ Get the in frame.
    The in time must be lesser than the out time.
    
    @rtype: C{number}
    """
    pass
    
    

def GetKatanaSceneName():
    """ Get the current asset name being used.
    Used by exporters to generate asset names.
    @return: asset name
    @rtype: C{str} or C{None}
    """
    pass
    
    

def GetMenuPath():
    """ None """
    pass
    
    

def GetNode():
    """ Find existing node by name.
    Search all created nodes for the node with the given name.
    The node name is not necessarily the node type. If the node
    is not found, C{None} is returned.
    
    @return: The newly created node.
    @rtype: L{Node} or C{None}
    @param nodeName: Name of the node type.
    @type nodeName: C{str}
    """
    pass
    
    

def GetNodeComment():
    """ Get the user comment on the node
    
    @type node: L{Node}
    @rtype: C{string}
    """
    pass
    
    

def GetNodeFlavors():
    """ Get all tagged flavors for a node type.
    @param nodeType: C{str}
    @return: C{list}
    """
    pass
    
    

def GetNodeModTime():
    """ Get the modification time of the file loaded into a LiveGroup node.
    This attribute will only be set on LiveGroup nodes.  All other nodes
    return 0.
    
    @type node: L{Node}
    @rtype: C{int}
    """
    pass
    
    

def GetNodeParameter():
    """ Gets an arbitrary parameter for a node
    """
    pass
    
    

def GetNodePosition():
    """ Get the 2D position of the node.
    Created nodes have the position (0, 0).
    The position is in y-down integers.
    
    @type node: L{Node}
    @rtype: (C{int}, C{int})
    """
    pass
    
    

def GetNodeShapeAttr():
    """ None """
    pass
    
    

def GetNodeShapeAttrs():
    """ None """
    pass
    
    

def GetNodeTypes():
    """ Get all the registered node types.
    Builds a list of all L{Node} types that have been registered.
    
    @return: All names
    @rtype: C{list} of C{str}
    """
    pass
    
    

def GetNodegraphVersionString():
    """ Get the nodegraph version string.
    When loading from a file, the nodegraph gets a version.
    
    @rtype: C{str}
    """
    pass
    
    

def GetOriginalProjectAssetID():
    """
    @rtype: C{str}
    @return: The name of the original file or the ID of the original asset that
    the current project was last saved as before loading.
    @note: Example: A file is saved to an asset and subsequently copied to
    "/tmp/a.katana". When the file is loaded from "/tmp/a.katana",
    L{GetProjectAssetID()} returns C{'/tmp/a.katana'}, and
    L{GetOriginalProjectAssetID()} returns the ID of the original asset.
    """
    pass
    
    

def GetOriginalSourceFile():
    """
    @rtype: C{str}
    @return: The name of the original file or the ID of the original asset that
    the current project was last saved as before loading.
    @note: Example: A file is saved to an asset and subsequently copied to
    "/tmp/a.katana". When the file is loaded from "/tmp/a.katana",
    L{GetSourceFile()} returns C{'/tmp/a.katana/'}, and
    L{GetOriginalSourceFile()} returns the ID of the original asset.
    """
    pass
    
    

def GetOutTime():
    """ Get the end frame.
    The out time must be greater than the in time.
    
    @rtype: C{number}
    """
    pass
    
    

def GetProjectAssetID():
    """
    @rtype: C{str}
    @return: The name of the file or the ID of the asset that the current
    project was loaded from.
    """
    pass
    
    

def GetProjectDir():
    """
    @rtype: C{str}
    @return: The resolved file system location path of the directory that
    contains the .katana file from which the node graph document of the
    current project was loaded.
    """
    pass
    
    

def GetProjectFile():
    """
    @rtype: C{str}
    @return: The resolved file system location path of the .katana file
    from which the node graph document of the current project was loaded.
    """
    pass
    
    

def GetRootNode():
    """ Get the current root node.
    Each nodegraph will exist inside a single root node.
    The root node always exists, even inside a new file.
    
    @rtype: C{NodegraphAPI.GroupNode}
    """
    pass
    
    

def GetSourceFile():
    """
    @rtype: C{str}
    @return: The name of the file or the ID of the asset that the current
    project was loaded from.
    """
    pass
    
    

def GetTimeIncrement():
    """ Get the time increment when a single frame is advanced.
    This value is usually 1.
    
    @rtype: C{float}
    """
    pass
    
    

def GetUserNodesXmlRootAttrs():
    """ None """
    pass
    
    

def GetViewNode():
    """ Get the node that is currently viewed.
    When the node is viewed, its output is displayed in the
    interface.
    
    @rtype: L{Node} or C{None}
    """
    pass
    
    

def GetViewNodes():
    """ Get the nodes that are currently viewed.
    When the node is viewed, its output is displayed in the
    interface.
    @rtype: L{Node} or C{None}
    """
    pass
    
    

def GetViewPortPosition():
    """ Get the view information of a group network.
    Each L{GroupNode} also maintains view information for its
    child network. It is stored in this viewport. The return
    contains the eyepoint and the viewscale.
    - The default vewpoint is C{0, 0, 10000}
    - The default viewscale is C{1, 1, 1}
    
    @type node: L{GroupNode}
    @return: the position and scale
    @rtype: (C{int}, C{int}, C{int}), (C{float}, C{float}, C{float})
    """
    pass
    
    

def GetWorkingInTime():
    """ Get the start frame of the working range.
    The in time is guaranteed to be less than or equal to the out time.
    
    @rtype: C{number}
    """
    pass
    
    

def GetWorkingOutTime():
    """ Get the end frame of the working range.
    The out time is guaranteed to be less than or equal to the in time.
    
    @rtype: C{number}
    """
    pass
    
    

class GraphState(object):
    """ GraphState """
    
    def getView(self):
        """  """
        pass
        
        
    
    def getTime(self):
        """  """
        pass
        
        
    
    def getShutterOpen(self):
        """  """
        pass
        
        
    
    def getMaxTimeSamples(self):
        """  """
        pass
        
        
    
    def matchVariableWithCEL(self):
        """  """
        pass
        
        
    
    def getDynamicEntry(self):
        """  """
        pass
        
        
    
    def getStaticHash(self):
        """  """
        pass
        
        
    
    def getDynamicHash(self):
        """  """
        pass
        
        
    
    def getStaticEntry(self):
        """  """
        pass
        
        
    
    def isDiskCachingAllowed(self):
        """  """
        pass
        
        
    
    def getROI(self):
        """  """
        pass
        
        
    
    def getHash(self):
        """  """
        pass
        
        
    
    def isExternalRenderAllowed(self):
        """  """
        pass
        
        
    
    def getRenderMethodName(self):
        """  """
        pass
        
        
    
    def getShutterClose(self):
        """  """
        pass
        
        
    
    def isHotRender(self):
        """  """
        pass
        
        
    
    def getSampleRateX(self):
        """  """
        pass
        
        
    
    def getSampleRateY(self):
        """  """
        pass
        
        
    
    def isTaskCachingIgnored(self):
        """  """
        pass
        
        
    
    def getOpSystemArgs(self):
        """  """
        pass
        
        
    
    def edit(self):
        """  """
        pass
        
        

class GraphStateBuilder(object):
    """ GraphStateBuilder """
    
    def setHotRender(self):
        """  """
        pass
        
        
    
    def setROI(self):
        """  """
        pass
        
        
    
    def setSampleRateX(self):
        """  """
        pass
        
        
    
    def setMaxTimeSamples(self):
        """  """
        pass
        
        
    
    def setIgnoreTaskCaching(self):
        """  """
        pass
        
        
    
    def setView(self):
        """  """
        pass
        
        
    
    def setSampleRateY(self):
        """  """
        pass
        
        
    
    def setShutterOpen(self):
        """  """
        pass
        
        
    
    def setShutterClose(self):
        """  """
        pass
        
        
    
    def setStaticEntry(self):
        """  """
        pass
        
        
    
    def setExternalRenderAllowed(self):
        """  """
        pass
        
        
    
    def deleteStaticEntry(self):
        """  """
        pass
        
        
    
    def setDynamicEntry(self):
        """  """
        pass
        
        
    
    def setDiskCachingAllowed(self):
        """  """
        pass
        
        
    
    def setTime(self):
        """  """
        pass
        
        
    
    def setRenderMethodName(self):
        """  """
        pass
        
        
    
    def deleteDynamicEntry(self):
        """  """
        pass
        
        
    
    def build(self):
        """  """
        pass
        
        

class GroupNode(Node):
    """ Group Node Type.Katana nodes are created and retrieved through the node graph. The node stores parameters and both input and output ports. This GroupNode subclass can contain other children nodes.  """
    
    def setContentLocked(self, bool):
        """ setContentLocked(bool)
        Locks or unlocks the node's content to prevent or allow changes to child nodes. """
        pass
        
        
    
    def getReturnPort(self, name):
        """ getReturnPort(name) -> Port
        Get a return port of a group by name. A return port is the internal connection inside a GroupNode. """
        pass
        
        
    
    def addOutputPortAtIndex(self, name, index):
        """ addOutputPortAtIndex(name, index) -> Port
        Creates a new output port at a specific index, and returns it. """
        pass
        
        
    
    def isContentLocked(self):
        """ isContentLocked() -> bool
        Returns True if the node's contents are locked to prevent changes, otherwise False. """
        pass
        
        
    
    def getNumChildren(self):
        """ getNumChildren() -> int
        The number of nodes inside the group. """
        pass
        
        
    
    def checkChildrenForCycles(self):
        """ checkChildrenForCycles() -> bool
        Returns True if the children nodes of a group form recursion. This is not normally possible. """
        pass
        
        
    
    def setLocked(self, bool):
        """ setLocked(bool)
        Locks or unlocks the group node to prevent or allow changes. """
        pass
        
        
    
    def getChildByIndex(self, index):
        """ getChildByIndex(index) -> Node
        Get one of a groups children nodes by index. """
        pass
        
        
    
    def addOutputPort(self, name, fromLoad=0):
        """ addOutputPort(name, fromLoad=0) -> Port
        Creates a new output port with the given name, and returns it. """
        pass
        
        
    
    def getChildren(self):
        """ getChildren() -> list of Node
        Returns a new list of all nodes inside the group. """
        pass
        
        
    
    def getSendPort(self, name):
        """ getSendPort(name) -> Port
        Get a send port of a group by name. A send port is the internal connection inside a GroupNode. """
        pass
        
        
    
    def getChild(self, name):
        """ getChild(name) -> Node
        Find a child node by name, or returns None. """
        pass
        
        
    
    def addInputPort(self, name, fromLoad=0):
        """ addInputPort(name, fromLoad=0) -> Port
        Creates a new input port with the given name, and returns it. """
        pass
        
        
    
    def addInputPortAtIndex(self, name, index):
        """ addInputPortAtIndex(name, index) -> Port
        Creates a new input port at a specific index, and returns it. """
        pass
        
        

def SynchronousContext():
    """
    Context manager that ensures that changes to parameters are taken into
    account when cooking the scene. All Katana events are processed before and
    after running code that is scoped with this context manager.
    Is used when running Python scripts in script mode and when executing
    Python code in the B{Python} tab.
    """
    pass
    
    

def IsAttributeEditorNodeActive():
    """ None """
    pass
    
    

def IsInSynchronousContext():
    """
    @rtype: C{bool}
    @return: C{True} if called when inside a synchronous context, for example
    when evaluating a Python script in the B{Python} tab, or when running a
    Python script in script mode.
    """
    pass
    
    

def IsLiveGroupCachingEnabled():
    """ None """
    pass
    
    

def IsLiveGroupLoadingEnabled():
    """ None """
    pass
    
    

def IsLoading():
    """ None """
    pass
    
    

def IsNodeEdited():
    """ True if the node parameters are displayed.
    When nodes are edited their parameters are displayed in the
    user interface. There can be none or several nodes edited at
    once time.
    
    @type node: L{Node}
    @rtype: C{bool}
    """
    pass
    
    

def IsNodeFloating():
    """ True if the node is tracking the mouse position.
    When nodes are interactively created or moved, they become
    floating nodes. Floating nodes track with the mouse movement
    until they are placed.
    
    @type node: L{Node}
    @rtype: C{bool}
    """
    pass
    
    

def IsNodeHidden():
    """ None """
    pass
    
    

def IsNodeLockedByParents():
    """
    @type node: C{NodegraphAPI.Node} or C{None}
    @rtype: C{bool}
    @param node: The node whose parent nodes to check.
    @return: C{True} if the contents of any of the given node's parent nodes
    are locked, otherwise C{False}.
    """
    pass
    
    

def IsNodeSelected():
    """ True if the node is selected in the interface.
    Interface operations that effect nodes will be applied
    to selected nodes. There can be any number of selected
    nodes at a time.
    
    @type node: L{Node}
    @rtype: C{bool}
    """
    pass
    
    

def IsNodeThumbnailEnabled():
    """ None """
    pass
    
    

def IsNodeViewed():
    """ True if the node results are displayed.
    When the node is viewed, its output is displayed in the
    interface.
    
    @type node: L{Node}
    @rtype: C{bool}
    """
    pass
    
    

class LiveGroupNode(LiveGroupMixin):
    """
    Class representing a Group node whose contents are defined by a referenced
    external node graph file.
    
    @cvar ATTRIBUTES_TO_IGNORE: A list of names of node attributes that are
    removed from a LiveGroup node's contents when exporting to file.
    """
    
    def _updateContentLock(self):
        """
        Updates the node's content locked flag and the locked states of child
        nodes based on the LiveGroup node's editable state.
        """
        pass
        
        
    
    def load(self):
        """
        Loads the currently referenced external file.
        
        @type lockResult: C{bool}
        @type forceLoad: C{bool}
        @type forceNonEditable: C{bool}
        @param lockResult: Deprecated. Has no effect.
        This flag controlled whether to lock the nodes that have been
        loaded into the LiveGroup node. Contents of loaded LiveGroup nodes
        are now locked by default.
        @param forceLoad: Flag to control whether to force loading of the
        LiveGroup node's source even if the source has not been modified
        since it was last loaded according to the modification timestamp
        stored in an attribute on the LiveGroup node in the node graph
        document.
        @param forceNonEditable: Flag to control whether to force the LiveGroup
        node to be non-editable after loading.
        """
        pass
        
        
    
    def publishAndLoadAsset(self):
        """ @deprecated: This function will be removed. Please use publishAssetAndFinishEditingContents() instead. """
        pass
        
        
    
    def addParameterHints(self):
        """
        Updates the given hints dictionary 'inputDict' for the given attribute
        name, updating the 'LiveGroup.source' parameter's 'widget' hint
        accordingly to the source parameter's asset or file type.
        """
        pass
        
        
    
    def revert(self):
        """
        Reverts the LiveGroup node to the state of the source on disk, or to
        the state of a freshly created LiveGroup node, if no source has been
        set yet.
        
        @rtype: C{bool}
        @return: C{True} if the LiveGroup node was successfully reverted,
        otherwise C{False}.
        """
        pass
        
        
    
    def setLocked(self):
        """
        Overrides the default C{setLocked()} implementation to update the
        locking of contents of the LiveGroup node after setting the locked
        state to the given locked state.
        
        @type locked: C{bool}
        @param locked: Flag to control whether to lock or unlock the LiveGroup
        node to prevent or allow changes.
        """
        pass
        
        
    
    def __resolveLiveGroupReferences(self):
        """
        Parses the content of the given C{documentElement} and replaces
        LiveGroup nodes with their content.
        
        @type documentElement: C{PyXmlIO.Element}
        @rtype: C{tuple} of C{bool} and C{PyXmlIO.Element}
        @param documentElement: A PyXmlIO element that represents the XML
        document in which to replace LiveGroup contents.
        @return: A tuple containing a boolean value indicating if the I{shared}
        element was found, and a PyXmlIO element representing the resulting
        XML document.
        """
        pass
        
        
    
    def publishAssetAndFinishEditingContents(self):
        """
        Convenience function that calls L{exportAsset()} with the given
        arguments, that updates the LiveGroup node's source parameter with the
        result of that function, and finishes editing of the LiveGroup's
        contents, unless an exception is raised.
        
        @type filenameOrAssetID: C{str} or C{None}
        @type extraOptions: C{dict} or C{None}
        @rtype: C{str}
        @param filenameOrAssetID: The name of the file to write, or the ID of
        an asset to write a file for. If empty or C{None}, the LiveGroup
        node's current source is used, if set.
        @param extraOptions: See L{exportAsset()}.
        @return: The result of L{exportAsset()}.
        @raise ValueError: If no filename or asset ID is given, and no source
        is set for the LiveGroup node.
        @raise Exception: If the LiveGroup node's contents could not be
        retrieved.
        @raise RuntimeError: If an asset operation failed.
        """
        pass
        
        
    
    def _calculateContentHash(self):
        """
        @deprecated: Hashing of LiveGroup contents has been removed due to
        performance concerns
        """
        pass
        
        
    
    def reloadFromSource(self):
        """
        Reloads the LiveGroup node from its source on disk.
        
        Logs an error and returns C{False} if no source has been set for the
        LiveGroup node, as LiveGroup nodes without a source set cannot be
        reloaded from a source on disk.
        
        @rtype: C{bool}
        @return: C{True} if the LiveGroup node was successfully reloaded,
        otherwise C{False}.
        @see: L{revertToSource()}
        """
        pass
        
        
    
    def _hasContentChanged(self):
        """
        @deprecated: Hashing of LiveGroup contents has been removed due to
        performance concerns
        """
        pass
        
        
    
    def setAttributes(self):
        """
        Sets the node attributes to use for the LiveGroup node to the given
        attributes.
        
        @type attrs: C{dict}
        @param attrs: A dictionary of node attributes to set for the LiveGroup
        node.
        """
        pass
        
        
    
    def exportAsset(self):
        """
        Exports a LiveGroup node's contents to the uncompressed XML file with
        the given name or to a file that corresponds to the given asset ID as
        determined by the current asset plug-in.
        
        @type filenameOrAssetID: C{str}
        @type extraOptions: C{dict} or C{None}
        @rtype: C{str}
        @param filenameOrAssetID: The name of the file to write, or the ID of
        an asset to write a file for. If a filename is given that does not
        have a C{".livegroup"} or C{".katana"} extension, the
        C{".livegroup"} extension is added to it.
        @param extraOptions: A dictionary of extra arguments to pass to the
        C{createAssetAndPath()} and C{postCreateAsset()} functions of the
        current asset plug-in, if the given C{filenameOrAssetID} is a valid
        asset ID.
        @return: The name of the file that was written, or the asset ID
        returned by the C{postCreateAsset()} call of the current asset
        plug-in, if the given C{filenameOrAssetID} is a valid asset ID.
        @raise ValueError: If no filename or asset ID is given.
        @raise Exception: If the LiveGroup node's contents could not be
        retrieved.
        @raise RuntimeError: If an asset operation failed.
        """
        pass
        
        
    
    def convertToGroup(self):
        """
        Converts the LiveGroup node to a Group node, keeping all child nodes
        and parameters except its B{source} and B{disable} parameters.
        """
        pass
        
        
    
    def publishAsset(self):
        """
        Convenience function that calls L{exportAsset()} with the given
        arguments, and that updates the LiveGroup node's source parameter with
        the result of that function, unless an exception is raised.
        
        Note that this function keeps an editable LiveGroup node in its
        editable state.
        
        @type filenameOrAssetID: C{str} or C{None}
        @type extraOptions: C{dict} or C{None}
        @rtype: C{str}
        @param filenameOrAssetID: The name of the file to write, or the ID of
        an asset to write a file for. If empty or C{None}, the LiveGroup
        node's current source is used, if set.
        @param extraOptions: See L{exportAsset()}.
        @return: The result of L{exportAsset()}.
        @raise ValueError: If no filename or asset ID is given, and no source
        is set for the LiveGroup node.
        @raise Exception: If the LiveGroup node's contents could not be
        retrieved.
        @raise RuntimeError: If an asset operation failed.
        """
        pass
        
        
    
    def hasContentChanged(self):
        """ @deprecated: This function will be removed. Please use isModified() instead. """
        pass
        
        
    
    def writeToAsset(self):
        """ @deprecated: This function will be removed. Please use exportAsset() instead. """
        pass
        
        
    
    def isModified(self):
        """
        @rtype: C{bool}
        @return: C{True} if the LiveGroup node's state indicates that its user
        parameters or contents have been modified, otherwise C{False}.
        """
        pass
        
        
    
    def _sourceAssetIdIsFilePath(self):
        """
        Returns True if current source parameter represents a file path even if
        the default "File" asset plug-in is not the current asset plug-in,
        False otherwise.
        """
        pass
        
        
    
    def getGroupXmlIO(self):
        """
        @rtype: C{Document}
        @return: An XML document that represents the externally referenced file
        (including local internal modifications).
        """
        pass
        
        
    
    def makeEditable(self):
        """
        Makes the LiveGroup node editable, allowing changes to its contents.
        Succeeds only if the LiveGroup node is not currently locked.
        
        @type includingAllParents: C{bool}
        @rtype: C{bool}
        @param includingAllParents: Flag to control whether to recursively make
        all parent LiveGroup nodes editable as well.
        @return: C{True} on success, C{False} if the operation fails or if
        the LiveGrop node is locked.
        """
        pass
        
        
    
    def _updateContentHash(self):
        """
        @deprecated: Hashing of LiveGroup contents has been removed due to
        performance concerns
        """
        pass
        
        

def LoadAllLiveGroups():
    """
    Loads all LiveGroup nodes from their sources starting from the specified
    node.
    
    It is expected that L{LockAllLiveGroups()} is called after loading all
    LiveGroup nodes.
    
    @type node: C{NodegraphAPI.Node}
    @type lockResult: C{bool}
    @type forceLoad: C{bool}
    @param node: The node at which to start loading LiveGroup child nodes.
    @param lockResult: Deprecated. Has no effect.
    This flag controlled whether to lock the nodes that have been loaded
    into the current Katana scene. Contents of loaded LiveGroup nodes are
    now locked by default.
    @param forceLoad: Flag to control whether to force loading of LiveGroup
    nodes from their sources even if the sources have not been modified
    since they were last loaded according to the modification timestamp
    stored in an attribute on LiveGroup nodes in the node graph document.
    If the LiveGroup is disabled, C{forceLoad} will not force it to load.
    """
    pass
    
    

def LoadElementsFromFile():
    """ Get the XmlIO element tree from file on disk.
    Returns the element and a boolean if the data was upgraded.
    """
    pass
    
    

def LoadElementsFromString():
    """ Get the XmlIO element tree from string in memory.
    Returns the element and a boolean if the data was upgraded.
    """
    pass
    
    

def LoadXmlFromFile():
    """ Load a Katana file into a string of XML. Normally the xml
    intermediate format is not required. Use LoadElementsFromFile
    to get the direct xml tree. """
    pass
    
    

def LoadXmlFromString():
    """ Load a Katana string into a string of XML. Normally the xml
    intermediate format is not required. Use LoadElementsFromString
    to get the direct xml tree. """
    pass
    
    

def LockAllLiveGroups():
    """
    Locks the contents of all LiveGroup nodes that are non-editable, starting
    from the specified node.
    
    @type node: C{NodegraphAPI.Node}
    @param node: The node at which to start locking contents of LiveGroup
    nodes.
    """
    pass
    
    

def MakeAllLiveGroupsEditable():
    """
    Makes all LiveGroup nodes starting from the specified node editable.
    
    @type node: C{NodegraphAPI.Node}
    @param node: The node at which to start making the child nodes editable.
    """
    pass
    
    

def MakeAllParentLiveGroupsEditable():
    """
    Makes all parent LiveGroup nodes starting from the specified node editable.
    
    @type node: C{NodegraphAPI.Node}
    @rtype: C{bool}
    @param node: The node at which to start making the parent nodes editable.
    @return: C{True} if all parent LiveGroup nodes have successfully been made
    editable, otherwise C{False}.
    """
    pass
    
    

def NeedsRedraw():
    """ None """
    pass
    
    

def NewNodegraph():
    """ None """
    pass
    
    

class Node(object):
    """ Generic Node Type.Katana nodes are created and retrieved through the node graph. The node stores parameters and both input and output ports. A GroupNode subclass can contain other children nodes.  """
    
    def getNumInputPorts(self):
        """ getNumInputPorts() -> int
        Returns the number of input ports on the node. """
        pass
        
        
    
    def addInputPortAtIndex(self, name, index):
        """ addInputPortAtIndex(name, index) -> Port
        Creates a new input port at a specific index, and returns it. """
        pass
        
        
    
    def getInputPort(self, name):
        """ getInputPort(name) -> Port
        Returns an input port from the node by name. Returns None if not found. """
        pass
        
        
    
    def addOutputPort(self, name):
        """ addOutputPort(name) -> Port
        Creates a new output port with the given name, and returns it. """
        pass
        
        
    
    def getParameter(self, name):
        """ getParameter(name) -> Parameter
        Returns a nested parameter by name. Separate children with '.' dots. Returns None if not found. """
        pass
        
        
    
    def getParameterValue(self, name):
        """ getParameterValue(name) -> float or str or None
        Returns the string or integer value of a named parameter. Separate children with '.' dots. Returns None if not found. """
        pass
        
        
    
    def renameInputPort(self, name, newName):
        """ renameInputPort(name, newName)
        Renames an input port. Returns the resulting unique name """
        pass
        
        
    
    def setType(self, typeName):
        """ setType(typeName)
        Sets a string naming the registered type of this node. """
        pass
        
        
    
    def getNumOutputPorts(self):
        """ getNumOutputPorts() -> int
        Returns the number of output ports on the node. """
        pass
        
        
    
    def getBoolValue(self, name):
        """ getBoolValue(name) -> bool
        Returns the bool value of a named (string) parameter. Separate children with '.' dots. Returns None if not found. """
        pass
        
        
    
    def addOutputPortAtIndex(self, name, index):
        """ addOutputPortAtIndex(name, index) -> Port
        Creates a new output port at a specific index, and returns it. """
        pass
        
        
    
    def setParent(self, groupNode):
        """ setParent(groupNode) -> bool
        Sets the new parent group for this node. Can be None for no parent. Returns True if reparent successful. """
        pass
        
        
    
    def getName(self):
        """ getName() -> str
        Returns the unique name for the node. """
        pass
        
        
    
    def setBypassRouting(self, dict(int:int):
        """ setBypassRouting(dict(int:int))
        Sets the dict of port routing when bypassed. outputindex : inputindex """
        pass
        
        
    
    def getBaseType(self):
        """ getBaseType()
        Returns a string naming the real base type of this node. """
        pass
        
        
    
    def isLocked(self, considerParents=False):
        """ isLocked(considerParents=False) -> bool
        True if the node is locked to prevent changes, otherwise False. The considerParents flag controls whether the content-locked states of ancestor nodes are taken into account: child nodes of content-locked ancestor nodes are locked against edits in the UI, but can still be modified using the NodegraphAPI (unless they are locked themselves). """
        pass
        
        
    
    def renameOutputPort(self, name, newName):
        """ renameOutputPort(name, newName)
        Renames an output port. Returns the resulting unique name. """
        pass
        
        
    
    def getBypassRouting(self):
        """ getBypassRouting() -> dict(int:int)
        Returns the dict of port routing when bypassed. outputindex : inputindex """
        pass
        
        
    
    def isMarkedForDeletion(self):
        """ isMarkedForDeletion() -> bool
        True if the node has been deleted (node.delete), but hasn't yet been deallocated by the deletion queue. """
        pass
        
        
    
    def getOutputPortByIndex(self, index):
        """ getOutputPortByIndex(index) -> Port
        Returns one of the output ports by index. Returns None if out of range. """
        pass
        
        
    
    def getInputPortByIndex(self, index):
        """ getInputPortByIndex(index) -> Port
        Returns one of the input ports by index. Returns None if out of range. """
        pass
        
        
    
    def removeOutputPort(self, name):
        """ removeOutputPort(name)
        Deletes an output port by name, breaking any connections it had. """
        pass
        
        
    
    def getType(self):
        """ getType() -> str
        Returns a string naming the registered type of this node. """
        pass
        
        
    
    def getInputPorts(self):
        """ getInputPorts() -> list of Port
        Returns a new list containing all the input ports. """
        pass
        
        
    
    def setName(self, name):
        """ setName(name)
        Sets the name for a node. The real unique name is returned. """
        pass
        
        
    
    def getInputSource(self, name, graphState):
        """ getInputSource(name, graphState) -> Port, GraphState
        Returns the port connected to an input port by name as a (Port, GraphState) tuple. Port will by None if not found. """
        pass
        
        
    
    def setLocked(self, bool):
        """ setLocked(bool)
        Locks or unlocks the node to prevent or allow changes. """
        pass
        
        
    
    def removeInputPort(self, name):
        """ removeInputPort(name)
        Deletes an input port by name, breaking any connections it had. """
        pass
        
        
    
    def getInfoString(self):
        """ getInfoString() -> string
        Returns a brief (and optional) description of the node's state given its parameters """
        pass
        
        
    
    def setBypassed(self, state):
        """ setBypassed(state)
        Enables or disables the node according to the given bypassed state. """
        pass
        
        
    
    def isAutoRenameAllowed(self):
        """ isAutoRenameAllowed() -> bool
        True if the node is locked from auto-name changes. """
        pass
        
        
    
    def isBypassed(self):
        """ isBypassed() -> bool
        True if the node state is set to bypassed. """
        pass
        
        
    
    def getGraphState(self, Node, GraphState):
        """ getGraphState(Node, GraphState) -> GraphState
        Builds and returns a GraphState object, starting from the given Node and GraphState, walking up the node graph until we reach this Node. If this Node is never reached (because it's not being cooked due to current GraphState), None is returned. If the input Node is not given, the currently viewed node will be used. If the input GraphState is not given, the current GraphState will be used. """
        pass
        
        
    
    def getOutputPort(self, name):
        """ getOutputPort(name) -> Port
        Returns an output port from the node by name. Returns None if not found. """
        pass
        
        
    
    def getParameters(self):
        """ getParameters() -> Parameter
        Returns the top-level group parameter that contains all the node's parameters. """
        pass
        
        
    
    def setAttributes(self, dict):
        """ setAttributes(dict)
        Assigns new named persistent values to the node with a string keyed dictionary. """
        pass
        
        
    
    def customReset(self):
        """ customReset() -> bool
        Resets node parameters to factory settings.  Returns true if a customReset is implemented.
        If false is returned, a generic parameter-by-parameter sync will be attempted. """
        pass
        
        
    
    def parseParameters(self, xmlString):
        """ parseParameters(xmlString)
        Adds new parameters to a node, from a given string of XML. """
        pass
        
        
    
    def getParent(self):
        """ getParent() -> Node
        Returns the GroupNode that is the parent of this node, or None. """
        pass
        
        
    
    def getLogicalInputPort(self, port, graphState):
        """ getLogicalInputPort(port, graphState) -> (Port, GraphState)
        Returns the input port of this node that is used in producing the data of the given port as a tuple of (port, graphState). Port will be None if not found. """
        pass
        
        
    
    def isResetPossible(self):
        """ isResetPossible() -> bool
        True if the node can be reset (either by a generic parameter reset or by calling
        the customReset() method). """
        pass
        
        
    
    def getDefaultParameter(self, name):
        """ getDefaultParameter(name) -> Parameter
        Returns a nested default parameter by name. Separate children with '.' dots. Returns None if not found. """
        pass
        
        
    
    def getAttributes(self):
        """ getAttributes() -> dict
        Returns a dictionary of named static values that are persistent with the node. """
        pass
        
        
    
    def getSourcePort(self, port, graphState):
        """ getSourcePort(port, graphState) -> Port
        Returns the output port that produces the data of the given port (which may be an upstream output port in the case of nodes being bypassed) as a tuple of (port, graphState). Port will be None if not found. """
        pass
        
        
    
    def addInputPort(self, name):
        """ addInputPort(name) -> Port
        Creates a new input port with the given name, and returns it. """
        pass
        
        
    
    def getOutputPorts(self):
        """ getOutputPorts() -> list of Port
        Returns a new list containing all the output ports. """
        pass
        
        
    
    def loadEnd(self):
        """ loadEnd()
        Called during load after a node's parameters and children have been built. Youshould not need to call this yourself. """
        pass
        
        
    
    def setAutoRenameAllowed(self, bool):
        """ setAutoRenameAllowed(bool) -> bool
        Locks or unlocks the node from auto-name changes. """
        pass
        
        
    
    def delete(self):
        """ delete()
        Deletes the node and any children it contains. """
        pass
        
        

def NodeMatchesFlavors():
    """ Return True if the node type matches the list of flavors.
    The flavors represent the required flavors to use, or None
    for all. The match will fail if ignoreFlavors is given
    and matches one of the flavors.
    
    @param nodeType: C{str}
    @param flavors: C{sequence} of C{str}
    @param ignoreFlavors: C{sequence} of C{str}
    @return: C{bool}
    """
    pass
    
    

def AsynchronousContext():
    """
    Context manager that undoes the effects of the L{SynchronousContext}
    context manager.
    When using the C{AsynchronousContext} context manager, users should
    explicitly process events when needed or otherwise be aware that
    correctness of the result is not guaranteed.
    """
    pass
    
    

class Parameter(object):
    """ Node Parameter Type.Node Parameters contain values or arrays of values on nodes. They can be typed as strings for floating point numbers. Group parameters can contain other parameters and create a hierarchy of values from the node. Parameters are created by XML string containing parameter descriptions.  """
    
    def createChildNumberArray(self, name, size, index=-1):
        """ createChildNumberArray(name, size, index=-1)
        Create a new number array parameter. Return new param. """
        pass
        
        
    
    def parseXML(self, xmlString):
        """ parseXML(xmlString)
        Builds new parameters from an XML definition. """
        pass
        
        
    
    def hasFloatingCurve(self):
        """ hasFloatingCurve() -> bool
        Returns True if number parameter currently has a floating curve. """
        pass
        
        
    
    def moveKeys(self, timeSequence, dt):
        """ moveKeys(timeSequence, dt)
        Moves keys (by deleting and re-creating) by a given time offset. """
        pass
        
        
    
    def getChildren(self):
        """ getChildren() -> list of Parameter
        Return a new list of all the children parameters. """
        pass
        
        
    
    def writeOpaqueDataToXmlIO(self):
        """ writeOpaqueDataToXmlIO() -> PyXmlIO element
        Opaque parameters only: returns opaque PyXmlIO structure to be inserted into katana scene xml as child of opaque_parameter tag. """
        pass
        
        
    
    def deleteChild(self, childParameter):
        """ deleteChild(childParameter)
        Delete a group child parameter from xml string. """
        pass
        
        
    
    def setSamples(self, {time:, [values]}, final=True):
        """ setSamples({time: [values]}, final=True) -> None
        Set a float vector's samples.If the parameter is not a float vector, no effect. """
        pass
        
        
    
    def removeKeys(self, timeSequence):
        """ removeKeys(timeSequence)
        Unsets keyed values at the listed times. """
        pass
        
        
    
    def replaceXmlIO(self, PyXmlIO.Element, destroyChildren=True):
        """ replaceXmlIO(PyXmlIO.Element, destroyChildren=True)
        Redefines an existing parameter with an xml element. Can optionally delete existing children. """
        pass
        
        
    
    def setValueAutoKey(self, value, time, final=True):
        """ setValueAutoKey(value, time, final=True)
        Sets the value of the parameter at the given time. The value's type is dictated by the parameter type; float, curve, etc. If this is an interactive value, set final=False. """
        pass
        
        
    
    def getExpression(self):
        """ getExpression() -> str
        Returns the string of the expression that controls the parameter (when it is enabled). """
        pass
        
        
    
    def setExpressionFlag(self, bool):
        """ setExpressionFlag(bool)
        Enables or disables the expression to control the parameter value. """
        pass
        
        
    
    def readOpaqueDataFromFile(self, [filename, ...]):
        """ readOpaqueDataFromFile([filename, ...])
        Opaque parameters only: reads opaque data from a series of files specified by input parameter. """
        pass
        
        
    
    def reorderChildren(self, oldIndex, newIndex, count):
        """ reorderChildren(oldIndex, newIndex, count)
        Move the given number of child parameters from the given old index to the given new index. """
        pass
        
        
    
    def getXML(self, forcePersistant=False):
        """ getXML(forcePersistant=False) -> str
        Returns a string representing the parameter definition as XML.
        If forcePersistant is True, will write all parameters, even the non-persistant. """
        pass
        
        
    
    def hasKey(self, time):
        """ hasKey(time) -> bool
        True if the animated parameter has a keyed value at the given time. """
        pass
        
        
    
    def getCurve(self):
        """ getCurve() -> FCurve
        Get the FCurve object representing the animated values for this parameter. """
        pass
        
        
    
    def getSamples(self):
        """ getSamples() -> {time: [values]}
        Return a float vector's samples.If the parameter is not a float vector, return None. """
        pass
        
        
    
    def sendSignal_finalize(self, **kwargs):
        """ sendSignal_finalize(**kwargs) -> None
        Queue a parameter_finalizeValue signal.
        Any keyword arguments are added to the signal's argument dict. """
        pass
        
        
    
    def getNode(self):
        """ getNode() -> Node
        Get the node that contains this parameter. """
        pass
        
        
    
    def reparentAtomic(self, newParentParameter):
        """ reparentAtomic(newParentParameter)
        Atomically reparent a parameter from its current parent to a new parent.
        This is used in place of sequential removeChild and addChild
        to avoid excess XML generation.
        Returns the new name of the parameter under the new parent, or None. """
        pass
        
        
    
    def finalizeValue(self):
        """ finalizeValue()
        Hardens the value of a parameter after it has been interactively modified.
        This simply calls through to sendSignal_finalize. """
        pass
        
        
    
    def getKeys(self):
        """ getKeys() -> list of float
        Get a list of the times for each animated key. """
        pass
        
        
    
    def renameExpression(self, oldName, newName):
        """ renameExpression(oldName, newName)
        Performs node name string substitution on the expression. This usually happens automatically. """
        pass
        
        
    
    def createChildNumber(self, name, value, index=-1):
        """ createChildNumber(name, value, index=-1)
        Create a new number parameter. Return new param. """
        pass
        
        
    
    def getInterpolation(self):
        """ getInterpolation() -> enum
        Return the interpolation type enum. This is only used on vector_parameters, and has no relation to fcurves. """
        pass
        
        
    
    def getHintString(self):
        """ getHintString() -> string
        Return a parameter's hint string -- or an empty string on absence """
        pass
        
        
    
    def getName(self):
        """ getName() -> str
        Get the string name of this parameter. """
        pass
        
        
    
    def getChildByIndex(self, index):
        """ getChildByIndex(index) -> Parameter
        Get a child parameter by index. Returns None if out of range. """
        pass
        
        
    
    def getFullName(self, includeNodeName=True):
        """ getFullName(includeNodeName=True) -> str
        Returns the full string name of this parameter from the node. Parameters are separated by '.' dots.
        """
        pass
        
        
    
    def getExpressionError(self):
        """ getExpressionError() -> str
        Returns a string description of any evaluation errors of the expression. """
        pass
        
        
    
    def setCurve(self, FCurve, final=True):
        """ setCurve(FCurve, final=True)
        Set the FCurve object representing the animated values for this number parameter. """
        pass
        
        
    
    def setValue(self, value, time, final=True, sendNotifyMessage=True):
        """ setValue(value, time, final=True, sendNotifyMessage=True)
        Sets the value of the parameter at the given time. The value is a string or float. If this is an interactive value, set the 'final' keyword argument to False. """
        pass
        
        
    
    def isPersistant(self):
        """ isPersistant() -> bool
        Return True if the Parameter value will be written out. This is True by default. """
        pass
        
        
    
    def getFileSequenceValue(self, time):
        """ getFileSequenceValue(time) -> str
        Gets the string of the parameter at the given time. Filename expansion is performed on the string. """
        pass
        
        
    
    def reorderChild(self, childParameter, index):
        """ reorderChild(childParameter, index)
        Move a child parameter. """
        pass
        
        
    
    def setTupleSize(self, length):
        """ setTupleSize(length)
        Sets the number of array values to bundle in the value representation. """
        pass
        
        
    
    def createChildStringArray(self, name, size, index=-1):
        """ createChildStringArray(name, size, index=-1)
        Create a new string array parameter. Return new param. """
        pass
        
        
    
    def createChildGroup(self, name, index=-1):
        """ createChildGroup(name, index=-1)
        Create a new group parameter. Return new param. """
        pass
        
        
    
    def removeKey(self, time):
        """ removeKey(time)
        Unsets a keyed value at the given time. """
        pass
        
        
    
    def reparentExpression(self, oldName, newName):
        """ renameExpression(oldName, newName)
        Performs node name string substitution on the expression. This usually happens automatically. """
        pass
        
        
    
    def useNodeDefault(self):
        """ useNodeDefault()
        """
        pass
        
        
    
    def isExpression(self):
        """ isExpression() -> bool
        True if the parameter defines an expression to compute the value. """
        pass
        
        
    
    def createChildXmlIO(self, element, index=-1):
        """ createChildXmlIO(element, index=-1)
        Create a new child parameter from any parameter XmlIO element. Return new param. """
        pass
        
        
    
    def isAnimated(self):
        """ isAnimated() -> bool
        True if the parameter contains keyframes to interpolate the value. """
        pass
        
        
    
    def getNumChildren(self):
        """ getNumChildren() -> int
        Get the number of children parameters. Value is zero or greater. """
        pass
        
        
    
    def getAutoKey(self):
        """ getAutoKey() -> bool
        Return the parameter's autokey flag (if True, setValue() will create a key). """
        pass
        
        
    
    def getTupleSize(self):
        """ getTupleSize() -> int
        Gets the number of array values to bundle in the value representation. """
        pass
        
        
    
    def sendSignal_setValue(self, **kwargs):
        """ sendSignal_setValue(**kwargs) -> None
        Queue a parameter_setValue signal.
        Any keyword arguments are added to the signal's argument dict. """
        pass
        
        
    
    def getChild(self, name):
        """ getChild(name) -> Parameter
        Get a child parameter by name. Returns None if not found. """
        pass
        
        
    
    def setName(self, str):
        """ setName(str)
        Set the string name of this parameter. If a sibling already has the given name, a numeric index will be added to the end and incremented until a unique name is generated. This will only work on parameters that are children of dynamic. Returns the actual new name of the parameter. """
        pass
        
        
    
    def insertArrayElement(self, index):
        """ insertArrayElement(index)
        Insert a new value into an array parameter. """
        pass
        
        
    
    def staticmethod(self, function):
        """ staticmethod(function) -> method
        
        Convert a function to be a static method.
        
        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:
        
        class C:
        def f(arg1, arg2, ...): ...
        f = staticmethod(f)
        
        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()).  The instance is ignored except for its class.
        
        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin. """
        pass
        
        
    
    def getReferences(self, time):
        """ getReferences(time) -> str or float
        Returns a list of parameters evaluated during the process of evaluating this one (including itself). """
        pass
        
        
    
    def setExpression(self, string, enable=True):
        """ setExpression(string, enable=True)
        Defines a new string to control the parameter value. """
        pass
        
        
    
    def resizeArray(self, length):
        """ resizeArray(length)
        Sets the new number of values on an array parameter. """
        pass
        
        
    
    def readOpaqueDataFromXmlIO(self, PyXmlIO, element):
        """ readOpaqueDataFromXmlIO(PyXmlIO element)
        Opaque parameters only: reads data from opaque PyXmlIO structure. """
        pass
        
        
    
    def resetFloatingCurve(self):
        """ resetFloatingCurve()
        Removes floating curve from a number parameter. """
        pass
        
        
    
    def getParent(self):
        """ getParent() -> Parameter
        Get the parent parameter of this parameter. Returns None if this is the top level parameter. """
        pass
        
        
    
    def getValue(self, time):
        """ getValue(time) -> str or float
        Gets the value of the parameter at the given time. The value can be a string, a float, or an FCurve. """
        pass
        
        
    
    def setAutoKey(self, autoKey):
        """ setAutoKey(autoKey)
        Set the parameter's autokey flag (if True, setValue() will create a key). """
        pass
        
        
    
    def buildXmlIO(self, forcePersistant=False):
        """ buildXmlIO(forcePersistant=False)
        Builds xml element representing parameter data. """
        pass
        
        
    
    def getValueXmlIO(self, PyXmlIO.Element, time):
        """ getValueXmlIO(PyXmlIO.Element, time) -> None
        Add this parameter's value at a time to an XmlIO element.
        Set attributes on or add children to the given element. """
        pass
        
        
    
    def setInterpolation(self, enum, final=True):
        """ setInterpolation(enum, final=True) -> void
        Sets the interpolation type. This is only used on vector_parameters, and has no effect on fcurves. """
        pass
        
        
    
    def hasUseNodeDefault(self):
        """ hasUseNodeDefault()
        """
        pass
        
        
    
    def removeArrayElements(self, index, count):
        """ removeArrayElements(index, count)
        Removes a number of values from an array parameter. """
        pass
        
        
    
    def removeArrayElement(self, index):
        """ removeArrayElement(index)
        Remove a value from an array parameter. """
        pass
        
        
    
    def getIndex(self):
        """ getIndex() -> int
        Returns the index we are within our parent. """
        pass
        
        
    
    def setHintString(self, value):
        """ setHintString(value)
        Set the parameter's hint string. """
        pass
        
        
    
    def writeOpaqueDataToFile(self, [filename, ...]):
        """ writeOpaqueDataToFile([filename, ...])
        Opaque parameters only: writes opaque data to a series of files specified by input parameter. """
        pass
        
        
    
    def setPersistant(self, persist):
        """ setPersistant(persist)
        Set the parameter's persist flag (if True, value will be written). """
        pass
        
        
    
    def setKey(self, time, sendNotifyMessage=True):
        """ setKey(time, sendNotifyMessage=True)
        Sets the value at a given time as an animated key value. """
        pass
        
        
    
    def makeConstant(self, time):
        """ makeConstant(time)
        Set number parameter to a constant value (reset curve and/or expression). The new value will be the previous animated value evaluated at 'time'. """
        pass
        
        
    
    def getType(self):
        """ getType() -> str
        Returns a string defining the type of the parameter. It is one of 'number',     'numberArray', 'string', 'stringArray', 'curve', or 'group'. """
        pass
        
        
    
    def replaceXML(self, xmlString, destroyChildren=1):
        """ replaceXML(xmlString, destroyChildren=1)
        Redefines an existing parameter with an XML definition. Can optionally delete existing children. """
        pass
        
        
    
    def createChildString(self, name, value, index=-1):
        """ createChildString(name, value, index=-1)
        Create a new string parameter. Return new param. """
        pass
        
        
    
    def sendSignal_setKey(self, keyTime):
        """ sendSignal_setKey(keyTime) -> None
        Queue a parameter_setKey signal.
        @param keyTime: keyTime value for the signal's argument dict """
        pass
        
        
    
    def setValueXmlIO(self, PyXmlIO.Element, time, final=True, sendNotifyMessage=True):
        """ setValueXmlIO(PyXmlIO.Element, time, final=True, sendNotifyMessage=True) -> None
        Set this parameter's value from an XmlIO element.
        Read from attributes or children on the given element.
        @see: getValueXmlIO """
        pass
        
        
    
    def staticmethod(self, function):
        """ staticmethod(function) -> method
        
        Convert a function to be a static method.
        
        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:
        
        class C:
        def f(arg1, arg2, ...): ...
        f = staticmethod(f)
        
        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()).  The instance is ignored except for its class.
        
        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin. """
        pass
        
        
    
    def getOpaqueDataInfo(self):
        """ getOpaqueDataInfo() -> {info dict}
        Opaque parameters only: returns (as dictionary) the necessary setup information for serializing opaque data. """
        pass
        
        
    
    def parseXmlIO(self, PyXmlIO.Element):
        """ parseXmlIO(PyXmlIO.Element)
        Builds new parameters from an xml element. """
        pass
        
        
    
    def setUseNodeDefault(self, value):
        """ setUseNodeDefault(value)
        """
        pass
        
        

def ParseNodegraphXmlIO():
    """
    Replaces the current Katana scene with a new scene loaded from the given
    XML element. The XML node graph will be upgraded to the current version.
    
    @type element: C{PyXmlIO.Element}
    @type sourcePath: C{str}
    @type isCrashFile: C{bool}
    @param element: An XML element that represents the root of the new Katana
    scene to create.
    @param sourcePath: The full path of a Katana file from which the given
    element was created, or an empty string to reset the current Katana
    scene filename.
    @param isCrashFile: Flag indicating whether the file with the given source
    path has been saved as an autosave from which a project can be restored
    after a crash.
    """
    pass
    
    

def ParseNodesXmlIO():
    """
    Loads a scene from the given XML element into the current Katana scene.
    The XML node graph will be upgraded to the current version.
    
    @type element: C{PyXmlIO.Element}
    @type emit: C{bool}
    @type floatNodes: C{bool}
    @type sourcePath: C{str}
    @type loadLiveGroups: C{bool}
    @type lockLiveGroups: C{bool}
    @rtype: C{list}
    @param element: An XML element that represents the root of the Katana scene
    to load into the current Katana scene.
    @param emit: Flag that controls the type of events added to Katana's event
    queue. It set to C{True}, C{"nodegraph_loadBegin"} and
    C{"nodegraph_loadEnd"} events are added at the start and end of the
    loading process, respectively. If set to C{False},
    C{"nodegraph_silentLoadBegin"} and C{"nodegraph_silentLoadEnd"} events
    are used instead.
    @param floatNodes: Flag that controls whether the loaded nodes are to be
    floating in the B{Node Graph} tab, so that the user can place them
    manually, or whether the node positions stored in the given node graph
    are used to place the loaded nodes in the current Katana scene.
    @param sourcePath: The full path of a Katana file from which the given
    element was created, or an empty string if the element was not created
    from a Katana file. Only used for log messages.
    @param loadLiveGroups: Flag that controls whether to load all new LiveGroup
    nodes in the scene.
    @param lockLiveGroups: Flag that controls whether to lock all new LiveGroup
    nodes in the scene. Only effective when C{loadLiveGroups} is set to
    C{True}.
    @return: A list of nodes that are present in the root level of the loaded
    Katana scene.
    """
    pass
    
    

def PopExpressionCache():
    """ None """
    pass
    
    

class Port(object):
    """ Node Port Type.Ports are used to connected nodes to each other. Ports are either of type Port.TYPE_PRODUCER or Port.TYPE_CONSUMER. They are connected to nodes of the other type, and a consumer can have only a single connection. Ports are accessed through the nodes they are contained by.
    
    It is better to refer to ports by their name than the index number. """
    
    def getMetadata(self, str):
        """ getMetadata(str) -> str
        Returns a metadata entry based on the given key. If the given doesn't exist, C{None} will be returned. """
        pass
        
        
    
    def isConnected(self, otherPort):
        """ isConnected(otherPort) -> bool
        True if the port is connected to otherPort. """
        pass
        
        
    
    def connect(self, otherPort):
        """ connect(otherPort) -> bool
        Connects a port to the given port. If the nodes to which the ports belong are not part of the same parent node, in-between connections along the way are created.
        Returns True if the port connection was successfully established, otherwise False if recursion was detected, nodes were locked or if other problems occurred. """
        pass
        
        
    
    def deleteMetadata(self, str):
        """ deleteMetadata(str)
        Deletes a metadata entry based on the given key. The method has no effect if the given key doesn't exist. """
        pass
        
        
    
    def getDisplayName(self):
        """ getDisplayName() -> str
        Get a UI-friendly name for this port that may consist of a label
        and the names of pages as defined in metadata on this port. """
        pass
        
        
    
    def getIndex(self):
        """ getIndex() -> int
        Returns the index of this port inside its node. """
        pass
        
        
    
    def getConnectedPort(self, index):
        """ getConnectedPort(index) -> Port
        Gets one of the other ports this is connected to, or None if index is out of range. """
        pass
        
        
    
    def getName(self):
        """ getName() -> str
        Get the name that refers to this port. """
        pass
        
        
    
    def getNumConnectedPorts(self):
        """ getNumConnectedPorts() -> int
        The number of other ports this port is connected to, can be zero or greater. """
        pass
        
        
    
    def getFlavor(self):
        """ getFlavor() -> int
        Returns the flavor of this port (Port.FLAVOR_STANDARD, Port.FLAVOR_MASK, Port.FLAVOR_DEPENDENCY). """
        pass
        
        
    
    def getMetadataDict(self):
        """ getMetadataDict() -> dict(str -> str)
        Returns a dictionary of key/value C{str} pairs containing all the metadata defined for the port. """
        pass
        
        
    
    def getType(self):
        """ getType() -> int
        Returns the type of this port (Port.TYPE_PRODUCER, Port.TYPE_CONSUMER). """
        pass
        
        
    
    def disconnect(self, otherPort):
        """ disconnect(otherPort) -> bool
        Disconnects a port from the given port. Does nothing if the ports are not directly connected.
        Returns True if the ports were successfully disconnected, otherwise False. """
        pass
        
        
    
    def getTags(self):
        """ getTags() -> list(str)
        Gets the allowed data types that can be connected to this port.None if no allowed data types have been set. """
        pass
        
        
    
    def addOrUpdateMetadata(self, str, str):
        """ addOrUpdateMetadata(str, str)
        Adds or updates a metadata entry, specified by a key/value pair, on this port. """
        pass
        
        
    
    def setTags(self, list/tuple(str):
        """ setTags(list/tuple(str))
        Sets the allowed data types that can be connected to this port . """
        pass
        
        
    
    def getConnectedPorts(self):
        """ getConnectedPorts() -> list of Port
        Returns a new list of all the ports connected to this one. """
        pass
        
        
    
    def getNode(self):
        """ getNode() -> Node or None
        Return the node that owns this port, or None if this port is orphaned. """
        pass
        
        

def PushExpressionCache():
    """ None """
    pass
    
    

class PythonGroupNode(GroupNode):
    """ Base class for Python Group nodes. """

class PythonNode(Node):
    """ Base class for python nodes. """

class PythonRenderScript(PythonNode):
    """ None """
    
    def renderFrame(self):
        """ None """
        pass
        
        
    
    def addParameterHints(self):
        """ None """
        pass
        
        
    
    def postRenderPublish(self):
        """ None """
        pass
        
        
    
    def preRenderPublish(self):
        """ None """
        pass
        
        
    
    def getActiveContexts(self):
        """ None """
        pass
        
        

def RegisterExtension():
    """ Register a new L{Node} extension. The extensions are an
    advanced way to tag additional persistent data to the
    L{Node}s. The extension object is required to have
    the following functions::
    
    - NewNode(node): called when a node is created
    - GetAttributes(node): get a dictionary of attributes to save
    - SetAttributes(node, attrs): load a dictionary of attributes
    
    The extension should fill a simple dictionary of values to
    write into the node xml stream. When the node is loaded the
    C{SetAttributes} will be called with all xml attributes saved
    with the node.
    
    @return: Object with special methods
    """
    pass
    
    

def RegisterPythonGroupType():
    """ Register a python group node class.
    The ctor class argument must be derived from L{PythonGroupNode}.
    The constructor will be called with no arguments when the
    requested node type is created.
    
    @attention: Registering a type name that already exists will
    terminate the process.
    @param type: Name of the node type.
    @type type: C{str}
    @param ctor: The node class
    @type ctor: C{type} of L{PythonGroupNode}
    """
    pass
    
    

def RegisterPythonNodeFactory():
    """ Register a callback to create nodes.
    The L{Node} factory must create and return a single node.
    It is almost always required that the callback disables
    the undo stack while it builds and decorates the node.
    
    The callback must have the following signature::
    def factory(type): return Node
    
    @attention: Registering a type name that already exists will
    terminate the process.
    @param type: Name of the node type.
    @type type: C{str}
    @param factory: Callback to create the node
    @type factory: C{function}
    """
    pass
    
    

def RegisterPythonNodeType():
    """ Register a python node class.
    The ctor class argument must be derived from L{PythonNode}.
    The constructor will be called with no arguments when the
    requested node type is created.
    
    @attention: Registering a type name that already exists will
    terminate the process.
    @param type: Name of the node type.
    @type type: C{str}
    @param ctor: The node class
    @type ctor: C{type} of L{PythonNode}
    """
    pass
    
    

def RegisterSuperTool():
    """ Register a new SuperTool. Give the name of the node
    and a class derived from SuperTool.
    """
    pass
    
    

def Register_NewNode_CB():
    """ None """
    pass
    
    

def RemoveNodeFlavor():
    """ Untag a node type with a flavor.
    This is safe to call if the node has never been tagged
    with this flavor, or neither has been previously registered.
    
    @param nodeType: C{str} of the node name
    @param flavor: C{str} of the flavor name
    """
    pass
    
    

def ResetAllFloatingCurves():
    """ Reset all uncommitted keyframes.
    This happens automatically on a frame change.
    """
    pass
    
    

def SetAllSelectedNodes():
    """ Replace the nodes that are selected.
    If the sequence of nodes is empty, all nodes will be unselected.
    Interface operations that effect nodes will be applied
    to selected nodes. There can be any number of selected
    nodes at a time.
    
    @type nodelist: sequence of L{Node}
    """
    pass
    
    

def SetAttributeEditorNodeActive():
    """ None """
    pass
    
    

def SetAutoKeyAll():
    """ Set the auto keyframing on or off.
    When autokeying is turned on, parameter value changes on
    parameters that are curves will be automatically keyed.
    Otherwise changes are applied to a temporary floating
    keyframe.
    
    @type autoKeyAll: C{bool}
    """
    pass
    
    

def SetCurrentTime():
    """
    Sets the current time on the timeline to the given time.
    
    @type newTime: C{number}
    @type final: C{bool}
    @param newTime: The time to set as the current time on the timeline.
    @param final: Flag to control whether to add a C{"parameter_finalizeValue"}
    event to Katana's event queue.
    @see: L{GetInTime()}, L{GetOutTime()}
    """
    pass
    
    

def SetEventsEnabled():
    """ Enables or disables generation of events in response to Nodegraph
    changes.
    
    @attention: Many things depend upon nodegraph events to function
    property. This should rarely be called and only when the state
    of the nodegraph can be guaranteed to be returned to exactly
    the same condition. In order words, you probably shouldn't
    ever call it.
    
    @param state: enable or disable.
    @type state: C{int}
    """
    pass
    
    

def SetExpressionGlobalValue():
    """ When L{Parameter} values are set to expression mode, they
    are evaluated inside a custom namespace. This function
    will set add or replace a value with the given name.
    
    @param name: Name of the new object.
    @type name: C{str}
    @param value: The value if the new object
    """
    pass
    
    

def SetInTime():
    """ Set the in frame.
    The in time must be lesser than the out time.
    
    @type inTime: C{number}
    """
    pass
    
    

def SetKatanaSceneName():
    """ None """
    pass
    
    

def SetLiveGroupCachingEnabled():
    """ None """
    pass
    
    

def SetLiveGroupLoadingEnabled():
    """ None """
    pass
    
    

def SetMenuPath():
    """ None """
    pass
    
    

def SetNeedsRedraw():
    """ None """
    pass
    
    

def SetNodeComment():
    """ Set the user comment.
    """
    pass
    
    

def SetNodeEdited():
    """ Set if the node parameters are displayed.
    When nodes are edited their parameters are displayed in the
    user interface. There can be none or several nodes edited at
    once time.  If optional exclusive arg is True, all nodes are
    unedited before setting the edited flag on specified node.
    
    @type node: L{Node}
    @type edited: C{bool}
    @type exclusive: C{bool}
    """
    pass
    
    

def SetNodeFloating():
    """ Set if the node is tracking the mouse position.
    When nodes are interactively created or moved, they become
    floating nodes. Floating nodes track with the mouse movement
    until they are placed.
    
    @type node: L{Node}
    @type flag: C{bool}
    """
    pass
    
    

def SetNodeHidden():
    """ None """
    pass
    
    

def SetNodeModTime():
    """ Set the modification time of the file loaded into a LiveGroup node.
    This attribute should only be set on LiveGroup nodes.
    
    @type node: L{Node}
    @param modTime: the new modification time
    @type modTime: C{int}
    """
    pass
    
    

def SetNodeParameter():
    """ None """
    pass
    
    

def SetNodePosition():
    """ Set the 2D position of the node.
    The position is in y-down integers.
    
    @type node: L{Node}
    @param xy: the new node position
    @type xy: C{int}, C{int}
    """
    pass
    
    

def SetNodeSelected():
    """ Set if the node is selected in the interface.
    Interface operations that effect nodes will be applied
    to selected nodes. There can be any number of selected
    nodes at a time.
    
    @type node: L{Node}
    @type selected: C{bool}
    """
    pass
    
    

def SetNodeShapeAttr():
    """ None """
    pass
    
    

def SetNodeShapeNodeAttrs():
    """ None """
    pass
    
    

def SetNodeThumbnailEnabled():
    """ None """
    pass
    
    

def SetNodeViewed():
    """ Set if the node results are displayed.
    When the node is viewed, its output is displayed in the
    interface.  If optional exclusive arg is True, all nodes are
    unviewed before setting the view flag on specified node.
    
    @type node: L{Node}
    @type viewed: C{bool}
    @type exclusive: C{bool}
    """
    pass
    
    

def SetOriginalProjectAssetID():
    """
    Sets the name of the original file or the ID of the original asset that
    the current project was last saved as before loading.
    
    @type originalProjectAsssetID: C{str}
    @param: The name of the original file or the ID of the original asset that
    the current project was last saved as before loading.
    """
    pass
    
    

def SetOriginalSourceFile():
    """ None """
    pass
    
    

def SetOutTime():
    """ Set the end frame.
    The out time must be greater than the in time.
    
    @type outTime: C{number}
    """
    pass
    
    

def SetProjectAssetID():
    """
    Sets the name of the file or the ID of the asset that the current project
    was loaded from.
    
    @type filenameOrAssetID: C{str}
    @param filenameOrAssetID: The name of the file or the ID of the asset that
    the current project was loaded from.
    """
    pass
    
    

def SetRootNode():
    """ None """
    pass
    
    

def SetSourceFile():
    """
    Sets the name of the file or the ID of the asset that the current project
    was loaded from.
    
    @type filenameOrAssetID: C{str}
    @param filenameOrAssetID: The name of the file or the ID of the asset that
    the current project was loaded from.
    """
    pass
    
    

def SetTimeIncrement():
    """ Set the time increment when a single frame is advanced.
    This value is usually 1.
    
    @type incTime: C{number}
    """
    pass
    
    

def SetUserNodesXmlRootAttrs():
    """ None """
    pass
    
    

def SetViewPortPosition():
    """ Set the view information for a group network.
    Each L{GroupNode} also maintains view information for its
    child network. It is stored in this viewport. The return
    contains the eyepoint and the viewscale.
    
    - The default vewpoint is C{0, 0, 10000}
    - The default viewscale is C{1, 1, 1}
    
    @type node: L{GroupNode}
    @type eyepoint: C{int}, C{int}, C{int}
    @type viewscale: C{float}, C{float}, C{float}
    """
    pass
    
    

def SetWorkingInTime():
    """ Set the working-range in time.
    
    @type workingInTime: C{number}
    """
    pass
    
    

def SetWorkingOutTime():
    """ Set the working-range out time.
    
    @type workingOutTime: C{number}
    """
    pass
    
    

def SetupExpressionGlobalScopeFromRootNode():
    """ None """
    pass
    
    

class SuperTool(PythonGroupNode):
    """ Class used for super tool plugins. Each SuperTool instance is
    attached to a SuperTool delegate. The delegate is a set of functions
    that are presented as methods on the SuperTool instance.
    """
    
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
        
        
    
    def polish(self):
        """ This method is automatically called on the SuperTool
        after it has finished loading and initialization.
        It will only be called once.
        """
        pass
        
        
    
    def hideNodegraphGroupControls(self):
        """ Remove the group-like controls for this node from the
        Node Graph tab. Should be called from the init method.
        """
        pass
        
        

def SynchronousContext():
    """
    Context manager that ensures that changes to parameters are taken into
    account when cooking the scene. All Katana events are processed before and
    after running code that is scoped with this context manager.
    Is used when running Python scripts in script mode and when executing
    Python code in the B{Python} tab.
    """
    pass
    
    

def UpdateAllLiveGroupSources():
    """
    Finds all LiveGroup nodes referencing the given C{oldSource} file or asset
    and changes them to reference the given C{newSource} file or asset.
    
    @type oldSource: C{str}
    @type newSource: C{str}
    @param oldSource: The old filename or asset ID.
    @param newSource: The new filename or asset ID.
    """
    pass
    
    

def UpdatePluginsFromGlobals():
    """ None """
    pass
    
    

def WriteKatanaFile():
    """ Write a tree of PyXmlIO Elements to a Katana file. """
    pass
    
    

def WriteKatanaString():
    """ Write a tree of PyXmlIO Elements to a string. """
    pass
    
    

def contextmanager():
    """ @contextmanager decorator.
    
    Typical usage:
    
    @contextmanager
    def some_generator(<arguments>):
    <setup>
    try:
    yield <value>
    finally:
    <cleanup>
    
    This makes this:
    
    with some_generator(<arguments>) as <variable>:
    <body>
    
    equivalent to this:
    
    <setup>
    try:
    <variable> = <value>
    <body>
    finally:
    <cleanup>
    
    """
    pass
    
    
