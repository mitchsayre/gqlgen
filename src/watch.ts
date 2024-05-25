import chokidar from 'chokidar';

interface Documents{
    location: string;
    [key:string]: any;
}

type RunCodegen = (path: string, action: 'added' | 'changed' |'removed') => void;
function setUpWatcher(directory:string, runCodegen:RunCodegen, documents:Documents) {
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

function runCodegen(path: string, action: 'added' | 'changed' | 'removed') {
    console.log(`${path} has been ${action}`);
}


export const plugin = (schema: any, documents: Documents, config: any) => {
    setUpWatcher(documents.location, runCodegen, documents);
    return {};
};
