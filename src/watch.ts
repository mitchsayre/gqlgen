const chokidar = require('chokidar');

function setUpWatcher(directory, runCodegen, documents) {
    let initialScanComplete = false;
    console.log(documents)

    // Initialize file watcher
    const watcher = chokidar.watch(directory, {
        ignored: /(^|[\/\\])\../, // ignore dotfiles
        persistent: true
    });

    watcher
        .on('add', path => {
            if (initialScanComplete) {
                runCodegen(path, 'added');
            }
        })
        .on('change', path => runCodegen(path, 'changed'))
        .on('unlink', path => runCodegen(path, 'removed'))
        .on('ready', () => {
            initialScanComplete = true; // Set the flag to true when the initial scan is complete
        });
}

function runCodegen(path, action) {
    console.log(`${path} has been ${action}`);
}

module.exports = {
    plugin: (schema, documents, config) => {
        setUpWatcher(documents.location, runCodegen, documents);
        return {};
    }
};
