
var count;
count = 1;
    function increase(){

      count = (count + 1) % 10;
      document.getElementById("qwer").src = "{{url_for('static', filename='image/AA/2.jpg')}}"
}