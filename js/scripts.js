/*function uniKeyCode(event) {
    var key = event.keyCode;
    document.getElementById("demo2").innerHTML = "Unicode KEY code: " + key;
}*/
document.addEventListener('keydown', (event) => {
  const keyName = event.key;
  if (keyName=="a"){

  $.ajax
  ({
  type: "GET",
  url: "URL",
  dataType: 'json',
  async: false,
  username: 'admin1',
  password: 'panasonic',
  data: '{ "comment" }',
  success: function (){
    alert('keydown event\n\n' + 'key: ' + keyName);
  }
  });
});
