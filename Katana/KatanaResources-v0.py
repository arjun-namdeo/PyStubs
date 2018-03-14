
def DefaultResourcePath():
    """ Return the path used for internal default resources.  Default resources
    can be overridden by resources in $KATANA_RESOURCES directories. """
    pass
    
    

def GetIconPath():
    """ Find a named image in the icon path directories.
    The "Icons" subdirectory is looked for on each shot path.
    Return None if the image is not found.
    
    @param name: image file name, possibly with subdirs
    @type name: C{str}
    @return: image filename
    @rtype: C{str} or C{None}
    """
    pass
    
    

def GetResourceFile():
    """ Find a Katana resource file.
    This should be used by Katana internally to ensure it gets a
    resource that it needs. It raises exception if it cannot find
    the file. This only searches in the internal Katana resource
    directories. The files cannot be overridden externally.
    
    @type resourceName: C{str}
    @raise AttributeError: Resource not found.
    """
    pass
    
    

def GetSearchPaths():
    """ Get default search paths.
    Get a new list of all the search paths. If the subdir argument
    is given, it will be added on to each path.
    
    @param subdir: optional subdirectory name to append
    @type subdir: C{str}
    @rtype: C{list} of C{str}
    """
    pass
    
    

def GetUserKatanaPath():
    """ Get the path to the users Katana directory.
    This will ensure that the directory actually exists
    before returning. If the subdir argument is given, it will
    be added to the path (and also ensured to exist).
    
    @param subdir: optional subdirectory name to append
    @type subdir: C{str}
    @rtype: C{str}
    @raise OSError: failed to create user directory.
    """
    pass
    
    

def Initialize():
    """ Call at startup time to initialize resource searching. """
    pass
    
    

def InternalResourcePath():
    """ Return the path used for internal resources. """
    pass
    
    
