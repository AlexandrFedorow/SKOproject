
for(var i=0; i<=10; i++){
  var el = document.getElementById(i);
  if (el.innerHTML == '-'){
    el.style.backgroundColor = 'red';
  }
  else{
    el.style.backgroundColor = 'green';
  }
}
