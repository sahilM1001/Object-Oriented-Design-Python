class Notepad:
    def __init__(self,text) -> None:
        self.allContent = []
        self.allContent = text.split("\n")
        self.undoStack  = []
        self.redoStack = []
        self.clipBoard = []
    
    def display(self):
        for i in self.allContent:
            print(i)
    
    def display(self,startLine, endLine=None):
        if startLine > len(self.allContent):
            print("Start line greater than content")
        elif  endLine != None and endLine > len(self.allContent):
            print("End line greater than content")
        elif endLine != None and startLine > endLine:
            print("Start line cannot be greater than end line")
        else:
            if endLine == None:
                endLine = len(self.allContent)
            for i in range(startLine, endLine):
                print(self.allContent[i])
    def insert(self, line, text):
        self.undoStack.append(self.allContent)
        if line > len(self.allContent):
            self.allContent.append(line)
        else:
            self.allContent.insert(line,text)
    def delete(self, startLine, endLine):
        if startLine > len(self.allContent):
            print("Line not present in content")
        elif endLine != None and endLine > len(self.allContent):
            print("End line greater than content")
        elif endLine != None and startLine > endLine:
            print("Start line cannot be greater than end line")
        else:
            self.undoStack.append(self.allContent)
            if endLine == None:
                del self.allContent[startLine]
            else:
                del self.allContent[startLine:endLine]
    
    def copy(self, startLine, endLine):
        if startLine > len(self.allContent):
            print("Line not present in content")
        elif endLine != None and endLine > len(self.allContent) :
            print("End line greater than content")
        elif endLine != None and startLine > endLine:
            print("Start line cannot be greater than end line")
        else:
            if endLine == None:
                self.clipBoard = self.allContent[startLine]
            else:
                self.clipBoard = self.allContent[startLine:endLine]

    def paste(self, startLine):
        if startLine > len(self.allContent):
            print("Line not present in content")
        else:
            self.undoStack.append(self.allContent)
            self.allContent.insert(startLine, self.clipBoard)
    
    def undo(self):
        if len(self.undoStack) == 0:
            print("Nothing to undo")
        else:
            self.redoStack.append(self.allContent)
            self.allContent = self.undoStack.pop()

    def redo(self):
        if len(self.redoStack) == 0:
            print("Nothing to redo")
        else:
            self.undoStack.append(self.content)
            self.allContent = self.redoStack.pop()

            
            
            

