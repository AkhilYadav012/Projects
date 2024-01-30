
function clearErrors(){
    document.getElementById("Message").innerHTML = "";
}


    
function validate() {
    let a="^[A-Za-z]\\w{4,10}$";


    let name = document.getElementById("name").value;
   

    if ( name.match(a) ) 
    {
        
       
        document.getElementById('username-display').textContent = name;
      document.getElementById('login-form').style.display = 'none';
      document.getElementById('user-info').style.display = 'block';
      
       
    }
    else
     { 
        document.getElementById("Message").innerHTML="** Wrong Username";
        return false;
       
    }
   
}