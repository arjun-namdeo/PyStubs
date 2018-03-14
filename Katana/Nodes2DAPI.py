
def CancelRender():
    """  """
    pass
    
    

def CheckExternalRender():
    """  """
    pass
    
    

def CheckFileIns(fileIns):
    """ CheckFileIns(fileIns) -> statusLis
    Check a list of FileIns, releasing the GIL while processing.
    @param fileIns: a list of (fileInName, frameTime) tuples
    @return a list of (fileInName, errorMessage) tuples. """
    pass
    
    

def ClearDisplayWindowCache():
    """  """
    pass
    
    

def ClearImageHeaderCache():
    """  """
    pass
    
    

def ClearSpeculativeCacheContents():
    """ Clear the speculative Cache Contents """
    pass
    
    

def CreateExternalRenderListener():
    """  """
    pass
    
    

def EnumerateReadableImageFormats():
    """  """
    pass
    
    

def EnumerateWriteableImageFormats():
    """  """
    pass
    
    

def FinishRender():
    """  """
    pass
    
    

class FrameBuffer(object):
    """ Katana FrameBuffer Type """
    
    def getView(self):
        """  """
        pass
        
        
    
    def glTexSubImage2D(self):
        """  """
        pass
        
        
    
    def setSequenceID(self):
        """  """
        pass
        
        
    
    def getBackgroundRegion(self):
        """  """
        pass
        
        
    
    def writeToDisk(self):
        """  """
        pass
        
        
    
    def getSize(self):
        """  """
        pass
        
        
    
    def getThumbnailHeight(self):
        """  """
        pass
        
        
    
    def getDataWindow(self):
        """  """
        pass
        
        
    
    def getBackgroundColor(self):
        """  """
        pass
        
        
    
    def getSampleRate(self):
        """  """
        pass
        
        
    
    def queryRegionStats(self):
        """  """
        pass
        
        
    
    def queryScanline(self):
        """  """
        pass
        
        
    
    def getSequenceID(self):
        """  """
        pass
        
        
    
    def duplicate(self):
        """  """
        pass
        
        
    
    def queryHistogram(self):
        """  """
        pass
        
        
    
    def getFrameTime(self):
        """  """
        pass
        
        
    
    def getNodeName(self):
        """  """
        pass
        
        
    
    def setView(self):
        """  """
        pass
        
        
    
    def getThumbnailData(self):
        """  """
        pass
        
        
    
    def getDataRegion(self):
        """  """
        pass
        
        
    
    def getNativeDataWindow(self):
        """  """
        pass
        
        
    
    def copyImageData(self):
        """  """
        pass
        
        
    
    def getDataRegionOutline(self):
        """  """
        pass
        
        
    
    def getChannels(self):
        """  """
        pass
        
        
    
    def getDisplayWindow(self):
        """  """
        pass
        
        
    
    def getThumbnailWidth(self):
        """  """
        pass
        
        
    
    def isRender3D(self):
        """  """
        pass
        
        

def GetAllRenderTypes():
    """  """
    pass
    
    

def GetDisplayWindow(inputPort, time):
    """ GetDisplayWindow(inputPort, time) -> (x0, y0, x1, y1)
    """
    pass
    
    

def GetErrorMessages():
    """ None """
    pass
    
    

def GetExternalRenderListenerInfo():
    """  """
    pass
    
    

def GetFileOutAssetId():
    """  """
    pass
    
    

def GetFileOutColorspace():
    """  """
    pass
    
    

def GetFileOutEnabled():
    """  """
    pass
    
    

def GetFileOutFilename():
    """  """
    pass
    
    

def GetFileOutFormat():
    """  """
    pass
    
    

def GetFileOutOutputParams():
    """  """
    pass
    
    

def GetFileOutPassName():
    """  """
    pass
    
    

def GetFileOutPostScriptInfo():
    """  """
    pass
    
    

def GetFileOutPostScriptParams():
    """  """
    pass
    
    

def GetFileOutProxyOnCue():
    """  """
    pass
    
    

def GetFileOutRepPrefix():
    """  """
    pass
    
    

def GetFileOutRepresentation():
    """  """
    pass
    
    

def GetFileOutResolutionName():
    """  """
    pass
    
    

def GetFilmWidthFromString():
    """  """
    pass
    
    

def GetFrameBufferCancelledMessages():
    """  """
    pass
    
    

def GetFrameBufferCompletedMessages():
    """  """
    pass
    
    

def GetFrameBufferRectUpdateMessages():
    """  """
    pass
    
    

def GetImageDescription():
    """  """
    pass
    
    

def GetImageReadPath(node):
    """ GetFileInPath(node) -> str
    Get the resolved path for the given FileIn at the given render time. """
    pass
    
    

def GetIncrementedRenderSequenceID():
    """  """
    pass
    
    

def GetMaxDiskUsage():
    """  """
    pass
    
    

def GetMaxImageMemory():
    """  """
    pass
    
    

def GetNameOfNodeBeingAnalysed():
    """  """
    pass
    
    

def GetNewFrameBuffers():
    """  """
    pass
    
    

def GetNewRenders():
    """ None """
    pass
    
    

def GetNumberParameterSetValueMessages():
    """  """
    pass
    
    

def GetOutputDisplayWindow(outputPort, time):
    """ GetOutputDisplayWindow(outputPort, time) -> (x0, y0, x1, y1)
    """
    pass
    
    

def GetPixelScriptCode():
    """  """
    pass
    
    

def GetRenderMessages():
    """ None """
    pass
    
    

def GetRenderProgressMessages():
    """  """
    pass
    
    

def GetRenderThreads():
    """  """
    pass
    
    

def GetSpeculativeCacheContents():
    """ Return an xml element containing the speculative cache contents """
    pass
    
    

def GetSpeculativeCacheEnabled():
    """  """
    pass
    
    

def GetTileRenderOrderMessages():
    """  """
    pass
    
    

def GetTileSize():
    """  """
    pass
    
    

def GetTransformBetweenNodes():
    """  """
    pass
    
    

def GetTransformForInputPort():
    """  """
    pass
    
    

def GetViewBasedPrioritization():
    """ None """
    pass
    
    

class IntImage(object):
    """ Katana Integer Image Type """
    
    def imageData(self):
        """  """
        pass
        
        
    
    def height(self):
        """  """
        pass
        
        
    
    def channels(self):
        """  """
        pass
        
        
    
    def width(self):
        """  """
        pass
        
        

def IsExternalRenderInProgress():
    """  """
    pass
    
    

def IsRenderInProgress():
    """  """
    pass
    
    

def IsThumbnailRendering():
    """  """
    pass
    
    

def IsUpstreamNode2D():
    """ None """
    pass
    
    

def KillExternalRender():
    """  """
    pass
    
    

class Node2D(Node):
    """ Katana Node2D Type """

def PrintImageMemoryUsage():
    """  """
    pass
    
    

def ProcessMainThreadProcessorTimeSlice():
    """  """
    pass
    
    

def ReadImage():
    """  """
    pass
    
    

def ReadImageThreaded():
    """  """
    pass
    
    

def RegisterCommandLineNode():
    """ None """
    pass
    
    

def RegisterNewRender():
    """ None """
    pass
    
    

def Render():
    """  """
    pass
    
    

def RenderThumbnail():
    """  """
    pass
    
    

def Render_Buffer():
    """ None """
    pass
    
    

def ReportRenderMessage():
    """ None """
    pass
    
    

def SetMaxDiskUsage():
    """  """
    pass
    
    

def SetMaxImageMemory():
    """  """
    pass
    
    

def SetPrioritizerCenter():
    """ None """
    pass
    
    

def SetPrioritizerWindow():
    """ None """
    pass
    
    

def SetRenderDebug():
    """  """
    pass
    
    

def SetRenderLogFile():
    """  """
    pass
    
    

def SetRenderPrioritizer():
    """  """
    pass
    
    

def SetRenderThreads():
    """  """
    pass
    
    

def SetSpeculativeCacheEnabled():
    """  """
    pass
    
    

def SetTileSize():
    """  """
    pass
    
    

def SetViewBasedPrioritization():
    """ None """
    pass
    
    

def Set_GetRenderProducer_Fn():
    """ None """
    pass
    
    

def SignalExternalRender():
    """  """
    pass
    
    

def StartAnalysis():
    """  """
    pass
    
    

def StartExternalRender(sequenceID, nodeName, preCommands, renderCmd, postCommands, appPackage, appVersion, appPath):
    """ StartExternalRender(sequenceID, nodeName, preCommands, renderCmd, postCommands, appPackage, appVersion, appPath) -> (errorCode, "", errorMessage)
    @return a triple of (errorCode, , errorMessage),
    where errorCode is 0 and errorMessage empty on success,
    and errorCode is -1 and errorMessage a string on failure. """
    pass
    
    

def StopAnalysis():
    """  """
    pass
    
    

def TileStitch():
    """  """
    pass
    
    

def fbo_bind():
    """ no docs """
    pass
    
    

def fbo_create():
    """ no docs """
    pass
    
    

def fbo_delete():
    """ no docs """
    pass
    
    

def fbo_init():
    """ no docs """
    pass
    
    

def fbo_unbind():
    """ no docs """
    pass
    
    

def glBatchVertex(vertexSequence):
    """ glBatchVertex(vertexSequence) -> None
    @param vertexSequence: a sequence of float tuples
    tuples may be of size 2, 3, or 4 """
    pass
    
    

def glDrawProjectedLatLongLine():
    """ no docs """
    pass
    
    

def gl_disableFragmentProgram():
    """ no docs """
    pass
    
    

def gl_enableFilmlookFragmentProgram():
    """ no docs """
    pass
    
    

def gl_enableFragmentProgram():
    """ no docs """
    pass
    
    

def stabilize_GetStabilizeMultiTransform(parentParam, times, overrideMode=None):
    """ GetStabilizeMultiTransform(parentParam, times, overrideMode=None) -> transforms
    @param parentParam: the parent under which to find the stabilization parameters (notably, 'points' should be a child of this parameter)
    @param times: a list of times at which to calculate the transforms
    @param overrideMode: if specified, use it instead of querying the mode parameter
    @return a list of transforms correlating to the given times """
    pass
    
    
