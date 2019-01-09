export class AppFactory {
    private ncp = require('ncp').ncp;
    appPath: string;
    constructor(appPath: string) {
        this.appPath = appPath;
    }
    createApp(){
        this.ncp.limit = 16;
        //  TODO: make the static file packaged into the release
        let template_path = "/Users/bingokarl/project/tornado-starter/src/templates";
        let result = this.ncp(template_path, this.appPath, function(err: any) {
            if (err){
                console.error(err);
            }
            console.log("Create project success");
        });
        return result;
    }
}