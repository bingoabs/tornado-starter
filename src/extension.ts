// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as path from 'path';
import { AppFactory } from './app/app';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "tornado-starter" is now active!');
	console.log('workspace');
	console.log(vscode.workspace.workspaceFolders);
	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('extension.tornadoStarter', () => {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		let options: vscode.InputBoxOptions = {
			prompt: "Please input the project name",
			placeHolder: "app-starter"
		};
		vscode.window.showInputBox(options).then(value => {
			if (!value) {
				let message = 'Project name is required';
				vscode.window.showErrorMessage(message);
				return;
			}
			let fullPath = __dirname;
			let filename = path.basename(fullPath);
			console.log('The full path: ' + fullPath);
			console.log('The file name: ' + filename);
			console.log('Input project name: ' + value);
			let app = new AppFactory(value);
			app.createFile();
		});
	});

	context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {}
