# makes UFOs in the same folder as selected OTFs/TTFs

from fbits.toolbox.file import File
import os

appendText = '_CONVERTED'

paths = File.collect(extensionInclude=['.ttf', '.otf'])


for path in paths:
    print path
    f = OpenFont(path, showUI=False)
    fileBase, fileExt = os.path.splitext(path)
    ufoPath = fileBase + appendText + '.ufo'
    f.save(ufoPath)
    f.close()

print 'done'