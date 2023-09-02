function sendEmailByForm(e) 
{
  // Set up email parameters
  var email = "EMAILADDRESS"; // Replace with your feedback email address
  
  // Create email heading
  var subject = "Send Email by Form Test";
  
  // Get response data
  var frm = FormApp.getActiveForm().getItems();
  var rsc = e.response.getResponseForItem(frm[0]).getResponse();
  var responseOne = e.response.getResponseForItem(frm[1]).getResponse();

  var submitter = Session.getActiveUser().getEmail();

  //Logger.log(e.response);
  Logger.log("resource: " + rsc + " reason: " + "resource: " + responseOne);

  //var body = "Here is the body of the Send Email by Form Test:\n\n";
  var body = "Submitted by: " + rsc 
  + "\n\n Response 1: " + responseOne;
  
  // Send email
  MailApp.sendEmail(email, subject, body);
}