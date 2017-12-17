
pk = {{pk}}
 $(document).ready(function () {
  urlname = ''
  $("#classify").click(function () {
    urlname = '/' + {{pk}}
    data =  $('#text').val();
    alert(urlname)

    $.ajax({

      url: urlname,
      type: 'get',
      
    });




    });
  

});