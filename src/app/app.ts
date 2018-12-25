export class appFactory {
    private fs = require('fs');
    constructor(name:string) {
        this.name = name;
    }
    createFile(){
        this.fs.writeFile("test_starter.txt", 'I am cool haha', function(err) {
            if (err) {
                console.error(err);
                return false;
            }
            console.log("File created success");
            return true;
        });
    }
}