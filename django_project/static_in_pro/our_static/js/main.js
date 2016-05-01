
$(document).ready(function(){

    /* Switch from Page App to Page App */

    $(".switchpage").click(function(event){
        event.preventDefault();

        var i = $(this).attr("id");

        $.get("/load-create-template/", {button:i}).done( function(response) {

            $("#main").html(response);
        });
    });
});



/* Choose an email list to send a blast to */
function emailListOnChange(listname){
    console.log(listname);
     $.get("/previewlist/", {filename:listname}).done(function(response) {

        console.log(response);
        var preview = response.preview_list;
         
        $("#show-list-preview").html(preview);
        $("#chosen-list").html(listname);
    });
    
}

/* Choose a template to use in your email blast */
function showTemp(val){

    $.get("/show-template/", {temp:val}).done(function(response) {
        
        var temp_subject = response.subject;
        var temp_body = response.body;

        $("#showsubject").html(temp_subject);
        $("#showbody").html(temp_body);
        $("#chosen-template").html(val);

    });

}



/* Send an Email Blast */
function sendBlast() {

    var e_list = $("#chosen-list").html();
    var email_template = $("#chosen-template").html();

    var attachments = [];

    /* Find attachments chosen and append each to a list */

    if ($('#attachment-list').is(':empty') ) {

    }
    else {
        var i = 0
        $("#attachment-list li").each( function(){

            var val = $(this).html();
            var file = val.split('<button ')[0];
            console.log(file);
            attachments.push(file);

            });
        var att_str = attachments.join("*JOINTO*");
        console.log(att_str);
    
    }

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
        confirm_blast = confirm("You are about to send a " + email_template + " email blast to the " +
            " recipients in the " + e_list + " file. Is that Okay?");
        if (confirm_blast == true) {

            /* Get email template and email list*/
            console.log("blastin bro, blastin!");
            var j = {email_list: e_list, email_template: email_template, att_str: att_str}
            console.log(j)
            $.get("/email-blast/", j).done(function (response) {
            
                console.log(response);
            });
        }

        else {
            alert("canceled");
        }

    }

    
}

/* Add an attachment to attachment list*/

function addAttachment(val) {
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

    console.log(i);
    var add_li_str = '<li class="' + 'attachment-' + i +'">' + val + '<button onclick="removeAttachment(this.name)" name="' + i+ '">DELETE</button></li>';
    $("#attachments ul").append(add_li_str);
    
}

function removeAttachment(class_name){

    remove_class = ".attachment-" + class_name
    $(remove_class).remove();

}