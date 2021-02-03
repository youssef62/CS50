document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector("#compose-form").onsubmit = send_email ; 
  
  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block'; 
  document.querySelector("#email-view").style.display = 'none'; 
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

}


function prepare_reply(email){
  recipients = document.querySelector('#compose-recipients') ; 
  
  recipients.value = email.sender;
  recipients.disabled = true ; 
  subject = document.querySelector('#compose-subject');
  subject.value = "Re : " + email.subject;
  subject.disabled = true ; 
  body = document.querySelector('#compose-body') ; 

  header = "On " + email.timestamp + " " + email.sender + " wrote: \n " + email.body  +"\n";    
  body.value = header ; 
  body.disable = true ; 

}
function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  document.querySelector("#email-view").style.display = 'none'; 
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  archive_button = document.querySelector("#archive_email") ; 
  console.log(mailbox) ; 
  if (mailbox=="inbox"){
    archive_button.style.display = 'inline';
    archive_button.innerHTML = "Archive";  
  }else if (mailbox=="sent"){

    archive_button.style.display = 'none'; 
  }else if (mailbox=="archive"){

    archive_button.style.display = 'inline'; 
    archive_button.innerHTML = "Unarchive" ; 
  }

  fetch('/emails/' + mailbox ) 
    .then(response => response.json())
    .then(emails => {
      show_emails(emails , document.querySelector("#emails-view"));  
    }); 
}

function archive (email){
  fetch('/emails/' + email.id, {
    method: 'PUT',
    body: JSON.stringify({
      archived: !email.archived
    })
  }).then(()=>{

    load_mailbox("inbox"); 
  }) ; 
}



function mark_as_read(email){
  fetch("/emails/" + email.id  ,{
    method : 'PUT' , 
    body : JSON.stringify({
      read : true  
    })
  }) ;  
}
function load_email(email_id){
  
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector("#email-view").style.display = 'block' ;

  fetch('/emails/' + email_id.toString() )
    .then(response => response.json())
    .then(email => {

      mark_as_read(email); 
      document.querySelector("#sender").innerHTML = email.sender ; 
      document.querySelector("#recipient").innerHTML = email.recipients ; 
      document.querySelector("#time").innerHTML = email.timestamp ; 
      document.querySelector("#subject").innerHTML = email.subject ; 
      document.querySelector("#body").innerHTML = email.body ; 
      document.querySelector("#reply").onclick = () =>{
        compose_email() ; 
        prepare_reply(email) ; 
      }; 
      
      
      document.querySelector("#archive_email").onclick = ()=>{
          archive(email) ; 
      }; 

    });

} 

function show_emails(emails,container){

    for ( i in emails ){
      
      
      li = document.createElement("div") ; 
      li.className = "email" ; 
      
      sender = document.createElement("h4") ; 
      sender.innerHTML = emails[i].sender ; 

      subject = document.createElement("div") ;
      subject.innerHTML = emails[i].subject ; 
      subject.className = "subject" ; 
      
      date = document.createElement("div") ; 
      date.innerHTML = emails[i].timestamp ; 
      date.className = "date" ; 

      li.append(sender);
      li.append(subject);
      li.append(date); 
      li.email_id = emails[i].id ; 
      li.onclick = (event) =>{ 
        console.log("on click id = " , emails[i].id ); 
        load_email(event.currentTarget.email_id) ; 
      };  

      if (emails[i].read){
        li.style.backgroundColor = "#e3e3e3" ; 
      }else{
        li.style.backgroundColor = "#f5f5f5" ; 
      }
       container.append(li) ; 

      
    }
    
}

function send_email(){
  let recipients = document.querySelector("#compose-recipients").value;
  let subjects = document.querySelector("#compose-subject").value;
  let bodys = document.querySelector("#compose-body").value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subjects,
      body: bodys
    })
  })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);
    });

}

