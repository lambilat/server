const webdav = require('webdav-server').v2;
const express = require('express');

const server = new webdav.WebDAVServer();
const app = express();

server.rootFileSystem().addSubTree(server.createExternalContext(), {
    'folder1': {                                // /folder1
        'file1.txt': webdav.ResourceType.File,  // /folder1/file1.txt
        'file2.txt': webdav.ResourceType.File   // /folder1/file2.txt
    },
    'file0.txt': webdav.ResourceType.File       // /file0.txt
})
// Mount the WebDAVServer instance
app.use(webdav.extensions.express('/', server));
app.listen(3000);
