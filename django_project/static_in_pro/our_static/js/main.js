
$(document).ready(function(){

    /* ===============
    Side Bar : Switch from app to app
    ==================*/

    $(".switchpage").click(function(event){

        event.preventDefault();

        // Grab page variable which tells the server what template to load
        var i = $(this).attr("id");

        // Get request sent to templates.views
        $.get("/load-create-template/", {button:i}).done( function(response) {

            $("#main").html(response);
        });
    });
});



/*=================
Choose an email list to send a blast to
=================*/

function emailListOnChange(listname){

    // Preview the contact CSV by sending a file name to the server and
    // returning a pandas DataFrame.head() object

    $.get("/previewlist/", {filename:listname}).done(function(response) {

        var preview = response.preview_list;
         
        $("#show-list-preview").html(preview);
        $("#chosen-list").html(listname);
    });
    
}

/* ==============
Choose a template to use in your email blast
=================*/

function showTemp(val){

    $.get("/show-template/", {temp:val}).done(function(response) {
        
        var temp_subject = response.subject;
        var temp_body = response.body;

        $("#showsubject").html(temp_subject);
        $("#showbody").html(temp_body);
        $("#chosen-template").html(val);

    });

}



/* ==============
Send an Email Blast
==============*/

function sendBlast() {
    // Store selected contact list CSV and Email Template names in variables
    var e_list = $("#chosen-list").html();
    var email_template = $("#chosen-template").html();
    var google_user = $("#google-user").val();
    // Initiate email attachments list
    var attachments = [];
    console.log(google_user);
    // Find attachments chosen and append each to a list
    if ($('#attachment-list').is(':empty') ) {

    }
    else {
        var i = 0
        $("#attachment-list li").each( function(){
            // Append each attachment to list
            var val = $(this).html();
            var file = val.split('<button ')[0];
            attachments.push(file);

            });
        // Prepare a string to send to server (**NOTE** ran into some trouble
        // sending a javascript array to Django view so need to package array
        // as a string and unpack from string to python list after it was sent
        var att_str = attachments.join("*JOINTO*");

    }
    // This alerts the user if they forgot to attach either a template or list

    if ($('#chosen-list').is(':empty') && $('#chosen-template').is(':empty')) {

        alert("You need to pick an email list AND a template ya fuckwad!");
    }
    else if ($('#chosen-list').is(':empty')) {
        alert("Didn't pick a list, stooopid...");

    }
    else if ($('#chosen-template').is(':empty')) {
        alert("Didn't pick an email template, stooopid...");

    }
    else {
        // Alert to confirm emails being sent
        confirm_blast = confirm("You are about to send a " + email_template + " email blast to the " +
            " recipients in the " + e_list + " file. Is that Okay?");
        if (confirm_blast == true) {

            // Get email template and email list and store in JSON
            var j = {email_list: e_list, email_template: email_template, att_str: att_str, google_user: google_user}

            // Send JSON GET request to to sendmail.views
            $.get("/email-blast/", j).done(function (response) {
                var r = response
                console.log(r);
            });
        }

        else {
            alert("canceled");
        }

    }

    
}

/*=============
Add an attachment to attachment list
==============*/

function addAttachment(val) {

    // Assigns each appended attachment a class for deletion purposes

    if( $('#attachment-list').is(':empty') ) {

        var base = 0;

    }
    else {

        var att_class = $("#attachment-list li").last().attr('class');
        var class_split_arr = att_class.split("-");
        var i_str = class_split_arr[1];
        var base = parseInt(i_str);

    }

    var count = $('#attachment-list li').length

    i = base + 1;

    // Attaches a li item to the ul with a delete button

    var add_li_str = '<li class="' + 'attachment-' + i +'">' + val + '<button onclick="removeAttachment(this.name)" name="' + i+ '">DELETE</button></li>';
    $("#attachments ul").append(add_li_str);
    
}

/*==============
Remove Attachment from Email Blast function
================*/

function removeAttachment(class_name){

    var remove_class = ".attachment-" + class_name
    $(remove_class).remove();

}

/*==============
Remove Attachment from Email Blast function
================*/

function deleteAttachment(attachmentfile){
    confirm_delete = confirm("You are about to delete " + attachmentfile + ". Are you sure you want to delete this file?");
    
    if (confirm_delete == true) {

        j = {file:attachmentfile}

        $.get("/delete-attachment/", j).done(function (response) {

            $("#main").html(response);

        });
    }
    else{
    }
}

function deleteEmailList(listfile){
    confirm_delete = confirm("You are about to delete " + listfile + ". Are you sure you want to delete this file?");
    
    if (confirm_delete == true) {

        j = {file:listfile}

        $.get("/delete-list-file/", j).done(function (response) {

            $("#main").html(response);

        });
    }
    else{
    }
}