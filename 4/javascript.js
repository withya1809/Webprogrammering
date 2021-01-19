var addressBook = new Book();

//AddToBook("Dole","98765432","dole@hotmail.no");

function Book() {
  this.contacts = [];
  this.currentId = 0;
}

Book.prototype.addContact = function(contact){
  contact.id = this.newId();
  this.contacts.push(contact);
}

Book.prototype.newId = function(contact){
  this.currentId += 1;
  return this.currentId;
}

Book.prototype.deleteContact = function(id) {
  for (var i=0; i< this.contacts.length; i++) {
    if (this.contacts[i]) {
      if (this.contacts[i].id == id) {
        delete this.contacts[i];
        return true;
      }
    }
  };
  return false;
}

Book.prototype.findContactByName = function(name) {
  for (var i=0; i< this.contacts.length; i++) {
    if (this.contacts[i]){
      if (this.contacts[i].name == name) {
        return this.contacts[i];
      }
    }
  };
  return false;
}

Book.prototype.findContactByNr = function(nr) {
  for (var i=0; i< this.contacts.length; i++) {
    if (this.contacts[i]){
      if (this.contacts[i].tel == nr) {
        return this.contacts[i];
      }
    }
  };
  return false;
}

Book.prototype.findContactByMail = function(mail) {
  for (var i=0; i< this.contacts.length; i++) {
    if (this.contacts[i]){
      if (this.contacts[i].email == mail) {
        return this.contacts[i];
      }
    }
  };
  return false;
}

Book.prototype.Liste = function() {
  let id_liste = [];

  for (var i=0; i< this.contacts.length; i++) {
    if (this.contacts[i]) {
      id_liste.push(this.contacts[i].id)
    }
  };
  return id_liste;
}



function Contact(name, tel, email){
  this.name = name;
  this.tel = tel;
  this.email = email;
}



function validateForm(){

  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var phone_regex = /[0-9() +-]{5,}/;

  //Navn-felt er tomt
  if (document.getElementById('name').value == ""){
    alert("Name must be filled out");
  }

  // Både tlf og email er tomt
  else if(document.getElementById('tel').value == "" && document.getElementById('email').value == ""){
    alert("Must fill inn either phone number or email address! ");
  }

  //Tlf tom, riktig mail
  else if (document.getElementById('tel').value == "" && mailformat.test(document.getElementById('email').value) == true) {
    AddToBook();
    document.forms[0].reset();
  }

  //Mail tom, riktig tlf
  else if(document.getElementById('email').value == "" && phone_regex.test(document.getElementById('tel').value) == true){
    AddToBook();
    document.forms[0].reset();
  }

  //Invalid email
  else if(mailformat.test(document.getElementById('email').value) == false )
  {
    alert("Invalid email address !");
  }

  //Invalid phone number
  else if(phone_regex.test(document.getElementById('tel').value) == false){
    alert("Invalid phone number !");
  }



  else{

    AddToBook();
    document.forms[0].reset(); //clears form
    //console.log(addressBook.Liste());
  }

}




function AddToBook(){


  var name_input = document.getElementById('name').value;
  var tel_input  = document.getElementById('tel').value;
  var email_input  = document.getElementById('email').value;

  var new_contact = new Contact(name_input,tel_input,email_input);
  addressBook.addContact(new_contact);


  let book_container  = document.getElementById('book_container'),
    div_1 = document.createElement('div'),
      div_2 = document.createElement('div'),
        ul = document.createElement('ul'),
          li_1 = document.createElement('li'),
          li_2 = document.createElement('li'),
          li_3 = document.createElement('li'),
            a = document.createElement('a'),



      div_3 = document.createElement('div'),
        button_1 = document.createElement('button'),
          img_1 = document.createElement('img'),
        button_2 = document.createElement('button'),
          img_2 = document.createElement('img');

  let  name_content = document.createTextNode(new_contact.name),
        tel_content = document.createTextNode(new_contact.tel),
      email_content = document.createTextNode(new_contact.email);

      book_container.appendChild(div_1);
      div_1.classList.add("each_container");

      div_1.id = new_contact.id;

      div_1.appendChild(div_2);
      div_2.classList.add("contact_info");
        div_2.appendChild(ul);
          ul.appendChild(li_1);
          ul.appendChild(li_2);
          ul.appendChild(li_3);
            li_1.appendChild(name_content);
            li_2.appendChild(tel_content);
            li_3.appendChild(a);
              a.appendChild(email_content);
              a.href = "mailto:email_content";



      div_1.appendChild(div_3);
      div_3.classList.add("knapper");
        div_3.appendChild(button_1);

          button_1.appendChild(img_1);
          button_1.type = "button";

          // FUNCTION TO DELETE CONTACTS
          button_1.onclick = function() {

            var result = confirm("Are you sure you want to delete this contact?");
            if (result){
              var this_id = new_contact.id;
              var element = document.getElementById(this_id);

              element.parentNode.removeChild(element);
              addressBook.deleteContact(this_id);
              console.log(addressBook);
            }

          };

          img_1.src = "delete_button.png";
          img_1.classList.add("img_size");

        div_3.appendChild(button_2);
          button_2.appendChild(img_2);
          button_2.type = "button";

          // FUNCTION TO EDIT CONTACT
          button_2.onclick = function(){
            var new_name = prompt("Enter new name: ");
            var new_phone = prompt("Enter new phone number");
            var new_mail = prompt("Enter new mail");

            var this_id = new_contact.id;
            var element = document.getElementById(this_id).getElementsByTagName("LI");


            element[0].innerHTML = new_name;
            element[1].innerHTML = new_phone;
            var x = document.getElementById(this_id).getElementsByTagName("a");

            x[0].innerHTML = new_mail;

          }


          img_2.src = "edit_button.png";
          img_2.classList.add("img_size");

}


//function find(){
//style = "display:none" på alle de som ikke matcher
//sett alle med ulik id til display none
//finn elementet som matcher, finn id til den,
//iterer igjennom contacts, lag ny liste, add de id som ikke matcher med den som ble søkt opp
//lag for løkke, iterer igjennom ny liste og getElementById(id).style.display ="none"
/*
function Hide(){
  var input = document.getElementById('search').value;
  let id_x = addressBook.findContactByName(input).id;

  for (var i=0; i < addressBook.Liste().length; i++){
    if (addressBook.Liste()[i] == id_x){
      document.getElementById(id_x).style.display = "";
    }
    else{
      document.getElementById(addressBook.Liste()[i]).style.display = 'none';
    }
  };
}
*/
/*
function searchFunction(){

  var input = document.getElementById('search');
  var filter = input.value.toUpperCase();
  var div = document.getElementById("book_container");
  var li = div.getElementsByTagName("li");

  for (i = 0; i< li.length; i++){
    var parentOfThisID = li[i].parentElement.parentElement.parentElement.id;
    var text = li[i].textContent || li[i].innerText;

    if (text.toUpperCase().includes(filter) == false){
      document.getElementById(parentOfThisID).style.display = "none";
    }

  };
}
*/
/*
  for (i = 0; i< li.length; i++){
    var li_parent = li[i].parentElement;
    var ul_parent = li_parent.parentElement;
    var div_parent = ul_parent.parentElement;
    var div_id = div_parent.id;

    var a = li[i];
    var txtValue = a.textContent || a.innerText;
    //console.log(a.innerText);

    if (txtValue.toUpperCase().includes(filter) == true) {
        document.getElementById(div_id).style.display = "";
    } else {
        document.getElementById(div_id).style.display = "none";
    }
  };

*/








function Hide(){
  var input = document.getElementById('search').value;



  if (document.getElementById('select').value == "navn"){
    let id_x = addressBook.findContactByName(input).id;

    for (var i=0; i < addressBook.Liste().length; i++){
      if (addressBook.Liste()[i] == id_x){
        document.getElementById(id_x).style.display = "";
      }
      else{
        document.getElementById(addressBook.Liste()[i]).style.display = 'none';
      }
    };

  }


  else if (document.getElementById('select').value == "tlf") {
    let id_y = addressBook.findContactByNr(input).id;

    for (var i=0; i < addressBook.Liste().length; i++){
      if (addressBook.Liste()[i] == id_y){
        document.getElementById(id_y).style.display = "";
      }
      else{
        document.getElementById(addressBook.Liste()[i]).style.display = 'none';
      }
    };
  }

  else if (document.getElementById('select').value == "mail"){
    let id_z = addressBook.findContactByMail(input).id;

    for (var i=0; i < addressBook.Liste().length; i++){
      if (addressBook.Liste()[i] == id_z){
        document.getElementById(id_z).style.display = "";
      }
      else{
        document.getElementById(addressBook.Liste()[i]).style.display = 'none';
      }
    };
  }


}


function displayAll(){
  for (var i=0; i < addressBook.Liste().length; i++){
    document.getElementById(addressBook.Liste()[i]).style.display = "";
  };
}



function fontChange(){
  if (document.getElementById('font-select').value == "Squada"){
    for (var i=0; i < addressBook.Liste().length; i++){
      document.getElementById(addressBook.Liste()[i]).classList.add("each_container_squada");
    };
  }


  if (document.getElementById('font-select').value == "Noto"){
    for (var i=0; i < addressBook.Liste().length; i++){
      document.getElementById(addressBook.Liste()[i]).classList.add("each_container_noto");
    };
  }

  if (document.getElementById('font-select').value == "Sri"){
    for (var i=0; i < addressBook.Liste().length; i++){
      document.getElementById(addressBook.Liste()[i]).classList.add("each_container_sri");
    };
  }

}


function delete_1(){
  var result = confirm("Are you sure you want to delete this contact?");
  if (result){
    var element =  document.getElementById("dummy_1");
    element.parentNode.removeChild(element);

  }
}

function delete_2(){
  var result = confirm("Are you sure you want to delete this contact?");
  if (result){
    var element =  document.getElementById("dummy_2");
    element.parentNode.removeChild(element);

  }
}

function delete_3(){
  var result = confirm("Are you sure you want to delete this contact?");
  if (result){
    var element =  document.getElementById("dummy_3");
    element.parentNode.removeChild(element);

  }
}


function edit_1(){
  var new_name = prompt("Enter new name: ");
  var new_phone = prompt("Enter new phone number");
  var new_mail = prompt("Enter new mail");

  var element = document.getElementById("dummy_1").getElementsByTagName("LI");

  element[0].innerHTML = new_name;
  element[1].innerHTML = new_phone;
  var x = document.getElementById("dummy_1").getElementsByTagName("a");

  x[0].innerHTML = new_mail;
}


function edit_2(){
  var new_name = prompt("Enter new name: ");
  var new_phone = prompt("Enter new phone number");
  var new_mail = prompt("Enter new mail");

  var element = document.getElementById("dummy_2").getElementsByTagName("LI");

  element[0].innerHTML = new_name;
  element[1].innerHTML = new_phone;
  var x = document.getElementById("dummy_2").getElementsByTagName("a");

  x[0].innerHTML = new_mail;
}

function edit_3(){
  var new_name = prompt("Enter new name: ");
  var new_phone = prompt("Enter new phone number");
  var new_mail = prompt("Enter new mail");

  var element = document.getElementById("dummy_3").getElementsByTagName("LI");

  element[0].innerHTML = new_name;
  element[1].innerHTML = new_phone;
  var x = document.getElementById("dummy_3").getElementsByTagName("a");

  x[0].innerHTML = new_mail;
}



//console.log(addressBook.Liste());

console.log(addressBook);

//console.log(addressBook.contacts);
