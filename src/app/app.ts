export class AppFactory {
    private ncp = require('ncp').ncp;
    appPath: string;
    constructor(appPath: string) {
        this.appPath = appPath;
    }
    createApp(){
        this.ncp.limit = 16;
        let result = this.ncp("./tornado-starter/src/templates", this.appPath, function(err) {
            if (err){
                console.error(err);
            }
            console.log("Create project success");
        });
        return result;
    }
}