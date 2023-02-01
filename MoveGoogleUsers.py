function moveUsersToNewOU() {
  // Replace NEW_OU_ID with the ID of the new OU you want to move the users to
  var newOUId = 'NEW_OU_ID';

  // Replace USER_EMAIL_1, USER_EMAIL_2, ... with the email addresses of the users you want to move
  var userEmails = ['USER_EMAIL_1', 'USER_EMAIL_2', ...];

  // Get the Admin Directory API service
  var service = AdminDirectory.Users.list({
    customer: 'my_customer',
    maxResults: 500
  });

  // Loop through each user
  var users = service.users;
  for (var i = 0; i < users.length; i++) {
    var user = users[i];

    // Check if the user's email is in the list of user emails to move
    if (userEmails.indexOf(user.primaryEmail) > -1) {
      // Get the current parent OU of the user
      var oldOUId = user.orgUnitPath.split('/')[1];

      // Move the user to the new OU
      user.orgUnitPath = '/' + newOUId;
      AdminDirectory.Users.update(user, user.primaryEmail);

      // Print a success message
      Logger.log('Successfully moved user ' + user.primaryEmail + ' from ' + oldOUId + ' to ' + newOUId);
    }
  }
}
