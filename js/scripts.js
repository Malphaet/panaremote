/*function uniKeyCode(event) {
    var key = event.keyCode;
    document.getElementById("demo2").innerHTML = "Unicode KEY code: " + key;
}*/
$(document).ready(function() {
    $("#shutter").html("SHUTTER : ?");
    document.addEventListener('keydown', (event) => {
      const keyName = event.key;
      if (keyName=="a"){
        alert('keydown event\n\n' + 'key: ' + keyName);
        $.ajax({
        type: "GET",
        url: "http://192.168.0.8/cgi-bin/proj_ctl.cgi?key=shutter_on&lang=e&osd=on",
        dataType: 'json',
        async: false,
        headers: {
          "Authorization": "Basic " + btoa("admin1 : panasonic")
        },
        data: '',
        success: function (){
          alert('keydown event\n\n' + 'key: ' + keyName);
        }});
      };
    });
});
