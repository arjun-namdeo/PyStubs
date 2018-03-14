
def CrashSave():
    """
    Forces a crash file to be saved.
    
    Katana automatically writes crash files based on user preferences. A crash
    file can be manually be written before potentially risky operations.
    
    @type forceSave: C{bool}
    @type logCompletion: C{bool}
    @param forceSave: Flag that controls whether to force a crash file save,
    even if the write is redundant.
    @param logCompletion: Flag that controls whether to log the result of
    trying to save the crash file.
    """
    pass
    
    

def CrashSaveDisable():
    """ None """
    pass
    
    

def CrashSaveEnable():
    """ None """
    pass
    
    

def CreateSceneAsset():
    """
    Creates a new asset to save the Katana file.
    
    The asset argument is usually a simple asset ID or the scene name. It can
    be a new or existing asset.
    
    @type asset: C{str}
    @type versionUp: C{bool}
    @type publish: C{bool}
    @type extraOptionsDict: C{dict}
    @rtype: C{str}
    @param asset: The basic base asset or base scene name.
    @param versionUp: Flag that controls whether to create a new version.
    @param publish: Flag that controls whether to publish the resulting scene
    as the current version.
    @param extraOptionsDict: args to pass down into createAssetAndPath
    @return: The full asset ID.
    """
    pass
    
    

def Export():
    """
    Exports the selected nodes in the node graph into a new Katana scene. If
    fileNameOrAssetId is an assetId then the scene will be published via the
    asset management system plugin (internally calling createAssetAndPath(),
    then save the file and finally calling postCreateAsset()).
    
    @type fileNameOrAssetId: C{str}
    @type nodes: C{list} of C{NodegraphAPI.Node}
    @type extraOptionsDict: C{dict}
    @rtype: C{str}
    @param fileNameOrAssetId: The name of the file or the ID of the asset under
    which to save the current scene.
    @param nodes: The list of nodes to export to the file or asset with the
    given name or ID.
    @param extraOptionsDict: A dictionary with extra options that will be passed
    to the createAssetAndPath() and postCreateAsset() functions as args.
    @return: The name of the saved project file, or the ID of the published
    project asset, or C{None} if the project could not be saved or
    published.
    @raise ValueError: If the given filename or asset ID is not valid.
    """
    pass
    
    

def GetCrashActions():
    """
    @rtype: C{int}
    @return: The number of actions since the last crash save.
    """
    pass
    
    

def GetCrashTime():
    """
    @rtype: C{float}
    @return: The seconds since the last crash save.
    """
    pass
    
    

def GetViableCrashFiles():
    """
    @type smartPrune: C{bool}
    @rtype: C{list}
    @param smartPrune: Flag that controls whether to skip empty files or old
    files that share a common prefix.
    @return: A list of dictionaries containing data for all crash save files
    that match the C{/TMPDIRp/*.katana} filename pattern.
    """
    pass
    
    

def Import():
    """
    Loads and merges a Katana file into the current one.
    
    @type fileName: C{str}
    @type floatNodes: C{bool}
    @rtype: C{list} of L{Node}
    @param fileName: The name of the file or the ID of the asset to import.
    @param floatNodes: Flag that controls whether to make nodes interactively
    moveable. If C{True} the new nodes will be set to a floating state in
    the node graph editor.
    @return: A list of all newly created nodes.
    @raise ValueError: If unable to read from the file.
    """
    pass
    
    

def IsFileDirty():
    """
    Determines if the file has been altered since the last load or save
    operation.
    
    @rtype: C{bool}
    @return: C{True} if the file has been modified, otherwise C{False}.
    """
    pass
    
    

def IsFileSavedAsAsset():
    """
    @rtype: C{bool}
    @return: C{True} if the current session is saved as an asset, C{False} if
    the session is saved to a file.
    """
    pass
    
    

def Load():
    """
    Replaces the current scene with a newly loaded one.
    The filename can either be a filename or an asset ID.
    
    This operation cannot be undone and clears the undo stack.
    
    @type fileName: C{str}
    @type isCrashFile: C{bool}
    @param fileName: filename or asset ID
    @param isCrashFile: Flag to indicate whether the file to load is a crash
    file.
    """
    pass
    
    

def New():
    """
    Replaces the current file with a new one.
    
    This operation cannot be undone and clears the undo stack.
    """
    pass
    
    

def Paste():
    """
    Creates new nodes that are encoded in XML.
    
    Katana uses XML to load, save, copy, and paste its nodes. The new nodes can
    be parented into any group.
    
    The C{nodeXML} argument can either be a string of XML data, a string from a
    Katana file, or an Katana XmlIO Element. Strings will attempt to be
    upgraded, but elements will not.
    
    @type nodeXML: C{str}
    @type parent: L{GroupNode}
    @param nodeXML: The string or element of nodes to paste.
    @param parent: The group node to set as the parent for the given node
    structure.
    """
    pass
    
    

def PopFileDirtyState():
    """ None """
    pass
    
    

def PostCreateSceneAsset():
    """
    Calls the postCreateAsset function of the currently loaded AssetAPI Plug-in
    
    The asset argument is usually a simple asset ID or the scene name. It can
    be a new or existing asset.
    
    @type asset: C{str}
    @type versionUp: C{bool}
    @type publish: C{bool}
    @type extraOptionsDict: C{dict}
    @rtype: C{str}
    @param asset: The basic base asset or base scene name.
    @param versionUp: Flag that controls whether to create a new version.
    @param publish: Flag that controls whether to publish the resulting scene
    as the current version.
    @param extraOptionsDict: args to pass down into postCreateAsset
    @return: The full asset ID.
    """
    pass
    
    

def PushFileDirtyState():
    """ None """
    pass
    
    

def RegisterPasteHandler():
    """
    Registers the given paste callback function.
    
    Paste handlers get the C{inputText}, and are expected to return a
    C{nodeList} if they can load it, or nothing otherwise.
    
    @type cb: C{callable}
    @param cb: The callback function to register as a paste handler.
    """
    pass
    
    

def Revert():
    """
    Reloads the current file from disk. This can only succeed if the current
    scene was loaded or saved to a file.
    
    This operation cannot be undone and clears the undo stack.
    
    @raise ValueError: If file not on disk.
    """
    pass
    
    

def Save():
    """
    Saves a Katana scene. If fileNameOrAssetId is an assetId then the scene will
    be published via the asset management system plugin (internally
    calling createAssetAndPath(), then save the file and finally calling
    postCreateAsset()).
    
    @type fileNameOrAssetId: C{str}
    @type extraOptionsDict: C{dict}
    @rtype: C{str}
    @param fileNameOrAssetId: The name of the file or the ID of the asset under
    which to save the current scene.
    @param extraOptionsDict: A dictionary with extra options that will be passed
    to the createAssetAndPath() and postCreateAsset() functions as args.
    @return: The name of the saved project file, or the ID of the published
    project asset, or C{None} if the project could not be saved or
    published.
    @raise ValueError: If the given filename or asset ID is not valid.
    """
    pass
    
    

def SetFileDirty():
    """
    Sets the Katana file to be dirty. Useful if you manipulate the node graph
    behind the undo system's back, yet still want to register that the file
    needs to be saved.
    """
    pass
    
    

def WasFileLoadedFromCrashFile():
    """
    @rtype: C{bool}
    @return: C{True} if the file was loaded from a crash file, otherwise
    C{False}.
    @attention: The user interface will not allow a regular save to overwrite a
    file that has been loaded this way. There is no restriction at the API
    level, but be aware.
    """
    pass
    
    

def WasFileVersionedOnLoad():
    """
    @rtype: C{bool}
    @return: C{True} if the file was run through the Katana versioning
    importers on load, otherwise C{False}.
    @attention: The user interface will not allow a regular save to overwrite a
    file that has been versioned. There is no restriction at the API level,
    but be aware.
    """
    pass
    
    
