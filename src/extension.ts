// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
		console.log('Congratulations, your extension "tornado-starter" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('extension.tornadoStarter', () => {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		let options: vscode.InputBoxOptions = {
			prompt?: "Please input the project name",
			placeHolder ?: "app-starter"
		}
		vscode.window.showInputBox(options).then(value => {
			if (!value) {
				let message = 'Project name is required';
				vscode.window.showInformationMessage(message);
				return
			}
			console.error('Input project name: ' + value);
		})
	});

	context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {}
