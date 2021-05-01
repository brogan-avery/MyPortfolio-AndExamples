/**************************************************************
* File Title: Dev Tool 3 Class Body
* Author: Brogan Avery
* Created : 2021-0401
* File Description : Features a tool to let user manage different parts of a product documentation, organization, and time management
***************************************************************/

#include "DevTool3.hpp"

DevTool3::DevTool3(){} ///constructor

/// simple main menu navigation function
void DevTool3::menu3(){
    string userInput = " ";
    cout << "\n* Project Management * " << endl;
    
    while (userInput != "3") {
        cout << "  Select number " << endl;
        cout << "     1. Generate Project Management Guide For New Project" << endl;
        cout << "     2. View Your Project Guides" << endl;
        cout << "     3. Return To Developer Tools Dashboard" << endl;

        cout << "  Enter Selection: " << endl;
        
        getline(cin, userInput);

        if (userInput == "1"){
            startNewProject();
        }
        
        if (userInput == "2"){
            viewProjectGuide();
        }
    }
    cout << "Going back to Dashboard..." << endl;
}

/// creates a new project object and then stores the data from used in various file forms to handle the formate and length (also to make it more editable directly from text docs if wanted)
void DevTool3::startNewProject(){
    string userInput = " ";
    Project newProject;
    
    /// get title
    cout << "Enter a Title for project:" << endl;
    getline(cin,userInput);
    newProject.setTitle(userInput);
    userInput = " ";
    
    /// get customer goals one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Goal to add to the Customer Goals for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToCustomerGoals(userInput);
        }
        createFile(newProject.getTitle()+"CustomerGoals.txt");
        for (int i = 0; i < newProject.getCustomerGoals().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"CustomerGoals.txt", newProject.getCustomerGoals()[i]);
        }
    }
    userInput = " ";
    
    /// get user goals one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Goal to add to the User Goals for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToUserGoals(userInput);
        }
        createFile(newProject.getTitle()+"UserGoals.txt");
        for (int i = 0; i < newProject.getUserGoals().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"UserGoals.txt", newProject.getUserGoals()[i]);
        }
    }
    userInput = " ";
    
    /// get proposal and store it to a file
    while (userInput != "c") {
        cout << "Enter a Proposal for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setProposal(userInput);
        }
        createFile(newProject.getTitle()+"Proposal.txt");
        appendLineToEOF(newProject.getTitle()+"Proposal.txt", newProject.getProposal());
        userInput = " ";
        break;
    }
    
    /// get detailed description and store it to a file
    while (userInput != "c") {
        cout << "Enter a Detailed Description for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setDetailedDescription(userInput);
        }
        createFile(newProject.getTitle()+"DetailedDescription.txt");
        appendLineToEOF(newProject.getTitle()+"DetailedDescription.txt", newProject.getDetailedDescription());
        userInput = " ";
        break;
    }
    
    /// get outline and store it to a file
    while (userInput != "c") {
        cout << "Enter the General Outline or parts for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setOutline(userInput);
        }
        createFile(newProject.getTitle()+"Outline.txt");
        appendLineToEOF(newProject.getTitle()+"Outline.txt", newProject.getOutline());
        userInput = " ";
        break;
    }
   
    /// get pseudocode and store it to a file
    while (userInput != "c") {
        cout << "Enter the Pseudocode for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setPseudocode(userInput);
        }
        createFile(newProject.getTitle()+"Pseudocode.txt");
        appendLineToEOF(newProject.getTitle()+"Pseudocode.txt", newProject.getPseudocode());
        userInput = " ";
        break;
    }
    
    /// get wireframe and store it to a file
    while (userInput != "c") {
        cout << "Enter the Wireframe for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setWireframe(userInput);
        }
        createFile(newProject.getTitle()+"Wireframe.txt");
        appendLineToEOF(newProject.getTitle()+"Wireframe.txt", newProject.getWireframe());
        userInput = " ";
        break;
    }
    
    /// get file names to add to the back log one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a File Name to add to the Files for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToFiles(userInput);
        }
        createFile(newProject.getTitle()+"Files.txt");
        for (int i = 0; i < newProject.getFiles().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"Files.txt", newProject.getFiles()[i]);
        }
    }
    userInput = " ";
    
    /// get reports to add to the reports one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Report to add to the Progress Reports for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToProgressReports(userInput);
        }
        createFile(newProject.getTitle()+"ProgressReports.txt");
        for (int i = 0; i < newProject.getProgressReports().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"ProgressReports.txt", newProject.getProgressReports()[i]);
        }
    }
    userInput = " ";
    
    /// get dates to add to the dead lines one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Dead Line to add to the Dead Lines for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.addToDeadLines(userInput);
        }
        
        createFile(newProject.getTitle()+"DeadLines.txt");
        for (int i = 0; i < newProject.getDeadLines().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"DeadLines.txt", newProject.getDeadLines()[i]);
        }
    }
    userInput = " ";
    
    /// get tasks to add to the back log one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Task to add to the Back Log for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToBackLog(userInput);
        }
        createFile(newProject.getTitle()+"BackLog.txt");
        for (int i = 0; i < newProject.getBackLog().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"BackLog.txt", newProject.getBackLog()[i]);
        }
    }
    userInput = " ";
    
    /// get item to add to the time log one by one and stores to a vector, then stores it to a file
    while (userInput != "c") {
        cout << "Enter a Item to add to the Time Log for project or 'c' to continue:" << endl;
        getline(cin,userInput);
        
        if (userInput != "c"){
            newProject.addToTimeLog(userInput);
        }
        createFile(newProject.getTitle()+"TimeLog.txt");
        for (int i = 0; i < newProject.getTimeLog().size() ; i++){
            appendLineToEOF(newProject.getTitle()+"TimeLog.txt", newProject.getTimeLog()[i]);
        }
    }
    userInput = " ";
    
    /// get user manual and store it to a file
    while (userInput != "c") {
        cout << "Enter the User Manual for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setUserManual(userInput);
        }
        createFile(newProject.getTitle()+"UserManual.txt");
        appendLineToEOF(newProject.getTitle()+"UserManual.txt", newProject.getUserManual());
        
        userInput = " ";
        break;
    }
    
    /// get product documentation and store it to a file
    while (userInput != "c") {
        cout << "Enter the Product Documentation for project or 'c' to leave blank for now:" << endl;
        getline(cin,userInput);
        if (userInput != "c"){
            newProject.setProductDocumentation(userInput);
        }
        createFile(newProject.getTitle()+"ProductDocumentation.txt");
        appendLineToEOF(newProject.getTitle()+"ProductDocumentation.txt", newProject.getProductDocumentation());
        userInput = " ";
        break;
    }
    
    /// adds the new project title to a file that is a list of all the project titles that the user has created
    appendLineToEOF("projectObjects.txt", newProject.getTitle());
    
    cout << "New Project Created.\n" << endl;
}

/// function that lets user select which product management guide they want to view
void DevTool3::viewProjectGuide(){
    string userInput = " ";
    string continueAfterWarning = " ";
    vector<string> projectTitles = readFile("projectObjects.txt");
    
    ///displays project names from the file of project names for the user to select from
    cout << "\n* Select Project To View Guide For * " << endl;
    while (userInput != "0") {
        cout << "Enter the number associated with the project you want to view the guide for or 0 to return to the previous screen: " << endl;
        cout << "  Select number " << endl;
        cout << "     0. Return To Previous Screen" << endl;
        for (int i = 0; i < projectTitles.size() ; i++){
            cout << "     " << i+1 << ". " << projectTitles[i] << endl;
        }

        cout << "  Enter Selection: " << endl;
        
        getline(cin, userInput);
        
        /// because there is now way to return this is labeled as a beta feature
        continueAfterWarning = " ";
        while (continueAfterWarning != "N") {
        if (continueAfterWarning != "N"){
            cout << "*** WARNING *** \nThis feature is still in Beta Testing. Continuing will require you to restart this program to use any other features. \n Do you wish to continue? (Y/N)" << endl;
            continueAfterWarning = " ";
            
            getline(cin, continueAfterWarning);
        }
           continueAfterWarning = capitalizeWord(continueAfterWarning);
            if (continueAfterWarning == "Y"){
        
        /// gets the name of the project that the user selected
        string projectTitle = projectTitles[stoi(userInput)-1];
        
// the following code reads and formats the text from each of the files associated with the project the user selected to be displayed in HTML on a webpage
        /// read customer goals file and stores each line to a vector
        vector<string> customerGoalsVector = readFile(projectTitle + "CustomerGoals.txt");
        
        /// read user goals file and stores each line to a vector
        vector<string> userGoalsVector = readFile(projectTitle + "UserGoals.txt");
        
        /// read proposal text and store in a string
        string proposalStr = "";
        vector<string> proposalVector = readFile(projectTitle + "Proposal.txt");
        for (auto line : proposalVector){
            proposalStr = proposalStr + line + "<br>";
        }
        
        /// read detailed description text and store in a string
        string detailedDescriptionStr = "";
        vector<string> detailedDescriptionVector = readFile(projectTitle + "DetailedDescription.txt");
        for (auto line : detailedDescriptionVector){
            detailedDescriptionStr = detailedDescriptionStr + line + "<br>";
        }
        
        /// read outline text and store in a string
        string outlineStr = "<pre>"; /// pre is used to preserve the formatting and spacing of the text file
        vector<string> outlineVector = readFile(projectTitle + "Outline.txt");
        for (auto line : outlineVector){
            outlineStr = outlineStr + line + "<br>";
        }
        outlineStr = outlineStr + "</pre>";
        
        /// read pseudocode text and store in a string
        string pseudocodeStr = "<pre>";
        vector<string> pseudocodeVector = readFile(projectTitle + "Pseudocode.txt");
        for (auto line : pseudocodeVector){
            pseudocodeStr = pseudocodeStr + line + "<br>";
        }
        pseudocodeStr = pseudocodeStr + "</pre>";
        
        /// read wireframe text and store in a string
        string wireframeStr = "";
        vector<string> wireframeVector = readFile(projectTitle + "Wireframe.txt");
        for (auto line : wireframeVector){
            wireframeStr = wireframeStr + line + "<br>";
        }
        
        /// read files file and stores each line to a vector
        vector<string> filesVector = readFile(projectTitle + "Files.txt");
        
        /// read progress reports file and stores each line to a vector
        vector<string> progressReportsVector = readFile(projectTitle + "ProgressReports.txt");
        
        /// read deadlines file and stores each line to a vector
        vector<string> deadLinesVector = readFile(projectTitle + "DeadLines.txt");
        
        /// read back log file and stores each line to a vector
        vector<string> backLogVector = readFile(projectTitle + "BackLog.txt");
        
        /// read time log file and stores each line to a vector
        vector<string> timeLogVector = readFile(projectTitle + "TimeLog.txt");
        
        /// read user manual text and store in a string
        string userManualStr = "";
        vector<string> userManualVector = readFile(projectTitle + "UserManual.txt");
        for (auto line : userManualVector){
            userManualStr = userManualStr + line + "<br>";
        }
        
        /// read product documentation text and store in a string
        string productDocumentationStr = "";
        vector<string> productDocumentationVector = readFile(projectTitle + "ProductDocumentation.txt");
        for (auto line : productDocumentationVector){
            productDocumentationStr = productDocumentationStr + line + "<br>";
        }
        
        /// creates a temporary project object to hold all of the information just read in from the files
        Project projectToView;
        projectToView.setTitle(projectTitle);
        projectToView.setCustomerGoals(customerGoalsVector);
        projectToView.setUserGoals(userGoalsVector);
        projectToView.setProposal(proposalStr);
        projectToView.setDetailedDescription(detailedDescriptionStr);
        projectToView.setOutline(outlineStr);
        projectToView.setPseudocode(pseudocodeStr);
        projectToView.setWireframe(wireframeStr);
        projectToView.setFiles(filesVector);
        projectToView.setProgressReports(progressReportsVector);
        projectToView.setDeadLines(deadLinesVector);
        projectToView.setBackLog(backLogVector);
        projectToView.setTimeLog(timeLogVector);
        projectToView.setUserManual(userManualStr);
        projectToView.setProductDocumentation(productDocumentationStr);
        
        /// calls function to get the rest of the text to make a webpage that can be displayed with the info just gathered
        stringifyHtml(projectToView);
            }
        }
    }
    cout << "Returning to previous screen..." << endl;
}

/// function that takes the attributes of a project object as text and combines it with text from an HTML template to create a project management guide on a webpage
stringstream body;
void DevTool3::stringifyHtml(Project projectToView){
    vector<string> lines = readFile("ProjectManagementGuide.html"); ///HTML template like file
  
//  the following operations display text or CSS on a webpage with a server call
    /// add lines of file for the header
    for (int i = 0; i < lines.size(); i++){
        body << lines[i];
        
// after each label from the HTML file, it writes the text from the project object
        /// display Title
        if ( i == 14){
            body << projectToView.getTitle();
        }
        
        /// display Customer Goals in an ordered list
        if ( i == 16){
            body << "<ol>";
            for (auto line : projectToView.getCustomerGoals()){
                body << "<li>" + line + "</li>";
            }
            body << "</ol>";
        }
        
        /// display User Goals in an ordered list
        if ( i == 17){
            body << "<ol>";
            for (auto line : projectToView.getUserGoals()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display Proposal
        if ( i == 18){
            body << projectToView.getProposal();
        }
        
        /// display Detailed Description
        if ( i == 19){
            body << projectToView.getDetailedDescription();
        }
        
        /// display Outline
        if ( i == 20){
            body << projectToView.getOutline();
        }
        
        /// display Pseudocode
        if ( i == 21){
            body << projectToView.getPseudocode();
        }
        
        /// display Wireframe
        if ( i == 22){
            body << projectToView.getWireframe();
        }
        
        /// display Project File Names (and desc.)  in an ordered list
        if ( i == 23){
            body << "<ol>";
            for (auto line : projectToView.getFiles()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display Progress Reports in an ordered list
        if ( i == 24){
            body << "<ol>";
            for (auto line : projectToView.getProgressReports()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display deadlines in an ordered list
        if ( i == 25){
            body << "<ol>";
            for (auto line : projectToView.getDeadLines()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display Back Log Tasks in an ordered list
        if ( i == 26){
            body << "<ol>";
            for (auto line : projectToView.getBackLog()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display Time Log Items in an ordered list
        if ( i == 27){
            body << "<ol>";
            for (auto line : projectToView.getTimeLog()){
                body << "<li>";
                body << line;
                body << "</li>";
            }
            body << "</ol>";
        }
        
        /// display User Manual
        if ( i == 28){
            body << projectToView.getUserManual();
        }
        
        /// display Product Documentation
        if ( i == 29){
            body << projectToView.getProductDocumentation();
        }
    }
    
    /// starts a server and displays all of the body string text that was just smooshed together from the HTML file and the project object's attributes
    cout << "Starting Server" << endl;
    system("open http://localhost:8080/"); /// opens to the page where the sever directed to
    httplib::Server svr;
    svr.Get("/", [](const httplib::Request & /*req*/, httplib::Response &res) {
        res.set_content(body.str(), "text/html");
    });
    svr.listen("localhost", 8080);
    
}
