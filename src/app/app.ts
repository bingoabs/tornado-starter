export class AppFactory {
    private fs = require('fs');
    name: string;
    constructor(name: string) {
        this.name = name;
    }
    createFile(){
        this.fs.writeFile("/Users/bingokarl/test_starter.txt", 'I am cool haha', function(err) {
            if (err) {
                console.error(err);
                return false;
            }
            console.log("File created success");
            return true;
        });
    }
}